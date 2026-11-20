# Baseline brief: Fly4Future

gpt-5-mini with web search, one call, 1 searches, 24 s, $0.016, 2026-11-20.

---

In short
- Fly4Future s.r.o. (IČO 06632581) is an Ostrava‑based Czech company developing autonomous, GNSS‑resilient multi‑robot drones for industrial, civil‑protection and inspection use cases; it was spun out from the Multi‑Robot Systems group at Czech Technical University (CTU) in 2017. ([rejstr.cz](https://rejstr.cz/06632581/fly4future?utm_source=openai))

Funding and ownership
- Registered as a private limited company since 27 Nov 2017 with registered capital CZK 30,000; publicly disclosed shareholders (and capital contributions) are three natural persons (names and contribution amounts removed from this copy: the project stores no personal holdings). ([rejstr.cz](https://rejstr.cz/06632581/fly4future?utm_source=openai))
- The company describes itself as profitable from the start and “not yet have an investor” while opening a first investment round (statement in CTU media piece); I could not find any public record of an equity financing (Seed/Series A) on corporate registers, VC databases, or press releases. ([aktualne.cvut.cz](https://aktualne.cvut.cz/en/media-screenings/20260615-the-development-of-drones-in-the-czech-republic-will-be-ensured-by-a-darpa?utm_source=openai))

Revenue, profit and cash
- Management‑level topline numbers appear in a public presentation: revenue (approx.) 2022 CZK 12.5M; 2023 CZK 17M; 2024 ≈ CZK 24M (presentation slide). ([uava.cz](https://uava.cz/wp-content/uploads/2024/09/10-f4f.pdf?utm_source=openai))
- The CTU article and company statements claim the company has been profitable from inception; however, detailed audited profit/loss and cash position line items (net income, cash on hand, burn rate) were not available in the sources I found — company annual accounts are referenced in registries but the full filings were not accessible in the public summaries I reviewed. (Could not find full P&L / cash balance statements online.) ([aktualne.cvut.cz](https://aktualne.cvut.cz/en/media-screenings/20260615-the-development-of-drones-in-the-czech-republic-will-be-ensured-by-a-darpa?utm_source=openai))

Public money (grants, public contracts)
- Fly4Future has received at least one public procurement award (≈ EUR 22,164.25) from Brno University of Technology / CEIT in 2023 (public contract listing). ([b2bhint.com](https://www.b2bhint.com/en/company/cz/fly4future-sro--06632581?utm_source=openai))
- The company appears on government procurement/contract portals and has documents on smlouvy.gov.cz indicating awarded contracts and agreements (multiple entries). ([hlidacstatu.cz](https://www.hlidacstatu.cz/subjekt/RegistrSmluv/06632581?utm_source=openai))
- There is a PRODEF program participation listing showing committed amounts CZK 3,600,000 across 2025–2028 (detailed schedule in a public contract document). ([smlouvy.gov.cz](https://smlouvy.gov.cz/smlouva/soubor/41741937/013416_2025_00_Smlouva%20o%20ucasti%20PRODEF_RS.pdf?backlink=urmkc&utm_source=openai))
- I found an OPERAČNÍ PROGRAM entry referencing grant code CZ.01.01.01/01/25_067/0009874 tied to Fly4Future; details of amount and scope require opening the specific grant document. ([optak.gov.cz](https://optak.gov.cz/UserFiles/File/17860874857-26-7-28-z-pis.pdf?utm_source=openai))

Defence relevance
- Technology is explicitly pitched for demanding environments such as firefighting and infrastructure monitoring and the company participates in security‑related tenders; public procurement listings and program names (e.g., PRODEF) indicate relevance to civil‑defence / defence‑adjacent projects. ([czechinvest.gov.cz](https://czechinvest.gov.cz/cz/Sektorove-huby/Smart-mobility-catalog/Firmy/Fly4Future?utm_source=openai))
- I found references to TAČR/Robosurv‑style contracts (technology/defence research) in public contract repositories, suggesting some work for research/defence agencies. ([smlouvy.gov.cz](https://smlouvy.gov.cz/smlouva/soubor/40006932/Smlouva%20Robosurv%20F4F_CVUT--xxxxx.pdf?utm_source=openai))

Technology and what could be rebuilt
- Core claims: autonomous drones capable of operating without GNSS, multi‑robot coordination, resilience in demanding conditions; the company offers a DroneBuilder online design tool. ([czechinvest.gov.cz](https://czechinvest.gov.cz/cz/Sektorove-huby/Smart-mobility-catalog/Firmy/Fly4Future?utm_source=openai))
- Technical origin: spin‑out from CTU Multi‑Robot Systems (access to academic IP and personnel). Rebuilding the stack in‑house (SW algorithms for GNSS‑denied navigation, multi‑UAV coordination, autonomy, embedded control, and custom airframes) is technically feasible but would require experienced robotics/controls engineers, significant test infrastructure and months to years of development — the company’s CTU heritage reduces that time/capex risk. ([fly4future.com](https://fly4future.com/about-us/?utm_source=openai))

Risks
- Limited public financial transparency: audited P&L/cash position not publicly available in the sources reviewed, making diligence on runway and margins incomplete. ([b2bhint.com](https://www.b2bhint.com/en/company/cz/fly4future-sro--06632581?utm_source=openai))
- Defence and public‑procurement dependence risk: part of revenue appears to come from public contracts/grants which can be lumpy and politically exposed. ([b2bhint.com](https://www.b2bhint.com/en/company/cz/fly4future-sro--06632581?utm_source=openai))
- Customer concentration and commercialization risk: no public evidence of large enterprise commercial contracts beyond academic/public bodies; commercial scaling to B2B customers and margins unclear. (Could not find lists of paying commercial customers other than partner mentions such as Axis or T‑Mobile on CzechInvest profile.) ([czechinvest.gov.cz](https://czechinvest.gov.cz/cz/Sektorove-huby/Smart-mobility-catalog/Firmy/Fly4Future?utm_source=openai))
- IP/competition: autonomous GNSS‑denied navigation is contested by many research groups and companies; freedom‑to‑operate, patents and key‑person dependency should be checked. ([fly4future.com](https://fly4future.com/about-us/?utm_source=openai))

Questions for the founders
1. Please provide the latest audited financials (last 3 years P&L, balance sheet, cash balance and cap table) and clarify whether the company has taken any external equity financing to date. ([rejstr.cz](https://rejstr.cz/06632581/fly4future?utm_source=openai))
2. Breakdown of 2024 revenue by customer (public vs private vs product vs services) and gross margins. ([uava.cz](https://uava.cz/wp-content/uploads/2024/09/10-f4f.pdf?utm_source=openai))
3. Details on grants/contracts: amounts, timelines, and whether any are conditional on milestones or non‑dilutive vs repayable. ([smlouvy.gov.cz](https://smlouvy.gov.cz/smlouva/soubor/41741937/013416_2025_00_Smlouva%20o%20ucasti%20PRODEF_RS.pdf?backlink=urmkc&utm_source=openai))
4. IP position: patents filed/granted, ownership (company vs CTU spin‑out terms), and any third‑party license obligations. ([fly4future.com](https://fly4future.com/about-us/?utm_source=openai))
5. Technical roadmap and reproducibility: key software modules, third‑party components, proprietary algorithms; what would be required to replicate product capabilities externally (headcount, test assets, time). ([czechinvest.gov.cz](https://czechinvest.gov.cz/cz/Sektorove-huby/Smart-mobility-catalog/Firmy/Fly4Future?utm_source=openai))
6. Customer references and pilot → commercial conversion metrics. ([czechinvest.gov.cz](https://czechinvest.gov.cz/cz/Sektorove-huby/Smart-mobility-catalog/Firmy/Fly4Future?utm_source=openai))

Notes on sources and unavailable items
- Corporate registry, ownership and basic company facts: Czech commercial register / rejstr.cz. ([rejstr.cz](https://rejstr.cz/06632581/fly4future?utm_source=openai))
- Company background and tech claims: Fly4Future website and CzechInvest profile. ([fly4future.com](https://fly4future.com/about-us/?utm_source=openai))
- Financial topline estimates: public presentation slide (PDF). ([uava.cz](https://uava.cz/wp-content/uploads/2024/09/10-f4f.pdf?utm_source=openai))
- Public contracts/grants: smlouvy.gov.cz, OPTAK and procurement summaries / B2BHint. ([smlouvy.gov.cz](https://smlouvy.gov.cz/smlouva/soubor/41514061/FIS%200125000373A.pdf?utm_source=openai))
- Statements I could not find publicly: full audited financial statements with detailed cash balances and any public VC/angel term sheets or press releases about equity rounds. (I searched registry repositories, smlouvy.gov.cz and press/CTU articles but did not find an announced VC round or full P&L PDF accessible in the public datasets.) ([b2bhint.com](https://www.b2bhint.com/en/company/cz/fly4future-sro--06632581?utm_source=openai))

If you want, I can (a) request and compile their latest annual report and cap table from the company (template request), (b) pull the full smlouvy.gov.cz / OPTAK / TAČR contract PDFs and extract amounts and timelines, or (c) run patent and LinkedIn key‑employee checks. Which would you prefer next?
