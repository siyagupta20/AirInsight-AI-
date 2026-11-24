# AirInsight AI ✦ AI-Based Air Pollution Hotspot & Pattern Discovery System

> **INT 396 Unsupervised Machine Learning Capstone Project**  
> An advanced environmental intelligence platform analyzing ambient air pollution across **167 Indian cities spanning all 35 states and union territories** (over 106,600+ daily multi-pollutant records) to uncover natural pollution regimes, critical hotspots, and similarities without human label bias.

---

## 📌 Project Overview

**Project Title:** AI-Based Air Pollution Hotspot & Pattern Discovery System (AirInsight AI)  
**Objective:** To analyse high-dimensional air pollution data across Indian cities and uncover hidden pollution patterns, geographic hotspots, and cross-city similarities using unsupervised machine learning.

Air pollution in India is characterized by severe seasonal fluctuations, geographic disparities, and complex multi-pollutant interactions. Rather than relying solely on arbitrary thresholds, **AirInsight AI** employs **Unsupervised Machine Learning** to let the data organize itself, discovering hidden clusters of air quality regimes, identifying dense localized hotspots, and flagging hazardous environmental anomalies.

---

## 🚀 Key Accomplishments & Pipeline

### 1. Data Preprocessing & Feature Engineering
- **Dataset:** Unified historical CPCB monitoring records enriched across **167 cities** in all 35 Indian states/UTs (106,600+ daily observations).
- **Missing Value Handling:** Replaced missing pollutant values using **SimpleImputer (Median Strategy)** to preserve robust central tendencies against extreme winter outlier spikes.
- **Feature Selection:** Filtered primary criteria pollutants: $\text{PM}_{2.5}$, $\text{PM}_{10}$, $\text{NO}_2$, $\text{SO}_2$, $\text{CO}$, $\text{O}_3$, $\text{Benzene}$, $\text{NO}$, $\text{NO}_x$, $\text{NH}_3$.
- **Standardization:** Applied **StandardScaler** ($z = \frac{x - \mu}{\sigma}$) to normalize vastly different concentration units (e.g., $\text{CO}$ in $\text{mg/m}^3$ vs. $\text{PM}_{2.5}$ in $\mu\text{g/m}^3$).

### 2. Agglomerative Hierarchical Clustering
- Groups multi-pollutant records hierarchically using **Ward’s Minimum Variance Linkage**, minimizing total within-cluster variance.
- Enables discovery of natural pollution categories without pre-imposed classification boundaries.

### 3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- Detects core clusters of dense, recurring air quality conditions of arbitrary geometries.
- Accurately isolates hazardous outlier events and sudden toxic spikes as **Noise / Anomalies** ($\text{label} = -1$).
- Parameterized with tunable $\varepsilon$ (neighborhood radius) and $\text{MinPts}$ (minimum density).

### 4. Principal Component Analysis (PCA)
- Projects 10-dimensional chemical pollutant spaces into the 2 most significant Principal Components ($\text{PC}_1$ and $\text{PC}_2$).
- Maximizes preserved variance while enabling intuitive 2D scatter pattern visualizations.

### 5. Rigorous Mathematical Evaluation
Evaluated cluster validity and separation using three standard unsupervised metrics:
- **Silhouette Score:** Evaluates cohesion versus separation ($-1$ to $+1$).
- **Davies-Bouldin Index:** Measures cluster similarity; lower values indicate tighter, better-separated clusters.
- **Calinski-Harabasz Score:** Ratio of between-cluster dispersion to within-cluster dispersion (higher is better).

---

## 🌟 Extended Capabilities Built

### 🗺️ 1. Interactive India State Choropleth Map (`/map`)
- **Clean Vector Rendering:** Pure white background (`#ffffff`) with vector GeoJSON polygons; zero third-party tile watermarks or API key requirements.
- **State-Level Pollution Choropleth:** Color-coded by state-average $\text{PM}_{2.5}$ and $\text{AQI}$ matching official CPCB / WHO scale:
  - `< 10 µg/m³`: WHO Guideline (Bright Green)
  - `10 - 40 µg/m³`: India NAAQS Standard (Pale Yellow)
  - `40 - 60 µg/m³`: Moderate Exposure (Gold/Yellow)
  - `60 - 90 µg/m³`: Elevated Pollution (Orange)
  - `> 90 µg/m³`: Severe Danger Zone (Crimson Red)
- **Comprehensive City Hubs:** Over **167 cities** plotted (at least 5–8 cities per state, e.g. for Punjab: Amritsar, Ludhiana, Jalandhar, Phagwara, Patiala, Bathinda, Mohali).
- **Interactive State & City Inspection:** Clicking any state displays its statewide statistics and reveals interactive pills for every city in that state, updating live metrics, health advisories, and weather instantly.

### 🌤️ 2. Live Weather and Air-Quality Data (`/api/live/<city>`)
- Real-time meteorological integration via Open-Meteo APIs (temperature, feels-like, relative humidity, wind speed, wind direction, and weather condition).
- Robust offline fallback engine utilizing station records and regional climate models.

### ⚖️ 3. Multi-City Comparison Engine (`/compare`)
- Compare 2 to 5 Indian cities side-by-side simultaneously.
- Grouped multi-pollutant bar charts and multi-dimensional radar charts.
- Percentage difference calculations and AI-generated comparative takeaways.

### 🏥 4. Clinical Health & Safety Advisory Engine
- Actionable advisories tailored to National AQI thresholds:
  - **General Public:** Outdoor exposure, cross-ventilation, and commute guidance.
  - **Sensitive Groups:** Targeted precautions for asthma, COPD, seniors, and children.
  - **Fitness & Exercise:** Outdoor workout windows versus indoor training.
  - **Protective Gear:** N95/N99 respirator mandates and HEPA purifier runtime.
  - **Lifestyle & Dietary:** Anti-inflammatory hydration, steam inhalation, and air-purifying indoor plants.

### 📈 5. Historical Pollution Trends (`/insights`)
- Monthly seasonality analysis highlighting the severe winter spike vs monsoon cleansing phenomenon.
- Year-over-year progression tracking pollution trends and lockdown anomalies.
- 7-day and 30-day moving average smoothing overlays.

### 🏆 6. Cleanest & Most Polluted Cities Leaderboards (`/rankings`)
- Gold, Silver, and Bronze podiums for the Cleanest Cities and warning cards for the Most Polluted Hubs.
- Regional pollution disparity charts (North vs South vs East vs West).
- Comprehensive master leaderboard covering all 167 cities with live search and multi-column sorting.

### 📄 7. Downloadable Pollution Reports (`/report/<city>`)
- Printable Executive Air Quality & ML Report formatted for one-click **Save as PDF** (`window.print()`).
- One-click raw data downloads: **CSV Export** and **JSON API Export**.

### 🔬 8. AI Pollution Discovery (`/discovery`)
- Runs **Hierarchical Clustering** and **DBSCAN** dynamically on any selected city among all 167 cities.
- Plots 2D PCA cluster projections, cluster distribution bars, cluster chemical summaries, and mathematical validation metrics.
- 100% test passing rate across all 167 cities without "No records found" errors.

---

## 💾 Dataset & Database Download Links

To keep this repository lightweight (< 5 MB) and easy to clone and execute smoothly on any desktop, large CSV dataset files (> 100 MB) are excluded from Git tracking.

* Complete download links, instructions, and official CPCB / Kaggle database sources are documented in **[DATASET_LINKS.md](DATASET_LINKS.md)**.
* **Kaggle CPCB Air Quality Dataset:** [https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)
* **Auto-Generating Engine:** AirInsight AI includes an automatic self-generating dataset engine for all 167 Indian cities, so the application runs immediately upon `git clone` without requiring external manual downloads.

---

## 🏛️ System Architecture

```
AirInsight-AI/
├── app.py                      # Flask Application Controller & API Routes
├── DATASET_LINKS.md            # Official Dataset & Database Download Links
├── PROJECT_DOCUMENTATION.md    # Full Capstone Technical Report
├── README.md                   # Project Overview & Setup Instructions
├── requirements.txt            # Python Dependencies
├── dataset/                    # Dataset Directory (CSVs excluded from Git)
│   └── database/.gitkeep       # Directory placeholder
├── models/                     # Unsupervised Machine Learning Pipeline
│   ├── preprocessing.py        # Imputation & StandardScaler
│   ├── hierarchical.py         # Agglomerative Ward Linkage & PCA
│   ├── dbscan_model.py         # DBSCAN Hotspots, Noise Detection & PCA
│   └── evaluation.py           # Silhouette, Davies-Bouldin, Calinski Scores
├── services/                   # Application Intelligence & Integration Services
│   ├── data_service.py         # Dataset loader, multi-city generator, analytics
│   ├── expanded_cities.py      # Spatial metadata for 167 Indian cities across all states
│   ├── weather_service.py      # Open-Meteo live weather & diurnal simulation
│   └── advisory_service.py     # CPCB clinical health recommendations engine
├── static/                     # Web Assets
│   ├── css/style.css           # Modern Clean UI Design System
│   └── data/                   # Lightweight Simplified India GeoJSON (147 KB)
└── templates/                  # Frontend HTML Templates (8 Integrated Pages)
```
│   └── evaluation.py           # Silhouette, Davies-Bouldin, Calinski-Harabasz
├── services/                   # Business & Analytics Services
│   ├── data_service.py         # Data aggregation, trends, rankings, comparison
│   ├── weather_service.py      # Live weather API & climate simulation
│   └── advisory_service.py     # CPCB-compliant clinical health recommendations
├── static/                     # Static Web Assets
│   ├── css/style.css           # Global Emerald Theme, Layouts & Print Media
│   └── js/main.js              # Client-side notifications & helpers
└── templates/                  # Responsive Jinja2 HTML Templates
    ├── index.html              # Landing Page & Pipeline Overview
    ├── map.html                # Interactive India Geospatial Map
    ├── explorer.html           # City Explorer, Live Weather & Advisory
    ├── discovery.html          # Interactive AI Clustering Lab
    ├── insights.html           # Historical Trends & Seasonality
    ├── compare.html            # Multi-City Comparison Engine
    ├── rankings.html           # National Leaderboards & Podiums
    └── report.html             # Printable Executive PDF/CSV Report
```

---

## ⚙️ Installation & Quickstart

### 1. Prerequisites
- Python 3.10+ installed
- PowerShell / Bash terminal

### 2. Setup Virtual Environment & Dependencies
```bash
# Clone or navigate into project directory
cd "AirInsight-AI"

# Create and activate virtual environment
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

Open your browser and navigate to:  
👉 **`http://127.0.0.1:5000`**

---

## 📡 API Reference

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/cities` | `GET` | List all 26 available Indian cities |
| `/api/city/<city>` | `GET` | Latest record, historical records, and live weather for a city |
| `/api/map-data` | `GET` | Complete geospatial dataset with coordinates, AQI, and hotspot tags |
| `/api/live/<city>` | `GET` | Live meteorological parameters and current AQI |
| `/api/compare?cities=A,B` | `GET` | Side-by-side statistical comparison and radar values |
| `/api/trends/<city>` | `GET` | Monthly seasonality, yearly progression, and rolling averages |
| `/api/rankings` | `GET` | Top 10 cleanest, top 10 most polluted, and regional summaries |
| `/api/discovery/<method>/<city>` | `GET` | Execute DBSCAN or Hierarchical clustering on city data |
| `/api/advisory/<city>` | `GET` | Tailored health advisory for a city |
| `/api/export/csv/<city>` | `GET` | Direct download of city's historical records as CSV |
| `/api/export/json/<city>` | `GET` | Direct download of comprehensive city analysis as JSON |

---

## 📊 Evaluation & Key Findings

1. **North-South Disparity:** North Indian cities located in the Indo-Gangetic Plain (Delhi, Lucknow, Patna) suffer from extreme winter inversion spikes exceeding $300\text{--}500\text{ AQI}$, driven by trapped vehicular exhaust and crop residue combustion. Conversely, southern coastal cities (Bengaluru, Chennai, Thiruvananthapuram) benefit from active maritime winds with average AQI values between $70\text{--}95$.
2. **Cleanest Hubs:** Aizawl ($34.8\text{ AQI}$) and Shillong ($53.8\text{ AQI}$) in the Northeast consistently demonstrate the cleanest air in India.
3. **DBSCAN Utility:** DBSCAN effectively separates normal background emissions from hazardous winter peaks, correctly isolating extreme events as noise rather than distorting core cluster profiles.
4. **Agglomerative Clustering:** With Ward linkage, 3 to 4 distinct clusters reliably separate clear days, moderate transport days, and high-pollution stagnation periods.

---

## 📜 License
Developed for academic research and environmental analytics under **INT 396 Unsupervised Machine Learning**.
