"""Filed annual accounts are read by code and accepted only when the balance sheet balances."""
from dd.accounts import parse_accounts

# layout text as pypdf gives it for real Czech filings (trimmed); the two forms number their rows differently
SIMPLIFIED = """
                                                                ROZVAHA
                                                       ve zjednodušeném rozsahu
                                                              ke dni 31.12.2025
                                                               (v celých tisících Kč)
   Označení                                Název                              Číslo       brutto           korekce             netto            minulé
A                  AKTIVA CELKEM                                                 1              36 631            -3 858            32 773            23 617
A C.II.            Pohledávky                                                    9               9 307                 0             9 307             5 475
A C.II.2.          Krátkodobé pohledávky                                        11               9 307                 0             9 307             5 475
A C.IV.            Peněžní prostředky                                           14              19 605                 0            19 605            15 119
   Označení                                                  Název                                                Číslo        netto            minulé
P                  PASIVA CELKEM                                                                                    15              32 773            23 617
P A.               Vlastní kapitál                                                                                  16               5 545             1 382
P A.V.             Výsledek hospodaření běžného účetního období                                                     21               4 163               -27
"""

FULL_PNL = """
                                                    VÝKAZ ZISKU A ZTRÁTY
                                                       ke dni 31.12.2025
                                                    (v celých tisících Kč)
      I.        Tržby z prodeje výrobků a služeb                                                              1                   47 786                        45 036
  D.            Osobní náklady                                                    Součet D.1. až D.2.         9                   30 366                        19 380
      *         Provozní výsledek hospodaření (+/-)             I. + II. - A. - B. - C. - D. - E. + III. - F.30                   18 605                        17 292
     **        Výsledek hospodaření po zdanění (+/-)                                          ** (ř. 49) - L.    53                      8 837                        16 570
"""
FULL_BALANCE = """
                                                        ROZVAHA ke dni 31.12.2025 (v celých tisících Kč)
               AKTIVA CELKEM                         Součet A. až D.      1              89 657                  4 366               85 291                71 010
C.IV.          Peněžní prostředky                                         13             57 141                                      57 141                58 771
               PASIVA CELKEM                                                           Součet A. až D.      15                   85 291                        71 010
A.V.           Výsledek hospodaření běžného účetního období (+/-)                                           21                     8 837                        16 570
"""


def test_simplified_balance_sheet_without_income_statement():
    r = parse_accounts([SIMPLIFIED])
    assert r["readable"] and r["period_end"] == "2025-12-31" and not r["pnl_published"] and r["revenue"] is None
    assert r["balance"]["cash"] == {"current": 19_605_000, "prior": 15_119_000}
    assert r["balance"]["receivables"]["current"] == 9_307_000          # not the "Krátkodobé pohledávky" sub-row
    assert r["balance"]["net_result"] == {"current": 4_163_000, "prior": -27_000}


def test_full_income_statement_and_cross_checks():
    r = parse_accounts([FULL_BALANCE, FULL_PNL])
    assert r["readable"] and r["revenue"] == 47_786_000
    assert r["pnl"]["operating_result"]["current"] == 18_605_000      # row number glued to a formula
    assert r["checks"] == {"assets_equal_equity_and_liabilities": True, "net_result_matches_balance_sheet": True}


def test_unbalanced_or_scanned_accounts_are_not_used():
    broken = SIMPLIFIED.replace("15              32 773", "15              32 774")  # total liabilities misread
    assert parse_accounts([broken])["readable"] is False
    assert "scanned" in parse_accounts([""])["reason"]


# a third form (Spaceti 2025): no row-number column, no thousands spaces, CZK instead of Kč, assets over two pages
NO_ROWNUM = ["""
                             Rozvaha pro podnikatele, v plném rozsahu
                             ke dni 31.12.2025 (v celých tisících CZK)
                 AKTIVA CELKEM                                             106223       65059       41164       49789
""", """
C.IV.             Peněžní prostředky                                            5796             0       5796       12749
""", """
                   PASIVA CELKEM                                                                  41164              49789
A.                 Vlastní kapitál                                                                17866              26271
A.V                Výsledek hospodaření běžného účetního období (+/-)                            -10371             -25076
"""]


def test_form_without_row_numbers():
    r = parse_accounts(NO_ROWNUM)
    assert r["readable"] and r["balance"]["total_assets"] == {"current": 41_164_000, "prior": 49_789_000}
    assert r["balance"]["cash"] == {"current": 5_796_000, "prior": 12_749_000}  # continuation page, "0" is not a row number
    assert r["balance"]["net_result"]["current"] == -10_371_000


def test_income_statement_that_disagrees_with_balance_sheet_is_not_used():
    bad_pnl = FULL_PNL.replace("53                      8 837", "53                      8 873")
    r = parse_accounts([FULL_BALANCE, bad_pnl])
    assert r["readable"] is False and "net result" in r["reason"]
