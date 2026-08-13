# MCU Doomsday Watch-Order Optimizer
**Data-Driven Marvel Cinematic Universe Analysis & Recommendations**

---

## 📺 Project Overview

Confused about which MCU movies to watch before **Spider-Man: Brand New Day (2026)** or **Avengers: Doomsday (2026)**?

This project builds a **data-driven watch-order optimizer** that:
- Maps character relationships across the entire MCU
- Recommends the minimum viable watch list for any character/event
- Shows continuity load trends (is the MCU getting harder to follow?)
- Powers personalized recommendations before major releases

---

## 📊 Data Pipeline

### Phase 1: Movie Data Collection ✅ COMPLETE
- **Source:** TMDB API
- **Data:** 38 MCU films + metadata (budget, revenue, runtime, rating, popularity)
- **Output:** `mcu_movies_clean.csv`
- **Status:** 38/38 films collected, cleaned, validated

### Phase 2: Character Relationship Enrichment (IN PROGRESS)
- **Source:** LLM (Claude API) for entity extraction from plot summaries
- **Data:** Character pairs + relationship types (allies, enemies, mentors, etc.)
- **Output:** `character_relationships.csv`
- **Status:** Testing on sample films, scaling to full dataset

### Phase 3: Data Modeling & Analysis (PLANNED)
- Load into Postgres database
- Compute character importance scores
- Calculate continuity load per film
- Generate watch-order recommendations

### Phase 4: Visualization (PLANNED)
- Interactive network graph (Plotly)
- Tableau dashboard: character stats, continuity trends
- Watch-order recommendation engine

---

## 📂 Files

| File | Description |
|---|---|
| `mcu_movies_clean.csv` | 38 MCU films with complete metadata |
| `character_relationships.csv` | Character pairs + relationships (in progress) |
| `fetch_mcu_correct.py` | Script to fetch movie data via TMDB API |
| `extract_relationships.py` | Script to enrich data with LLM |

---

## 🚀 How to Use

### Run Phase 1 (Fetch MCU movies):
```bash
python fetch_mcu_correct.py
```

### Run Phase 2 (Extract character relationships):
```bash
python extract_relationships.py
```

---

## 📈 Key Metrics

- **Movies:** 38 MCU films (2008-2026)
- **Release timespan:** 18 years
- **Characters:** ~80+ unique characters (in progress)
- **Relationships:** ~500+ character pairs (in progress)

---

## 🎬 Motivation

Watched **Spider-Man: Brand New Day** without understanding half the character references?
Overwhelmed by "who connects to who" before **Avengers: Doomsday**?

This project solves that with data.

---

## 🛠️ Tech Stack

- **Python:** Data collection & enrichment
- **TMDB API:** Movie metadata
- **Claude API:** Character relationship extraction
- **Pandas:** Data transformation
- **PostgreSQL:** Data storage (Phase 3)
- **Tableau:** Dashboard visualization (Phase 4)
- **Plotly:** Interactive network graphs

---

## 📅 Timeline

- **Aug 12, 2026:** Phase 1 complete (movie data collected)
- **Aug 13-18, 2026:** Phase 2 (character relationships via LLM)
- **Aug 19-25, 2026:** Phase 3 (SQL modeling)
- **Aug 26-Sept 2, 2026:** Phase 4-5 (analysis + visualization)
- **Sept 5, 2026:** Launch on GitHub + LinkedIn
- **Dec 18, 2026:** Ready for Doomsday release 🚀

---

## 👤 Author

**Sahana Varadharajan**  
Data Analyst | Portfolio Project  
Hamburg, Germany

---

## 📝 License

Personal portfolio project (non-commercial)