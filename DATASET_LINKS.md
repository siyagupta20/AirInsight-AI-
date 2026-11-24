# 📊 AirInsight AI — Dataset & Database Download Links

This repository is kept lightweight (< 5 MB) by excluding heavy raw CSV data files (`> 100 MB`) so that it can be cloned, shared, and run smoothly on any desktop or server.

---

## 🔗 Official Dataset Download Sources

You can download the full historical CPCB ambient air quality monitoring datasets directly from the following official repositories:

### 1. Kaggle — Air Quality Data in India (CPCB 2015–2020)
* **Dataset URL:** [https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)
* **Dataset Author:** Rohan Rao (CPCB Official Records)
* **Included Files:**
  * `city_day.csv` (~2.5 MB) — Daily city-level pollution records
  * `city_hour.csv` (~63 MB) — Hourly city-level pollution records
  * `station_day.csv` (~8.5 MB) — Daily monitoring station records
  * `station_hour.csv` (~210 MB) — Hourly station records (large file)
  * `stations.csv` (~18 KB) — Station metadata, coordinates, and operational status

### 2. Central Pollution Control Board (CPCB) Official Portals
* **CPCB National AQI Portal (CAAQMS Live):** [https://app.cpcbccr.com/AQI_India/](https://app.cpcbccr.com/AQI_India/)
* **CPCB Environmental Data Bank:** [https://cpcb.nic.in/air-quality-data/](https://cpcb.nic.in/air-quality-data/)
* **Open Government Data (OGD) Platform India:** [https://data.gov.in/](https://data.gov.in/)

### 3. Live Weather & Meteorological API
* **Open-Meteo Weather API (Free & Open):** [https://open-meteo.com/](https://open-meteo.com/)
* Real-time temperature, humidity, wind velocity, and atmospheric condition feeds.

---

## 🚀 Running on Any Other Desktop (Zero Configuration Needed)

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/siyagupta20/AirInsight-AI-.git
   cd AirInsight-AI-
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to: `http://127.0.0.1:5000`

> **Note on Datasets:**  
> The application includes a self-healing dataset engine. If `dataset/city_day.csv` is not present, AirInsight AI automatically generates the comprehensive 167-city multi-pollutant environmental time series on the fly.  
> If you wish to use the raw CPCB historical records, simply download `city_day.csv` from the Kaggle link above and place it in the `dataset/` directory.
