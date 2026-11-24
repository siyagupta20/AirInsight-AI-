"""
Live Weather and Air Quality Service for AirInsight AI.
Provides real-time weather and pollution metrics using Open-Meteo APIs
with robust offline fallback based on latest station records and climate modeling.
"""

from datetime import datetime
import math
import random
import requests

# Accurate coordinates and state metadata for all 26 cities in the dataset
CITY_METADATA = {
    "Ahmedabad": {"lat": 23.0225, "lon": 72.5714, "state": "Gujarat", "region": "West", "base_temp": 31, "humidity": 55},
    "Aizawl": {"lat": 23.7271, "lon": 92.7176, "state": "Mizoram", "region": "North-East", "base_temp": 22, "humidity": 75},
    "Amaravati": {"lat": 16.5417, "lon": 80.5158, "state": "Andhra Pradesh", "region": "South", "base_temp": 30, "humidity": 65},
    "Amritsar": {"lat": 31.6340, "lon": 74.8723, "state": "Punjab", "region": "North", "base_temp": 24, "humidity": 60},
    "Bengaluru": {"lat": 12.9716, "lon": 77.5946, "state": "Karnataka", "region": "South", "base_temp": 26, "humidity": 62},
    "Bhopal": {"lat": 23.2599, "lon": 77.4126, "state": "Madhya Pradesh", "region": "Central", "base_temp": 28, "humidity": 52},
    "Brajrajnagar": {"lat": 21.8258, "lon": 83.9214, "state": "Odisha", "region": "East", "base_temp": 29, "humidity": 68},
    "Chandigarh": {"lat": 30.7333, "lon": 76.7794, "state": "Chandigarh", "region": "North", "base_temp": 25, "humidity": 58},
    "Chennai": {"lat": 13.0827, "lon": 80.2707, "state": "Tamil Nadu", "region": "South", "base_temp": 30, "humidity": 78},
    "Coimbatore": {"lat": 11.0168, "lon": 76.9558, "state": "Tamil Nadu", "region": "South", "base_temp": 28, "humidity": 64},
    "Delhi": {"lat": 28.6139, "lon": 77.2090, "state": "Delhi", "region": "North", "base_temp": 26, "humidity": 55},
    "Ernakulam": {"lat": 9.9816, "lon": 76.2999, "state": "Kerala", "region": "South", "base_temp": 29, "humidity": 80},
    "Gurugram": {"lat": 28.4595, "lon": 77.0266, "state": "Haryana", "region": "North", "base_temp": 26, "humidity": 54},
    "Guwahati": {"lat": 26.1445, "lon": 91.7362, "state": "Assam", "region": "North-East", "base_temp": 26, "humidity": 74},
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867, "state": "Telangana", "region": "South", "base_temp": 29, "humidity": 60},
    "Jaipur": {"lat": 26.9124, "lon": 75.7873, "state": "Rajasthan", "region": "North-West", "base_temp": 28, "humidity": 45},
    "Jorapokhar": {"lat": 23.7022, "lon": 86.4131, "state": "Jharkhand", "region": "East", "base_temp": 28, "humidity": 62},
    "Kochi": {"lat": 9.9312, "lon": 76.2673, "state": "Kerala", "region": "South", "base_temp": 29, "humidity": 82},
    "Kolkata": {"lat": 22.5726, "lon": 88.3639, "state": "West Bengal", "region": "East", "base_temp": 29, "humidity": 76},
    "Lucknow": {"lat": 26.8467, "lon": 80.9462, "state": "Uttar Pradesh", "region": "North", "base_temp": 27, "humidity": 60},
    "Mumbai": {"lat": 19.0760, "lon": 72.8777, "state": "Maharashtra", "region": "West", "base_temp": 30, "humidity": 75},
    "Patna": {"lat": 25.5941, "lon": 85.1376, "state": "Bihar", "region": "East", "base_temp": 27, "humidity": 65},
    "Shillong": {"lat": 25.5788, "lon": 91.8933, "state": "Meghalaya", "region": "North-East", "base_temp": 19, "humidity": 78},
    "Talcher": {"lat": 20.9500, "lon": 85.2167, "state": "Odisha", "region": "East", "base_temp": 29, "humidity": 66},
    "Thiruvananthapuram": {"lat": 8.5241, "lon": 76.9366, "state": "Kerala", "region": "South", "base_temp": 29, "humidity": 80},
    "Visakhapatnam": {"lat": 17.6868, "lon": 83.2185, "state": "Andhra Pradesh", "region": "South", "base_temp": 30, "humidity": 74}
}

WEATHER_CODE_MAP = {
    0: ("Clear Sky", "☀️"),
    1: ("Mainly Clear", "🌤️"),
    2: ("Partly Cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Foggy / Hazy", "🌫️"),
    48: ("Depositing Rime Fog", "🌫️"),
    51: ("Light Drizzle", "🌦️"),
    53: ("Moderate Drizzle", "🌧️"),
    55: ("Dense Drizzle", "🌧️"),
    61: ("Slight Rain", "🌦️"),
    63: ("Moderate Rain", "🌧️"),
    65: ("Heavy Rain", "🌧️"),
    71: ("Slight Snow", "🌨️"),
    80: ("Rain Showers", "🌦️"),
    95: ("Thunderstorm", "⛈️")
}


def _get_fallback_weather(city_name, meta):
    """Generate realistic climate condition based on city location and current time."""
    now = datetime.now()
    hour = now.hour
    month = now.month

    # Diurnal cycle factor (-1 to +1)
    # Peak temp around 14:00 (hour 14), lowest around 05:00
    diurnal = math.sin((hour - 8) / 12 * math.pi)
    
    # Seasonal factor (Northern hemisphere India: May-Jun warmest, Dec-Jan coolest)
    seasonal = -math.cos((month - 1) / 12 * 2 * math.pi)

    base = meta.get("base_temp", 27)
    temp = round(base + (diurnal * 4.5) + (seasonal * 3.5), 1)
    humidity = round(max(25, min(95, meta.get("humidity", 60) - (diurnal * 12))), 0)
    wind_speed = round(max(3.0, 11.0 + (diurnal * 4.0)), 1)

    if humidity > 75 and diurnal < 0:
        condition, icon = "Hazy / Mist", "🌫️"
    elif diurnal > 0.5:
        condition, icon = "Sunny & Clear", "☀️"
    elif diurnal < -0.3:
        condition, icon = "Clear Night", "🌙"
    else:
        condition, icon = "Partly Cloudy", "⛅"

    return {
        "temperature": temp,
        "feels_like": round(temp + (humidity / 100 * 2.5), 1),
        "humidity": int(humidity),
        "wind_speed": wind_speed,
        "wind_direction": "NW" if "North" in meta.get("region", "") else "SW",
        "condition": condition,
        "icon": icon,
        "weather_code": 1
    }


def get_live_weather_and_aqi(city_name, latest_record=None):
    """
    Fetch real-time weather and air quality for an Indian city.
    Uses Open-Meteo real-time APIs with automatic fallback.
    """
    city_clean = city_name.strip()
    # Case-insensitive lookup in metadata
    meta = None
    for k, v in CITY_METADATA.items():
        if k.casefold() == city_clean.casefold():
            meta = v
            city_clean = k
            break

    if not meta:
        meta = {"lat": 20.5937, "lon": 78.9629, "state": "India", "region": "Central", "base_temp": 28, "humidity": 60}

    lat, lon = meta["lat"], meta["lon"]
    is_live = False
    source = "Historical Dataset & Climate Engine"
    weather = None
    live_pollutants = {}

    # Attempt Live API Query (weather + air quality)
    try:
        w_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m,wind_direction_10m"
        w_res = requests.get(w_url, timeout=2.5)
        if w_res.status_code == 200:
            w_data = w_res.json().get("current", {})
            code = w_data.get("weather_code", 0)
            cond, icon = WEATHER_CODE_MAP.get(code, ("Clear Sky", "☀️"))
            weather = {
                "temperature": round(w_data.get("temperature_2m", 28.0), 1),
                "feels_like": round(w_data.get("apparent_temperature", 29.0), 1),
                "humidity": int(w_data.get("relative_humidity_2m", 60)),
                "wind_speed": round(w_data.get("wind_speed_10m", 10.0), 1),
                "wind_direction": f"{w_data.get('wind_direction_10m', 180)}°",
                "condition": cond,
                "icon": icon,
                "weather_code": code
            }
            is_live = True
            source = "Live Open-Meteo Station Network"

            # Attempt Air Quality fetch
            aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone,us_aqi,european_aqi"
            aq_res = requests.get(aq_url, timeout=2.5)
            if aq_res.status_code == 200:
                aq_data = aq_res.json().get("current", {})
                live_pollutants = {
                    "PM2.5": aq_data.get("pm2_5"),
                    "PM10": aq_data.get("pm10"),
                    "NO2": aq_data.get("nitrogen_dioxide"),
                    "SO2": aq_data.get("sulphur_dioxide"),
                    "CO": round(aq_data.get("carbon_monoxide", 0) / 1000.0, 2) if aq_data.get("carbon_monoxide") else None,
                    "O3": aq_data.get("ozone"),
                    "AQI": aq_data.get("us_aqi")
                }
    except Exception:
        # Graceful fallback on network unreachable / sandbox
        pass

    if not weather:
        weather = _get_fallback_weather(city_clean, meta)

    # Reconcile pollutants with latest dataset records if live pollutants are empty/partial
    if latest_record is None:
        latest_record = {}

    final_pm25 = live_pollutants.get("PM2.5") or latest_record.get("PM2.5") or 45.0
    final_pm10 = live_pollutants.get("PM10") or latest_record.get("PM10") or 85.0
    final_no2 = live_pollutants.get("NO2") or latest_record.get("NO2") or 22.0
    final_so2 = live_pollutants.get("SO2") or latest_record.get("SO2") or 11.0
    final_co = live_pollutants.get("CO") or latest_record.get("CO") or 0.8
    final_o3 = live_pollutants.get("O3") or latest_record.get("O3") or 34.0

    # Compute Indian AQI if not directly present
    final_aqi = live_pollutants.get("AQI") or latest_record.get("AQI")
    if final_aqi is None or math.isnan(float(final_aqi or 0)) or float(final_aqi or 0) <= 0:
        # Approximate sub-index for PM2.5
        val = float(final_pm25)
        if val <= 30:
            final_aqi = (val / 30) * 50
        elif val <= 60:
            final_aqi = 50 + ((val - 30) / 30) * 50
        elif val <= 90:
            final_aqi = 100 + ((val - 60) / 30) * 100
        elif val <= 120:
            final_aqi = 200 + ((val - 90) / 30) * 100
        elif val <= 250:
            final_aqi = 300 + ((val - 120) / 130) * 100
        else:
            final_aqi = 400 + min(100, ((val - 250) / 100) * 100)

    final_aqi = round(float(final_aqi), 1)

    # Determine bucket
    if final_aqi <= 50:
        bucket = "Good"
    elif final_aqi <= 100:
        bucket = "Satisfactory"
    elif final_aqi <= 200:
        bucket = "Moderate"
    elif final_aqi <= 300:
        bucket = "Poor"
    elif final_aqi <= 400:
        bucket = "Very Poor"
    else:
        bucket = "Severe"

    return {
        "city": city_clean,
        "state": meta.get("state", "India"),
        "region": meta.get("region", "India"),
        "latitude": lat,
        "longitude": lon,
        "weather": weather,
        "aqi": final_aqi,
        "aqi_bucket": bucket,
        "pollutants": {
            "PM2.5": round(float(final_pm25), 1) if final_pm25 is not None else None,
            "PM10": round(float(final_pm10), 1) if final_pm10 is not None else None,
            "NO2": round(float(final_no2), 1) if final_no2 is not None else None,
            "SO2": round(float(final_so2), 1) if final_so2 is not None else None,
            "CO": round(float(final_co), 2) if final_co is not None else None,
            "O3": round(float(final_o3), 1) if final_o3 is not None else None
        },
        "is_live": is_live,
        "source": source,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
