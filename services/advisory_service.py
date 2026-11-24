"""
Advisory Service for AirInsight AI.
Provides actionable health, safety, outdoor activity, mask, and lifestyle
recommendations based on National Air Quality Index (AQI) categories and pollutant thresholds.
"""

AQI_CATEGORIES = [
    {
        "min": 0,
        "max": 50,
        "bucket": "Good",
        "color": "#10b981",
        "badge_bg": "#d1fae5",
        "badge_text": "#065f46",
        "risk_level": "Minimal",
        "summary": "Air quality is satisfactory and poses little or no health risk.",
        "general_public": (
            "Enjoy outdoor activities freely. Keep rooms well-ventilated to let in fresh air."
        ),
        "sensitive_groups": (
            "No special precautions needed. Ideal conditions for outdoor walks and exercise."
        ),
        "outdoor_exercise": "Safe for all high-intensity outdoor exercises, sports, and running.",
        "mask_recommendation": "No mask required for general outdoor exposure.",
        "air_purifier": "No air purifier needed. Natural cross-ventilation is recommended.",
        "lifestyle_tips": [
            "Take advantage of clean air for outdoor fitness and cardiovascular activities.",
            "Open windows in the morning and evening to ventilate indoor living spaces.",
            "Maintain indoor green plants (Snake Plant, Spider Plant, Areca Palm) to keep indoor air fresh."
        ]
    },
    {
        "min": 51,
        "max": 100,
        "bucket": "Satisfactory",
        "color": "#22c55e",
        "badge_bg": "#dcfce7",
        "badge_text": "#166534",
        "risk_level": "Low",
        "summary": "Air quality is acceptable; minor breathing discomfort possible for sensitive individuals.",
        "general_public": (
            "Air quality is generally acceptable. Most people can continue normal outdoor activities."
        ),
        "sensitive_groups": (
            "Unusually sensitive individuals with severe asthma or COPD should monitor for mild symptoms."
        ),
        "outdoor_exercise": "Generally safe for outdoor workouts. Take breaks if fatigue or throat dryness occurs.",
        "mask_recommendation": "Not strictly necessary; sensitive individuals near traffic junctions may prefer a light mask.",
        "air_purifier": "Optional; recommended primarily for bedrooms of individuals with dust or pollen allergies.",
        "lifestyle_tips": [
            "Stay well-hydrated throughout the day to support mucosal respiratory barriers.",
            "Keep vehicles properly serviced to minimize localized tailpipe emissions.",
            "Prefer morning exercise before peak urban vehicular traffic builds up."
        ]
    },
    {
        "min": 101,
        "max": 200,
        "bucket": "Moderate",
        "color": "#eab308",
        "badge_bg": "#fef9c3",
        "badge_text": "#854d0e",
        "risk_level": "Moderate",
        "summary": "Breathing discomfort possible for people with lung/heart disease, elderly, and children.",
        "general_public": (
            "Healthy adults may experience mild throat irritation during strenuous outdoor activity."
        ),
        "sensitive_groups": (
            "People with asthma, cardiovascular disorders, elderly individuals, and young children should limit prolonged outdoor exertion."
        ),
        "outdoor_exercise": "Reduce prolonged heavy exertion outdoors. Consider indoor cardiovascular training or yoga.",
        "mask_recommendation": "Recommended for sensitive groups when commuting in heavy traffic; surgical or cloth mask offers basic dust protection.",
        "air_purifier": "Beneficial in bedrooms during nighttime hours. Keep windows closed during peak traffic hours.",
        "lifestyle_tips": [
            "Incorporate antioxidant-rich foods (vitamin C, citrus fruits, amla) into daily meals.",
            "Rinse face, eyes, and nasal passages with clean water after returning from outdoors.",
            "Avoid burning garden waste, incense sticks, or tobacco indoors."
        ]
    },
    {
        "min": 201,
        "max": 300,
        "bucket": "Poor",
        "color": "#f97316",
        "badge_bg": "#ffedd5",
        "badge_text": "#9a3412",
        "risk_level": "High",
        "summary": "Breathing discomfort to most people on prolonged exposure; severe impact on sensitive groups.",
        "general_public": (
            "Noticeable smog and haze. Avoid prolonged outdoor exertion. Healthy individuals may experience cough and throat irritation."
        ),
        "sensitive_groups": (
            "Children, seniors, and patients with asthma, bronchitis, or heart disease should remain indoors and keep inhalers accessible."
        ),
        "outdoor_exercise": "Avoid outdoor running, cycling, or intense sports. Shift entirely to indoor workouts.",
        "mask_recommendation": "N95 or N99 certified respirators strongly advised for anyone spending more than 30 minutes outside.",
        "air_purifier": "Run HEPA air purifiers indoors. Keep doors and windows tightly shut.",
        "lifestyle_tips": [
            "Drink warm herbal infusions (ginger, tulsi, turmeric tea) to soothe respiratory tracts.",
            "Use wet mopping rather than dry sweeping to prevent re-suspending settled particulate matter.",
            "Consider steam inhalation in the evening to clear nasal and throat passages."
        ]
    },
    {
        "min": 301,
        "max": 400,
        "bucket": "Very Poor",
        "color": "#ef4444",
        "badge_bg": "#fee2e2",
        "badge_text": "#991b1b",
        "risk_level": "Very High",
        "summary": "Respiratory illness on prolonged exposure. Significant health warning for the entire population.",
        "general_public": (
            "Everyone may experience adverse health effects. Keep outdoor exposure to the bare minimum necessary."
        ),
        "sensitive_groups": (
            "Strictly avoid all outdoor activity. High risk of asthma triggers, bronchitis flare-ups, and cardiovascular stress."
        ),
        "outdoor_exercise": "Strictly prohibited. All workouts must be done indoors in filtered air environments.",
        "mask_recommendation": "N95/N99 respirator with airtight fit is mandatory for anyone stepping outdoors.",
        "air_purifier": "Continuous HEPA air filtration is essential. Seal window and door gaps with weatherstripping.",
        "lifestyle_tips": [
            "Keep emergency rescue inhalers and prescribed allergy/heart medications close at hand.",
            "Avoid frying or high-heat cooking without active exhaust ventilation.",
            "Install indoor air-purifying plants such as Snake Plant, Peace Lily, and Boston Fern."
        ]
    },
    {
        "min": 401,
        "max": 10000,
        "bucket": "Severe",
        "color": "#7f1d1d",
        "badge_bg": "#ffe4e6",
        "badge_text": "#881337",
        "risk_level": "Emergency / Hazardous",
        "summary": "Public health emergency. Healthy individuals experience severe symptoms; acute danger to sensitive groups.",
        "general_public": (
            "Public health emergency conditions. Stay indoors with doors and windows sealed. Minimize physical exertion."
        ),
        "sensitive_groups": (
            "Critical hazard. Complete confinement to clean, filtered indoor air. Seek prompt medical care if wheezing or chest tightness occurs."
        ),
        "outdoor_exercise": "Completely prohibited. Any outdoor physical activity presents acute toxic exposure.",
        "mask_recommendation": "Medical-grade N95/N99 respirator with silicone seal is required even for brief essential outdoor trips.",
        "air_purifier": "Run high-grade HEPA purifiers on maximum settings 24/7. Create a dedicated 'clean room' if whole-house filtration is unavailable.",
        "lifestyle_tips": [
            "Schools and outdoor work should transition to remote/indoor modalities where possible.",
            "Stay strictly hydrated and maintain a nutrient-dense diet rich in omega-3 and antioxidants.",
            "Monitor oxygen saturation (SpO2) for family members with chronic respiratory illnesses."
        ]
    }
]


def get_health_advisory(aqi, pm25=None, pm10=None, city=None):
    """
    Generate comprehensive health and safety recommendations
    for a given AQI value and optional pollutant readings.
    """
    if aqi is None or (isinstance(aqi, float) and not (aqi == aqi)):
        aqi = 100  # Default moderate if not specified

    try:
        aqi_val = float(aqi)
    except (TypeError, ValueError):
        aqi_val = 100.0

    matched = None
    for category in AQI_CATEGORIES:
        if category["min"] <= aqi_val <= category["max"]:
            matched = category
            break

    if not matched:
        matched = AQI_CATEGORIES[-1]

    # Specific pollutant alerts
    pollutant_alerts = []
    if pm25 is not None:
        try:
            val = float(pm25)
            if val > 120:
                pollutant_alerts.append(
                    f"PM2.5 is critically high ({val:.1f} µg/m³). Fine particles penetrate deep into lung alveoli and bloodstream."
                )
            elif val > 60:
                pollutant_alerts.append(
                    f"PM2.5 is elevated ({val:.1f} µg/m³), above WHO 24-hr guideline of 15 µg/m³."
                )
        except (TypeError, ValueError):
            pass

    if pm10 is not None:
        try:
            val = float(pm10)
            if val > 200:
                pollutant_alerts.append(
                    f"PM10 is extremely high ({val:.1f} µg/m³), causing upper airway and conjunctival irritation."
                )
        except (TypeError, ValueError):
            pass

    return {
        "city": city,
        "aqi": round(aqi_val, 1),
        "bucket": matched["bucket"],
        "color": matched["color"],
        "badge_bg": matched["badge_bg"],
        "badge_text": matched["badge_text"],
        "risk_level": matched["risk_level"],
        "summary": matched["summary"],
        "general_public": matched["general_public"],
        "sensitive_groups": matched["sensitive_groups"],
        "outdoor_exercise": matched["outdoor_exercise"],
        "mask_recommendation": matched["mask_recommendation"],
        "air_purifier": matched["air_purifier"],
        "lifestyle_tips": matched["lifestyle_tips"],
        "pollutant_alerts": pollutant_alerts
    }
