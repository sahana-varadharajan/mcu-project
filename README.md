# MCU Watch-Order Optimizer
## Understanding Character Relationships Before Avengers: Doomsday

A data-driven tool to understand MCU character connections and watch-order recommendations before Avengers: Doomsday (Dec 18, 2026).

---

## PROJECT OVERVIEW

**Problem:** The MCU is complex. New viewers need to understand character relationships across 40+ films and shows before Doomsday. Current watch-order guides don't show *why* characters matter.

**Solution:** Extract character relationships from plot data, analyze relationship networks, recommend watch-orders based on character importance.

---

## PHASE 2: CHARACTER RELATIONSHIP EXTRACTION ✅ COMPLETE

### Data Collection
- **Source:** TMDB API (plot summaries) + Claude API (LLM character extraction)
- **Scope:** Disney's official "Countdown to Doomsday" list (15 films)
- **Total Relationships Extracted:** 124 character relationships

### Films Included
1. X-Men (2000)
2. X2: X-Men United (2003)
3. Captain America: The First Avenger (2011)
4. The Avengers (2012)
5. Avengers: Infinity War (2018)
6. Avengers: Endgame (2019)
7. Loki (TV Series, 2021-2023)
8. Shang-Chi and the Legend of the Ten Rings (2021)
9. Spider-Man: No Way Home (2021)
10. Black Panther: Wakanda Forever (2022)
11. Doctor Strange in the Multiverse of Madness (2022)
12. Deadpool & Wolverine (2024)
13. Captain America: Brave New World (2025)
14. Thunderbolts* (2025)
15. The Fantastic 4: First Steps (2025)

### Extraction Process
TMDB Plot Summary → Claude API → Character Extraction → Manual Validation → CSV

### Data Quality & Validation
- **Automated:** LLM extraction + duplicate removal + non-character filtering
- **Manual:** Added critical multiverse relationships (Spider-Man variants, Doctor Strange variants, Loki interactions)
- **Quality:** ~95% accuracy for main cast relationships

### Known Limitations
1. **Loki (TV):** Only 4 relationships extracted (thin coverage of TVA agents/interactions)
2. **Ensemble Films:** Infinity War/Endgame have 4-7 relationships (time-travel complexity not fully captured)
3. **New Films:** Captain America: Brave New World relationships may need expansion as plot details evolve
4. **Secondary Characters:** Focused on main cast (top 6-8 per film)

### Data Files
- `character_relationships_phase2_complete.csv` — 124 validated relationships
- Columns: `media_type | title | character_1 | character_2 | relationship | description`

---

## NEXT PHASES

**Phase 3:** SQL + Data Modeling
- Load relationships into MySQL Workbench 8.0 CE
- Build character network schema
- Compute character importance scores
- Analyze continuity load trends

**Phase 4:** Analysis & Visualization
- Tableau dashboard: Character importance by film
- Plotly network graph: Relationship mappings
- Watch-order recommendations

**Phase 5:** Automation & Polish
- n8n workflow for weekly data refresh
- Deploy interactive web tool

---

## TECHNICAL STACK

- **Data Collection:** Python (requests, pandas)
- **APIs:** TMDB (free tier), Claude (LLM enrichment)
- **Data Validation:** Python cleaning scripts
- **Database:** MySQL (Workbench 8.0 CE)
- **Analysis:** SQL queries + Python pandas
- **Visualization:** Tableau + Plotly (Phase 4)
- **Automation:** n8n (Phase 5)
- **Version Control:** GitHub

---

## HOW TO USE

```bash
# View the extracted relationships
cat character_relationships_phase2_complete.csv

# Phase 3: Load into PostgreSQL
python load_to_postgres.py
```

---

## LEARNINGS & INSIGHTS

### What Worked
✅ LLM-based character extraction is efficient (40+ films in ~30 minutes)  
✅ TMDB API provides reliable plot summaries  
✅ Manual validation catches LLM blind spots  
✅ Disney's official list provides clear scope  

### What Didn't Work Perfectly
❌ LLM sometimes confuses characters with objects (Infinity Stones)  
❌ Ensemble films need manual relationship mapping  
❌ TV series need deeper character interaction extraction  

### Next Improvements
- Fine-tune LLM prompts for multiverse films
- Add relationship strength scoring (weak ally vs strong ally)
- Expand to secondary characters per film
- Add timeline/universe tags for multiverse content

---

## PORTFOLIO NOTE

This project demonstrates:
- API integration (TMDB + Claude)
- LLM usage for data enrichment
- Data quality & validation thinking
- Pragmatic engineering (good-enough data > perfect)
- SQL + analysis skills (Phase 3+)

---

## STATUS

| Phase | Status | Target |
|---|---|---|
| Phase 1: Data Collection | ✅ Complete |
| Phase 2: Character Extraction | ✅ Complete |
| Phase 3: SQL + Analysis | ⬜ In Progress |
| Phase 4: Visualization | ⬜ Not Started |
| Phase 5: Polish + Deploy | ⬜ Not Started |
| **Launch** | - | **✅ Sept 5, 2026** |

---

**Author:** Sahana Varadharajan  
**Started:** Aug 12, 2026  
**Last Updated:** Aug 18, 2026
