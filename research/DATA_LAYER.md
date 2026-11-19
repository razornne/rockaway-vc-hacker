# Checking the data layer: open dumps of the Czech business register

16 November 2026. Source: dataor.justice.cz, `sro-full-praha-2026.xml.gz` — 362 MB, full extracts with history for every s.r.o. registered at the Prague Municipal Court. Parser: `prototype/registry_parse.py`; output: `data/praha_sro_holders.jsonl` (not committed). Natural persons are not stored.

## What worked

- 312,713 companies, 98,723 of them with legal-entity shareholders. Processing takes 4.5 minutes on a laptop.
- The data matches the manual check. Campiri: Rockaway Ventures Fund SCSp SICAV-RAIF from 4 May 2022. Cruxo: Rockaway, Czech Founders, Presto, ZAKA from 24 Aug 2026. Filuta: Filuta AI Inc. ValkaAI: Valka.AI B.V.
- The "venture capital person" label (osoba rizikového kapitálu) is used by 45 entities across 139 companies, mostly small Czech vehicles; large funds do not use it.

## What did not work

**Of the 14 Rockaway Ventures deals, 2 are visible in the Prague register (Campiri, Cruxo).** The rest:
- foreign holding: Filuta (Delaware), ValkaAI (Netherlands), CulturePulse (Delaware);
- foreign companies: Apaleo, Spotawheel, Valpas, Remix, Raus, FreewayCamper, Vermeer;
- a.s. or SE without a public shareholder list: BottleCap AI (SE);
- no Czech entity: Navigara.

Companies per fund in the register (matched by entity name; noisy — includes the funds' own holdings):

| Fund | Companies | Fund | Companies |
|---|---|---|---|
| Reflex | 28 | Nation 1 | 10 |
| Presto | 22 | Tensor | 9 |
| J&T Ventures | 14 | Credo | 5 |
| Purple | 13 | Czech Founders | 5 |
| Tarpan | 12 | Kaya | ~0 (matches are a different Kaya) |

Credo and Kaya, the largest Czech VC funds, are almost invisible in the Prague register: their companies are usually held through foreign structures.

## Conclusion

1. **The register is not a map of the venture market.** It covers a small share of deals, and mostly not the strongest ones: strong companies move their holding abroad early.
2. **For a dossier on one company the register is useful.** If the company is there, it gives an exact ownership history, dates and share classes. If it is not, that is a fact too: "holding abroad".
3. **The register works better for mature Czech companies:** profitable SMEs, family firms, defence suppliers. They have a Czech entity, mandatory filings in the Collection of Deeds (Sbírka listin) and public contracts. See the defence research in `research/defense/`.

## Side finding

The register contains Rockaway Defense Advisors s.r.o. (from 26 Mar 2025) and Rockaway Defense B1 s.r.o. (from 23 Jan 2026, shareholder Rockaway Alpha Fund SICAV a.s.). B1 looks like an acquisition vehicle. Rockaway Defense is a sub-fund of Rockaway Alpha Fund SICAV.
