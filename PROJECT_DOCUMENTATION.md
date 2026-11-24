# AirInsight AI: Technical Project Documentation & Comprehensive Report

**Course:** INT 396 Unsupervised Machine Learning  
**Project Title:** AI-Based Air Pollution Hotspot & Pattern Discovery System (AirInsight AI)  
**Date:** November 2026  

---

## Executive Abstract

Air pollution in Indian urban centers poses critical environmental, epidemiological, and economic challenges. Traditional monitoring techniques evaluate air quality through linear thresholding indices, which often obscure multi-pollutant correlations, non-linear atmospheric interactions, and localized hotspot formations.

**AirInsight AI** is an advanced environmental intelligence platform that utilizes **Unsupervised Machine Learning** to uncover latent structures in ambient air quality monitoring datasets without human supervision or label bias. By coupling **Agglomerative Hierarchical Clustering**, **Density-Based Spatial Clustering of Applications with Noise (DBSCAN)**, and **Principal Component Analysis (PCA)**, the system automatically detects natural air quality regimes, isolates hazardous outlier episodes, and maps high-risk pollution hotspots across **167 Indian cities** spanning all 35 states and union territories.

The system is further augmented with an interactive vector-rendered India state choropleth map, real-time weather and meteorological synthesis, a multi-city comparison engine, clinical health and safety recommendations, historical seasonality trend analytics, national leaderboards, and automated downloadable executive reports.

---

## 1. Introduction & Motivation

### 1.1 Problem Statement
India is home to several of the world's most polluted urban agglomerations. Severe atmospheric episodes are driven by a complex interplay of:
- Vehicular exhaust emissions ($\text{NO}_2$, $\text{CO}$)
- Industrial effluent combustion ($\text{SO}_2$, $\text{VOCs}$)
- Seasonal agricultural stubble burning and construction dust ($\text{PM}_{2.5}$, $\text{PM}_{10}$)
- Meteorological temperature inversion trapping particulate matter in the lower troposphere during winter months.

Standard air quality assessments rely on single-pollutant maxima to compute a composite Air Quality Index (AQI). However, this fails to capture:
1. Multi-pollutant co-occurrence patterns (e.g., photochemical smog vs. primary combustion).
2. Arbitrarily shaped clusters of environmental behavior.
3. Sudden extreme anomalies versus persistent background pollution.

### 1.2 Project Objectives
1. **Unsupervised Regime Discovery:** Automatically cluster multi-pollutant observations into coherent environmental states using Agglomerative Hierarchical Clustering.
2. **Hotspot & Noise Detection:** Detect dense recurring pollution patterns and isolate extreme outlier events using DBSCAN.
3. **Dimensionality Reduction:** Project high-dimensional chemical spaces (10 pollutants) into 2 principal components using PCA for intuitive visualization.
4. **Validation & Assessment:** Quantitatively validate cluster quality using Silhouette Score, Davies-Bouldin Index, and Calinski-Harabasz Score.
5. **Interactive Decision Support Platform:** Build a full-stack web platform delivering interactive geospatial mapping, live meteorological tracking, city comparisons, and automated PDF-ready reporting.

---

## 2. Dataset Description & Preprocessing Pipeline

### 2.1 Dataset Profile
The project utilizes historical continuous ambient air quality monitoring station (CAAQMS) datasets published by the Central Pollution Control Board (CPCB), enriched with baseline geographical and meteorological observation series, spanning **106,658 daily records** across **167 Indian cities** covering all 35 states and union territories:
- **Spatial Coverage:** 167 urban, industrial, and tier-2/tier-3 hubs across Northern, Southern, Eastern, Western, Central, and North-Eastern India (with at least 5–8 monitored hubs per state, e.g. for Punjab: Amritsar, Ludhiana, Jalandhar, Phagwara, Patiala, Bathinda, Mohali).
- **Pollutant Features ($10$ features):** $\text{PM}_{2.5}$, $\text{PM}_{10}$, $\text{NO}$, $\text{NO}_2$, $\text{NO}_x$, $\text{NH}_3$, $\text{CO}$, $\text{SO}_2$, $\text{O}_3$, $\text{Benzene}$.

### 2.2 Preprocessing Methodology
1. **Cleaning & Missing Value Imputation:**
   Environmental sensor feeds frequently experience missing measurements due to power interruptions, sensor drift, and maintenance outages. A median imputation strategy via `SimpleImputer(strategy="median")` was adopted. Median imputation is robust to extreme winter pollution spikes that would otherwise skew mean estimates.
2. **Infinite and Boundary Value Removal:**
   All non-finite, $\pm\infty$, and unparseable characters are sanitized to `NaN` prior to imputation.
3. **Standardization via Z-Score Scaling:**
   Pollutants exist across vastly different dimensional scales and units:
   - Particulate Matter ($\text{PM}_{2.5}, \text{PM}_{10}$): $10\text{--}800\ \mu\text{g/m}^3$
   - Carbon Monoxide ($\text{CO}$): $0.1\text{--}15\ \text{mg/m}^3$
   - Sulphur Dioxide ($\text{SO}_2$): $2\text{--}150\ \mu\text{g/m}^3$

   Standardization applies the transformation:
   $$z = \frac{x - \mu}{\sigma}$$
   ensuring zero mean and unit variance across all features, preventing high-magnitude particulate metrics from dominating distance calculations.

---

## 3. Unsupervised Machine Learning Framework

### 3.1 Agglomerative Hierarchical Clustering
Agglomerative clustering is a bottom-up hierarchical technique. Each observation starts as its own cluster, and pairs of clusters are iteratively merged to minimize variance.

- **Linkage Criterion:** Ward's Minimum Variance Linkage
  The objective function minimizes the total within-cluster sum of squared differences:
  $$\Delta \text{ESS}_{AB} = \frac{n_A n_B}{n_A + n_B} \|\mathbf{m}_A - \mathbf{m}_B\|^2$$
  where $n_A, n_B$ are cluster sizes and $\mathbf{m}_A, \mathbf{m}_B$ are cluster centroids.
- **Advantage:** Produces balanced, compact clusters corresponding to clean background days, moderate industrial/traffic days, and severe stagnation events.

### 3.2 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
DBSCAN defines clusters as continuous dense regions of points separated by low-density areas.

- **Key Hyperparameters:**
  - $\varepsilon$ (Epsilon): Maximum Euclidean radius defining the neighborhood of a point.
  - $\text{MinPts}$ (Minimum Samples): Minimum points required within the $\varepsilon$-neighborhood to establish a core point.
- **Density Classification:**
  - **Core Point:** $|\mathcal{N}_\varepsilon(p)| \ge \text{MinPts}$
  - **Border Point:** Point within $\varepsilon$ of a core point but possessing $< \text{MinPts}$ neighbors.
  - **Noise / Anomaly:** Point that is neither core nor border ($\text{label} = -1$).
- **Environmental Utility:** Accurately isolates episodic toxic smog emergencies and anomalous industrial leaks as noise without forcing them into regular clusters.

### 3.3 Principal Component Analysis (PCA)
PCA executes orthogonal linear transformation to project correlated multi-pollutant vectors into an uncorrelated low-dimensional subspace:
$$\mathbf{Z} = \mathbf{X} \mathbf{W}$$
where $\mathbf{W}$ contains the eigenvectors corresponding to the two largest eigenvalues of the covariance matrix $\mathbf{\Sigma} = \frac{1}{n} \mathbf{X}^T \mathbf{X}$.
- **PC1:** Primarily captures general particulate and combustion mass loading ($\text{PM}_{2.5}, \text{PM}_{10}, \text{NO}_2$).
- **PC2:** Captures secondary pollutant and photochemical variations ($\text{O}_3, \text{SO}_2$).

---

## 4. Cluster Evaluation Metrics

Since ground-truth labels do not exist in real-world environmental monitoring, unsupervised internal validation metrics are employed:

### 4.1 Silhouette Score
Measures how similar an observation is to its own cluster compared to neighboring clusters:
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$
where $a(i)$ is mean intra-cluster distance, and $b(i)$ is mean nearest-cluster distance.
- Range: $[-1, 1]$. Higher values denote clear separation.

### 4.2 Davies-Bouldin Index
Evaluates the similarity between each cluster and its most similar counterpart:
$$R_{ij} = \frac{s_i + s_j}{d(c_i, c_j)}, \quad DB = \frac{1}{k} \sum_{i=1}^k \max_{j \ne i} R_{ij}$$
where $s_i$ is cluster dispersion and $d(c_i, c_j)$ is centroid distance.
- Lower values denote superior clustering.

### 4.3 Calinski-Harabasz Score (Variance Ratio Criterion)
Ratio of between-cluster variance to within-cluster variance:
$$CH = \frac{\text{Tr}(\mathbf{B}_k)}{\text{Tr}(\mathbf{W}_k)} \times \frac{n - k}{k - 1}$$
- Higher values denote dense, well-separated clusters.

---

## 5. Software Architecture & Implementation

AirInsight AI follows a modular, decoupled architecture:

```
┌────────────────────────────────────────────────────────┐
│                   Web Client (Browser)                 │
│  Interactive Leaflet Map • Plotly.js Visualizations    │
└───────────────────────────▲────────────────────────────┘
                            │ REST JSON / HTTP
┌───────────────────────────▼────────────────────────────┐
│              Flask Application Controller (app.py)     │
│   Routing • Serialization • Error Handling • In-Memory  │
└───────▲───────────────────▲────────────────────▲───────┘
        │                   │                    │
┌───────▼───────────┐ ┌─────▼──────────┐ ┌───────▼──────────┐
│  models/          │ │  services/     │ │  dataset/        │
│  - dbscan_model   │ │  - data_service│ │  - city_day.csv  │
│  - hierarchical   │ │  - weather_serv│ │  - city_hour.csv │
│  - preprocessing  │ │  - advisory_ser│ │  - stations.csv  │
│  - evaluation     │ │                │ │                  │
└───────────────────┘ └────────────────┘ └──────────────────┘
```

---

## 6. System Modules & Features

1. **Interactive India State Choropleth Map (`/map`):**
   - Clean vector rendering on a pure white background (`#ffffff`) without raster tiles, eliminating third-party API key watermarks.
   - States shaded by mean PM2.5 and AQI values matching WHO guidelines and India NAAQS standards.
   - 167 station markers with instant tooltips.
   - Interactive State & City Inspection: Clicking a state shows statewide averages and displays interactive selection chips for all monitored cities in that state (at least 5–8 cities per state).
2. **Live Weather & Air Quality Service (`/api/live/<city>`):**
   - Retrieves real-time temperature, humidity, wind speed, and weather condition from Open-Meteo APIs.
   - Graceful offline fallback using station readings and localized diurnal/climate models.
3. **Multi-City Comparison Engine (`/compare`):**
   - Side-by-side grouped bar charts and 6-axis radar charts.
   - Normalized pollution scores and automated AI summary narrative.
4. **Clinical Health & Safety Recommendations (`/api/advisory/<city>`):**
   - Tailored advice across 6 AQI buckets for general public, sensitive groups, outdoor workouts, masks (N95/N99), and indoor air purifiers.
5. **Historical Pollution Trends (`/insights`):**
   - Monthly seasonal curve demonstrating the winter temperature inversion spike versus monsoon cleansing.
   - Multi-year progression (2015–2020) and 7-day/30-day moving averages.
6. **National Leaderboards (`/rankings`):**
   - Cleanest and Most Polluted podiums.
   - Regional pollution disparity analysis (North vs South vs East vs West).
   - Full master leaderboard spanning all 167 cities with live filter and column sorting.
7. **Downloadable & Printable Reports (`/report/<city>`):**
   - Full executive summary, health advisory, pollutant tables, and seasonality graphs.
   - One-click print/save as clean PDF (`@media print`), plus raw CSV and JSON export.
8. **AI Pollution Discovery (`/discovery`):**
   - Interactive Hierarchical Clustering and DBSCAN execution on any of the 167 cities.
   - 2D PCA cluster projection, cluster distribution, feature summaries, and mathematical validation metrics (Silhouette, Davies-Bouldin, Calinski-Harabasz).

---

## 7. Experimental Findings & Discussion

1. **Seasonal Winter Inversion:**
   In Northern cities (Delhi, Lucknow, Patna), winter months (November to January) exhibit AQI values 3 to 4 times higher than monsoon months (July to September). Cold air traps ground-level emissions, compounded by post-harvest residue burning.
2. **Geographical Disparity:**
   Southern coastal cities (Bengaluru, Chennai, Thiruvananthapuram) maintain significantly cleaner air profiles (mean AQI 73–92), aided by maritime breezes and absence of severe winter temperature inversions.
3. **Clustering Insights:**
   - **DBSCAN:** Core clusters identify normal baseline emissions, while extreme post-Diwali or stubble-burning episodes are correctly categorized as noise outliers rather than skewing baseline cluster profiles.
   - **Hierarchical Clustering:** 3 to 4 clusters cleanly partition the data into:
     - Cluster 0: Clear / Post-monsoon clean days ($\text{PM}_{2.5} < 35$)
     - Cluster 1: Moderate urban traffic days ($\text{PM}_{2.5} \approx 60\text{--}90$)
     - Cluster 2: Heavy winter inversion episodes ($\text{PM}_{2.5} > 180$)

---

## 8. Conclusion

**AirInsight AI** provides a complete, robust, and intuitive unsupervised machine learning system for air pollution analysis in India. By integrating Agglomerative Clustering, DBSCAN, PCA, and rigorous mathematical evaluation with real-time weather, interactive geospatial visualization, multi-city comparisons, and automated reporting, the platform bridges the gap between machine learning research and actionable environmental decision-making.
