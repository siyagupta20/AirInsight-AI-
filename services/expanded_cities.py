"""
Comprehensive Expanded Cities Database for AirInsight AI.
Provides at least 5 to 8 major monitoring hubs and industrial centers for each Indian state,
with precise coordinates, state affiliation, and environmental profiles.
"""

EXPANDED_CITIES = {
    # ------------------ PUNJAB (7 cities) ------------------
    "Amritsar": {"lat": 31.6340, "lon": 74.8723, "state": "Punjab", "region": "North", "pm25": 55.5, "pm10": 115.2, "no2": 28.0, "so2": 12.0, "co": 1.1, "o3": 34.0, "aqi": 120, "is_core": True},
    "Ludhiana": {"lat": 30.9010, "lon": 75.8573, "state": "Punjab", "region": "North", "pm25": 68.4, "pm10": 138.5, "no2": 36.5, "so2": 15.2, "co": 1.4, "o3": 38.0, "aqi": 145, "is_core": False},
    "Jalandhar": {"lat": 31.3260, "lon": 75.5762, "state": "Punjab", "region": "North", "pm25": 62.1, "pm10": 126.0, "no2": 32.0, "so2": 13.5, "co": 1.25, "o3": 35.0, "aqi": 135, "is_core": False},
    "Phagwara": {"lat": 31.2240, "lon": 75.7708, "state": "Punjab", "region": "North", "pm25": 58.7, "pm10": 120.4, "no2": 29.5, "so2": 12.8, "co": 1.18, "o3": 33.5, "aqi": 128, "is_core": False},
    "Patiala": {"lat": 30.3398, "lon": 76.3869, "state": "Punjab", "region": "North", "pm25": 52.3, "pm10": 108.2, "no2": 26.4, "so2": 11.2, "co": 1.05, "o3": 32.0, "aqi": 115, "is_core": False},
    "Bathinda": {"lat": 30.2110, "lon": 74.9455, "state": "Punjab", "region": "North", "pm25": 64.0, "pm10": 132.0, "no2": 33.2, "so2": 16.0, "co": 1.30, "o3": 36.5, "aqi": 138, "is_core": False},
    "Mohali": {"lat": 30.7046, "lon": 76.7179, "state": "Punjab", "region": "North", "pm25": 48.9, "pm10": 98.5, "no2": 24.1, "so2": 10.4, "co": 0.95, "o3": 30.0, "aqi": 108, "is_core": False},

    # ------------------ HARYANA (7 cities) ------------------
    "Gurugram": {"lat": 28.4595, "lon": 77.0266, "state": "Haryana", "region": "North", "pm25": 117.1, "pm10": 191.5, "no2": 45.2, "so2": 18.4, "co": 1.8, "o3": 44.0, "aqi": 225, "is_core": True},
    "Faridabad": {"lat": 28.4089, "lon": 77.3178, "state": "Haryana", "region": "North", "pm25": 122.5, "pm10": 204.0, "no2": 48.0, "so2": 19.5, "co": 1.9, "o3": 46.0, "aqi": 238, "is_core": False},
    "Panipat": {"lat": 29.3909, "lon": 76.9635, "state": "Haryana", "region": "North", "pm25": 108.0, "pm10": 182.0, "no2": 42.0, "so2": 17.0, "co": 1.6, "o3": 41.0, "aqi": 210, "is_core": False},
    "Ambala": {"lat": 30.3782, "lon": 76.7767, "state": "Haryana", "region": "North", "pm25": 82.0, "pm10": 145.0, "no2": 34.0, "so2": 14.0, "co": 1.3, "o3": 36.0, "aqi": 165, "is_core": False},
    "Rohtak": {"lat": 28.8955, "lon": 76.6066, "state": "Haryana", "region": "North", "pm25": 96.0, "pm10": 168.0, "no2": 38.0, "so2": 15.5, "co": 1.5, "o3": 39.0, "aqi": 192, "is_core": False},
    "Hisar": {"lat": 29.1492, "lon": 75.7217, "state": "Haryana", "region": "North", "pm25": 92.5, "pm10": 160.0, "no2": 36.0, "so2": 14.8, "co": 1.4, "o3": 38.0, "aqi": 185, "is_core": False},
    "Karnal": {"lat": 29.6857, "lon": 76.9905, "state": "Haryana", "region": "North", "pm25": 88.0, "pm10": 152.0, "no2": 35.0, "so2": 14.2, "co": 1.35, "o3": 37.0, "aqi": 178, "is_core": False},

    # ------------------ DELHI (6 stations/districts) ------------------
    "Delhi": {"lat": 28.6139, "lon": 77.2090, "state": "Delhi", "region": "North", "pm25": 117.2, "pm10": 232.8, "no2": 50.6, "so2": 17.8, "co": 1.53, "o3": 42.7, "aqi": 259, "is_core": True},
    "Anand Vihar": {"lat": 28.6469, "lon": 77.3160, "state": "Delhi", "region": "North", "pm25": 142.0, "pm10": 285.0, "no2": 62.0, "so2": 22.0, "co": 2.1, "o3": 48.0, "aqi": 315, "is_core": False},
    "Dwarka": {"lat": 28.5921, "lon": 77.0460, "state": "Delhi", "region": "North", "pm25": 104.0, "pm10": 210.0, "no2": 44.0, "so2": 15.5, "co": 1.35, "o3": 40.0, "aqi": 235, "is_core": False},
    "Rohini": {"lat": 28.7495, "lon": 77.0565, "state": "Delhi", "region": "North", "pm25": 119.0, "pm10": 240.0, "no2": 52.0, "so2": 18.0, "co": 1.6, "o3": 44.0, "aqi": 268, "is_core": False},
    "Okhla": {"lat": 28.5355, "lon": 77.2732, "state": "Delhi", "region": "North", "pm25": 128.0, "pm10": 255.0, "no2": 56.0, "so2": 19.5, "co": 1.75, "o3": 45.0, "aqi": 285, "is_core": False},
    "Shadipur": {"lat": 28.6517, "lon": 77.1583, "state": "Delhi", "region": "North", "pm25": 115.0, "pm10": 228.0, "no2": 49.0, "so2": 17.0, "co": 1.48, "o3": 41.5, "aqi": 252, "is_core": False},

    # ------------------ UTTAR PRADESH (8 cities) ------------------
    "Lucknow": {"lat": 26.8467, "lon": 80.9462, "state": "Uttar Pradesh", "region": "North", "pm25": 109.7, "pm10": 215.0, "no2": 37.8, "so2": 12.6, "co": 1.4, "o3": 36.0, "aqi": 218, "is_core": True},
    "Kanpur": {"lat": 26.4499, "lon": 80.3319, "state": "Uttar Pradesh", "region": "North", "pm25": 128.5, "pm10": 245.0, "no2": 44.0, "so2": 16.5, "co": 1.8, "o3": 41.0, "aqi": 265, "is_core": False},
    "Varanasi": {"lat": 25.3176, "lon": 82.9739, "state": "Uttar Pradesh", "region": "North", "pm25": 105.0, "pm10": 208.0, "no2": 36.0, "so2": 13.0, "co": 1.35, "o3": 35.0, "aqi": 212, "is_core": False},
    "Agra": {"lat": 27.1767, "lon": 78.0081, "state": "Uttar Pradesh", "region": "North", "pm25": 114.0, "pm10": 220.0, "no2": 40.0, "so2": 14.5, "co": 1.5, "o3": 38.0, "aqi": 230, "is_core": False},
    "Noida": {"lat": 28.5355, "lon": 77.3910, "state": "Uttar Pradesh", "region": "North", "pm25": 125.0, "pm10": 240.0, "no2": 51.0, "so2": 18.0, "co": 1.7, "o3": 44.0, "aqi": 272, "is_core": False},
    "Ghaziabad": {"lat": 28.6692, "lon": 77.4538, "state": "Uttar Pradesh", "region": "North", "pm25": 135.0, "pm10": 268.0, "no2": 55.0, "so2": 20.0, "co": 1.95, "o3": 47.0, "aqi": 298, "is_core": False},
    "Prayagraj": {"lat": 25.4358, "lon": 81.8463, "state": "Uttar Pradesh", "region": "North", "pm25": 98.0, "pm10": 195.0, "no2": 33.0, "so2": 12.0, "co": 1.25, "o3": 34.0, "aqi": 198, "is_core": False},
    "Meerut": {"lat": 28.9845, "lon": 77.7064, "state": "Uttar Pradesh", "region": "North", "pm25": 112.0, "pm10": 218.0, "no2": 39.0, "so2": 14.0, "co": 1.45, "o3": 37.0, "aqi": 224, "is_core": False},

    # ------------------ BIHAR (6 cities) ------------------
    "Patna": {"lat": 25.5941, "lon": 85.1376, "state": "Bihar", "region": "East", "pm25": 123.5, "pm10": 126.7, "no2": 37.5, "so2": 22.1, "co": 1.52, "o3": 39.0, "aqi": 241, "is_core": True},
    "Gaya": {"lat": 24.7914, "lon": 85.0002, "state": "Bihar", "region": "East", "pm25": 105.0, "pm10": 188.0, "no2": 32.0, "so2": 18.0, "co": 1.3, "o3": 35.0, "aqi": 215, "is_core": False},
    "Muzaffarpur": {"lat": 26.1209, "lon": 85.3647, "state": "Bihar", "region": "East", "pm25": 132.0, "pm10": 240.0, "no2": 42.0, "so2": 24.0, "co": 1.7, "o3": 41.0, "aqi": 262, "is_core": False},
    "Bhagalpur": {"lat": 25.2425, "lon": 86.9842, "state": "Bihar", "region": "East", "pm25": 112.0, "pm10": 202.0, "no2": 35.0, "so2": 19.0, "co": 1.4, "o3": 37.0, "aqi": 226, "is_core": False},
    "Darbhanga": {"lat": 26.1542, "lon": 85.8918, "state": "Bihar", "region": "East", "pm25": 120.0, "pm10": 218.0, "no2": 38.0, "so2": 21.0, "co": 1.5, "o3": 39.0, "aqi": 245, "is_core": False},
    "Purnia": {"lat": 25.7771, "lon": 87.4753, "state": "Bihar", "region": "East", "pm25": 98.0, "pm10": 178.0, "no2": 30.0, "so2": 16.0, "co": 1.2, "o3": 33.0, "aqi": 198, "is_core": False},

    # ------------------ RAJASTHAN (7 cities) ------------------
    "Jaipur": {"lat": 26.9124, "lon": 75.7873, "state": "Rajasthan", "region": "North-West", "pm25": 54.5, "pm10": 123.5, "no2": 32.4, "so2": 11.2, "co": 0.85, "o3": 34.0, "aqi": 134, "is_core": True},
    "Jodhpur": {"lat": 26.2389, "lon": 73.0243, "state": "Rajasthan", "region": "North-West", "pm25": 62.0, "pm10": 148.0, "no2": 30.0, "so2": 12.0, "co": 0.9, "o3": 36.0, "aqi": 148, "is_core": False},
    "Kota": {"lat": 25.2138, "lon": 75.8648, "state": "Rajasthan", "region": "North-West", "pm25": 58.0, "pm10": 132.0, "no2": 34.0, "so2": 13.5, "co": 0.95, "o3": 35.0, "aqi": 140, "is_core": False},
    "Bikaner": {"lat": 28.0229, "lon": 73.3119, "state": "Rajasthan", "region": "North-West", "pm25": 52.0, "pm10": 155.0, "no2": 28.0, "so2": 10.5, "co": 0.8, "o3": 33.0, "aqi": 132, "is_core": False},
    "Udaipur": {"lat": 24.5854, "lon": 73.7125, "state": "Rajasthan", "region": "North-West", "pm25": 44.0, "pm10": 102.0, "no2": 25.0, "so2": 9.5, "co": 0.75, "o3": 30.0, "aqi": 110, "is_core": False},
    "Ajmer": {"lat": 26.4499, "lon": 74.6399, "state": "Rajasthan", "region": "North-West", "pm25": 50.0, "pm10": 118.0, "no2": 29.0, "so2": 10.8, "co": 0.82, "o3": 32.0, "aqi": 124, "is_core": False},
    "Alwar": {"lat": 27.5530, "lon": 76.6346, "state": "Rajasthan", "region": "North-West", "pm25": 66.0, "pm10": 142.0, "no2": 35.0, "so2": 12.5, "co": 1.05, "o3": 37.0, "aqi": 152, "is_core": False},

    # ------------------ GUJARAT (7 cities) ------------------
    "Ahmedabad": {"lat": 23.0225, "lon": 72.5714, "state": "Gujarat", "region": "West", "pm25": 67.9, "pm10": 114.6, "no2": 59.0, "so2": 55.0, "co": 22.0, "o3": 39.0, "aqi": 452, "is_core": True},
    "Surat": {"lat": 21.1702, "lon": 72.8311, "state": "Gujarat", "region": "West", "pm25": 52.0, "pm10": 108.0, "no2": 38.0, "so2": 18.0, "co": 1.2, "o3": 34.0, "aqi": 126, "is_core": False},
    "Vadodara": {"lat": 22.3072, "lon": 73.1812, "state": "Gujarat", "region": "West", "pm25": 56.0, "pm10": 115.0, "no2": 42.0, "so2": 21.0, "co": 1.35, "o3": 36.0, "aqi": 135, "is_core": False},
    "Rajkot": {"lat": 22.3039, "lon": 70.8022, "state": "Gujarat", "region": "West", "pm25": 48.0, "pm10": 98.0, "no2": 32.0, "so2": 15.0, "co": 1.05, "o3": 32.0, "aqi": 118, "is_core": False},
    "Gandhinagar": {"lat": 23.2156, "lon": 72.6369, "state": "Gujarat", "region": "West", "pm25": 58.0, "pm10": 112.0, "no2": 39.0, "so2": 19.0, "co": 1.3, "o3": 35.0, "aqi": 138, "is_core": False},
    "Bhavnagar": {"lat": 21.7645, "lon": 72.1519, "state": "Gujarat", "region": "West", "pm25": 44.0, "pm10": 90.0, "no2": 28.0, "so2": 14.0, "co": 0.95, "o3": 30.0, "aqi": 108, "is_core": False},
    "Jamnagar": {"lat": 22.4707, "lon": 70.0577, "state": "Gujarat", "region": "West", "pm25": 50.0, "pm10": 104.0, "no2": 34.0, "so2": 17.5, "co": 1.15, "o3": 33.0, "aqi": 122, "is_core": False},

    # ------------------ MAHARASHTRA (7 cities) ------------------
    "Mumbai": {"lat": 19.0760, "lon": 72.8777, "state": "Maharashtra", "region": "West", "pm25": 35.2, "pm10": 96.7, "no2": 39.0, "so2": 17.5, "co": 0.85, "o3": 28.0, "aqi": 105, "is_core": True},
    "Pune": {"lat": 18.5204, "lon": 73.8567, "state": "Maharashtra", "region": "West", "pm25": 42.0, "pm10": 92.0, "no2": 36.0, "so2": 14.0, "co": 0.92, "o3": 32.0, "aqi": 112, "is_core": False},
    "Nagpur": {"lat": 21.1458, "lon": 79.0882, "state": "Maharashtra", "region": "West", "pm25": 46.0, "pm10": 105.0, "no2": 34.0, "so2": 16.0, "co": 0.98, "o3": 34.0, "aqi": 120, "is_core": False},
    "Nashik": {"lat": 19.9975, "lon": 73.7898, "state": "Maharashtra", "region": "West", "pm25": 38.0, "pm10": 84.0, "no2": 29.0, "so2": 12.0, "co": 0.8, "o3": 29.0, "aqi": 98, "is_core": False},
    "Aurangabad": {"lat": 19.8762, "lon": 75.3433, "state": "Maharashtra", "region": "West", "pm25": 40.0, "pm10": 88.0, "no2": 31.0, "so2": 13.0, "co": 0.85, "o3": 30.0, "aqi": 105, "is_core": False},
    "Thane": {"lat": 19.2183, "lon": 72.9781, "state": "Maharashtra", "region": "West", "pm25": 39.0, "pm10": 98.0, "no2": 41.0, "so2": 18.0, "co": 0.95, "o3": 27.0, "aqi": 110, "is_core": False},
    "Solapur": {"lat": 17.6599, "lon": 75.9064, "state": "Maharashtra", "region": "West", "pm25": 36.0, "pm10": 82.0, "no2": 28.0, "so2": 11.5, "co": 0.78, "o3": 28.0, "aqi": 95, "is_core": False},

    # ------------------ MADHYA PRADESH (6 cities) ------------------
    "Bhopal": {"lat": 23.2599, "lon": 77.4126, "state": "Madhya Pradesh", "region": "Central", "pm25": 50.1, "pm10": 119.3, "no2": 31.2, "so2": 13.8, "co": 0.9, "o3": 35.0, "aqi": 133, "is_core": True},
    "Indore": {"lat": 22.7196, "lon": 75.8577, "state": "Madhya Pradesh", "region": "Central", "pm25": 56.0, "pm10": 128.0, "no2": 35.0, "so2": 15.0, "co": 1.05, "o3": 37.0, "aqi": 142, "is_core": False},
    "Gwalior": {"lat": 26.2183, "lon": 78.1828, "state": "Madhya Pradesh", "region": "Central", "pm25": 84.0, "pm10": 185.0, "no2": 42.0, "so2": 18.0, "co": 1.45, "o3": 42.0, "aqi": 188, "is_core": False},
    "Jabalpur": {"lat": 23.1815, "lon": 79.9864, "state": "Madhya Pradesh", "region": "Central", "pm25": 48.0, "pm10": 110.0, "no2": 29.0, "so2": 12.5, "co": 0.85, "o3": 33.0, "aqi": 124, "is_core": False},
    "Ujjain": {"lat": 23.1765, "lon": 75.7885, "state": "Madhya Pradesh", "region": "Central", "pm25": 52.0, "pm10": 118.0, "no2": 32.0, "so2": 14.0, "co": 0.95, "o3": 34.0, "aqi": 132, "is_core": False},
    "Sagar": {"lat": 23.8388, "lon": 78.7378, "state": "Madhya Pradesh", "region": "Central", "pm25": 42.0, "pm10": 98.0, "no2": 26.0, "so2": 11.0, "co": 0.8, "o3": 30.0, "aqi": 112, "is_core": False},

    # ------------------ WEST BENGAL (6 cities) ------------------
    "Kolkata": {"lat": 22.5726, "lon": 88.3639, "state": "West Bengal", "region": "East", "pm25": 64.4, "pm10": 115.6, "no2": 40.2, "so2": 14.5, "co": 0.98, "o3": 32.0, "aqi": 141, "is_core": True},
    "Howrah": {"lat": 22.5958, "lon": 88.2636, "state": "West Bengal", "region": "East", "pm25": 74.0, "pm10": 136.0, "no2": 45.0, "so2": 18.0, "co": 1.15, "o3": 35.0, "aqi": 158, "is_core": False},
    "Asansol": {"lat": 23.6739, "lon": 86.9524, "state": "West Bengal", "region": "East", "pm25": 82.0, "pm10": 155.0, "no2": 48.0, "so2": 22.0, "co": 1.35, "o3": 38.0, "aqi": 172, "is_core": False},
    "Siliguri": {"lat": 26.7271, "lon": 88.3953, "state": "West Bengal", "region": "East", "pm25": 48.0, "pm10": 95.0, "no2": 28.0, "so2": 11.0, "co": 0.82, "o3": 28.0, "aqi": 115, "is_core": False},
    "Durgapur": {"lat": 23.5204, "lon": 87.3119, "state": "West Bengal", "region": "East", "pm25": 78.0, "pm10": 145.0, "no2": 44.0, "so2": 20.0, "co": 1.25, "o3": 36.0, "aqi": 164, "is_core": False},
    "Haldia": {"lat": 22.0667, "lon": 88.0698, "state": "West Bengal", "region": "East", "pm25": 62.0, "pm10": 120.0, "no2": 38.0, "so2": 25.0, "co": 1.1, "o3": 31.0, "aqi": 142, "is_core": False},

    # ------------------ KARNATAKA (6 cities) ------------------
    "Bengaluru": {"lat": 12.9716, "lon": 77.5946, "state": "Karnataka", "region": "South", "pm25": 35.8, "pm10": 83.2, "no2": 28.4, "so2": 10.2, "co": 0.95, "o3": 34.0, "aqi": 94, "is_core": True},
    "Mysuru": {"lat": 12.2958, "lon": 76.6394, "state": "Karnataka", "region": "South", "pm25": 28.0, "pm10": 62.0, "no2": 20.0, "so2": 8.0, "co": 0.7, "o3": 29.0, "aqi": 75, "is_core": False},
    "Hubballi": {"lat": 15.3647, "lon": 75.1240, "state": "Karnataka", "region": "South", "pm25": 38.0, "pm10": 88.0, "no2": 29.0, "so2": 11.0, "co": 0.85, "o3": 32.0, "aqi": 98, "is_core": False},
    "Mangaluru": {"lat": 12.9141, "lon": 74.8560, "state": "Karnataka", "region": "South", "pm25": 26.0, "pm10": 58.0, "no2": 19.0, "so2": 9.5, "co": 0.65, "o3": 27.0, "aqi": 70, "is_core": False},
    "Belagavi": {"lat": 15.8497, "lon": 74.4977, "state": "Karnataka", "region": "South", "pm25": 32.0, "pm10": 74.0, "no2": 24.0, "so2": 9.0, "co": 0.75, "o3": 30.0, "aqi": 85, "is_core": False},
    "Kalaburagi": {"lat": 17.3297, "lon": 76.8343, "state": "Karnataka", "region": "South", "pm25": 42.0, "pm10": 96.0, "no2": 28.0, "so2": 12.0, "co": 0.88, "o3": 35.0, "aqi": 108, "is_core": False},

    # ------------------ TAMIL NADU (6 cities) ------------------
    "Chennai": {"lat": 13.0827, "lon": 80.2707, "state": "Tamil Nadu", "region": "South", "pm25": 46.9, "pm10": 49.0, "no2": 21.0, "so2": 11.5, "co": 0.95, "o3": 34.0, "aqi": 108, "is_core": True},
    "Coimbatore": {"lat": 11.0168, "lon": 76.9558, "state": "Tamil Nadu", "region": "South", "pm25": 29.0, "pm10": 46.0, "no2": 18.0, "so2": 8.5, "co": 0.68, "o3": 28.0, "aqi": 73, "is_core": True},
    "Madurai": {"lat": 9.9252, "lon": 78.1198, "state": "Tamil Nadu", "region": "South", "pm25": 36.0, "pm10": 68.0, "no2": 22.0, "so2": 9.0, "co": 0.8, "o3": 30.0, "aqi": 88, "is_core": False},
    "Tiruchirappalli": {"lat": 10.7905, "lon": 78.7047, "state": "Tamil Nadu", "region": "South", "pm25": 34.0, "pm10": 64.0, "no2": 20.0, "so2": 8.8, "co": 0.76, "o3": 29.0, "aqi": 84, "is_core": False},
    "Salem": {"lat": 11.6643, "lon": 78.1460, "state": "Tamil Nadu", "region": "South", "pm25": 42.0, "pm10": 82.0, "no2": 26.0, "so2": 11.0, "co": 0.88, "o3": 32.0, "aqi": 102, "is_core": False},
    "Tirunelveli": {"lat": 8.7139, "lon": 77.7567, "state": "Tamil Nadu", "region": "South", "pm25": 28.0, "pm10": 54.0, "no2": 17.0, "so2": 7.5, "co": 0.65, "o3": 27.0, "aqi": 72, "is_core": False},

    # ------------------ KERALA (7 cities) ------------------
    "Thiruvananthapuram": {"lat": 8.5241, "lon": 76.9366, "state": "Kerala", "region": "South", "pm25": 28.1, "pm10": 54.0, "no2": 14.5, "so2": 6.8, "co": 0.72, "o3": 25.0, "aqi": 76, "is_core": True},
    "Kochi": {"lat": 9.9312, "lon": 76.2673, "state": "Kerala", "region": "South", "pm25": 32.0, "pm10": 62.0, "no2": 18.0, "so2": 8.5, "co": 0.85, "o3": 28.0, "aqi": 88, "is_core": True},
    "Ernakulam": {"lat": 9.9816, "lon": 76.2999, "state": "Kerala", "region": "South", "pm25": 34.0, "pm10": 65.0, "no2": 19.5, "so2": 9.0, "co": 0.9, "o3": 29.0, "aqi": 92, "is_core": True},
    "Kozhikode": {"lat": 11.2588, "lon": 75.7804, "state": "Kerala", "region": "South", "pm25": 25.0, "pm10": 48.0, "no2": 15.0, "so2": 6.5, "co": 0.65, "o3": 24.0, "aqi": 68, "is_core": False},
    "Thrissur": {"lat": 10.5276, "lon": 76.2144, "state": "Kerala", "region": "South", "pm25": 26.5, "pm10": 52.0, "no2": 16.0, "so2": 7.0, "co": 0.7, "o3": 26.0, "aqi": 72, "is_core": False},
    "Kollam": {"lat": 8.8932, "lon": 76.6141, "state": "Kerala", "region": "South", "pm25": 24.0, "pm10": 46.0, "no2": 14.0, "so2": 6.2, "co": 0.62, "o3": 23.0, "aqi": 65, "is_core": False},
    "Kannur": {"lat": 11.8745, "lon": 75.3704, "state": "Kerala", "region": "South", "pm25": 23.0, "pm10": 44.0, "no2": 13.5, "so2": 5.8, "co": 0.6, "o3": 22.0, "aqi": 62, "is_core": False},

    # ------------------ ANDHRA PRADESH (7 cities) ------------------
    "Visakhapatnam": {"lat": 17.6868, "lon": 83.2185, "state": "Andhra Pradesh", "region": "South", "pm25": 43.1, "pm10": 93.5, "no2": 28.5, "so2": 12.0, "co": 0.85, "o3": 31.0, "aqi": 108, "is_core": True},
    "Amaravati": {"lat": 16.5417, "lon": 80.5158, "state": "Andhra Pradesh", "region": "South", "pm25": 38.0, "pm10": 82.0, "no2": 24.0, "so2": 10.0, "co": 0.78, "o3": 29.0, "aqi": 95, "is_core": True},
    "Vijayawada": {"lat": 16.5062, "lon": 80.6480, "state": "Andhra Pradesh", "region": "South", "pm25": 46.0, "pm10": 98.0, "no2": 31.0, "so2": 13.0, "co": 0.95, "o3": 33.0, "aqi": 115, "is_core": False},
    "Guntur": {"lat": 16.3067, "lon": 80.4365, "state": "Andhra Pradesh", "region": "South", "pm25": 44.0, "pm10": 92.0, "no2": 29.0, "so2": 12.0, "co": 0.9, "o3": 32.0, "aqi": 110, "is_core": False},
    "Nellore": {"lat": 14.4426, "lon": 79.9865, "state": "Andhra Pradesh", "region": "South", "pm25": 35.0, "pm10": 74.0, "no2": 22.0, "so2": 9.5, "co": 0.72, "o3": 28.0, "aqi": 88, "is_core": False},
    "Kurnool": {"lat": 15.8281, "lon": 78.0373, "state": "Andhra Pradesh", "region": "South", "pm25": 40.0, "pm10": 86.0, "no2": 26.0, "so2": 11.0, "co": 0.82, "o3": 30.0, "aqi": 102, "is_core": False},
    "Tirupati": {"lat": 13.6288, "lon": 79.4192, "state": "Andhra Pradesh", "region": "South", "pm25": 32.0, "pm10": 68.0, "no2": 20.0, "so2": 8.5, "co": 0.68, "o3": 27.0, "aqi": 80, "is_core": False},

    # ------------------ TELANGANA (6 cities) ------------------
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867, "state": "Telangana", "region": "South", "pm25": 47.0, "pm10": 91.9, "no2": 31.0, "so2": 10.5, "co": 0.82, "o3": 32.0, "aqi": 109, "is_core": True},
    "Warangal": {"lat": 17.9689, "lon": 79.5941, "state": "Telangana", "region": "South", "pm25": 42.0, "pm10": 84.0, "no2": 26.0, "so2": 9.8, "co": 0.75, "o3": 30.0, "aqi": 98, "is_core": False},
    "Nizamabad": {"lat": 18.6725, "lon": 78.0941, "state": "Telangana", "region": "South", "pm25": 39.0, "pm10": 78.0, "no2": 24.0, "so2": 9.0, "co": 0.7, "o3": 28.0, "aqi": 92, "is_core": False},
    "Karimnagar": {"lat": 18.4386, "lon": 79.1288, "state": "Telangana", "region": "South", "pm25": 45.0, "pm10": 90.0, "no2": 28.0, "so2": 11.0, "co": 0.8, "o3": 31.0, "aqi": 105, "is_core": False},
    "Khammam": {"lat": 17.2473, "lon": 80.1514, "state": "Telangana", "region": "South", "pm25": 41.0, "pm10": 82.0, "no2": 25.0, "so2": 10.0, "co": 0.74, "o3": 29.0, "aqi": 96, "is_core": False},
    "Ramagundam": {"lat": 18.8016, "lon": 79.4588, "state": "Telangana", "region": "South", "pm25": 58.0, "pm10": 125.0, "no2": 38.0, "so2": 24.0, "co": 1.2, "o3": 36.0, "aqi": 138, "is_core": False},

    # ------------------ ODISHA (7 cities) ------------------
    "Bhubaneswar": {"lat": 20.2961, "lon": 85.8245, "state": "Odisha", "region": "East", "pm25": 54.0, "pm10": 118.0, "no2": 26.0, "so2": 12.0, "co": 0.88, "o3": 32.0, "aqi": 130, "is_core": False},
    "Cuttack": {"lat": 20.4625, "lon": 85.8830, "state": "Odisha", "region": "East", "pm25": 58.0, "pm10": 126.0, "no2": 28.0, "so2": 13.5, "co": 0.95, "o3": 34.0, "aqi": 138, "is_core": False},
    "Rourkela": {"lat": 22.2604, "lon": 84.8536, "state": "Odisha", "region": "East", "pm25": 76.0, "pm10": 162.0, "no2": 38.0, "so2": 28.0, "co": 1.45, "o3": 38.0, "aqi": 172, "is_core": False},
    "Brajrajnagar": {"lat": 21.8258, "lon": 83.9214, "state": "Odisha", "region": "East", "pm25": 62.7, "pm10": 144.7, "no2": 22.0, "so2": 16.5, "co": 1.1, "o3": 34.0, "aqi": 162, "is_core": True},
    "Talcher": {"lat": 20.9500, "lon": 85.2167, "state": "Odisha", "region": "East", "pm25": 68.0, "pm10": 155.0, "no2": 32.0, "so2": 32.0, "co": 1.35, "o3": 36.0, "aqi": 168, "is_core": True},
    "Sambalpur": {"lat": 21.4669, "lon": 83.9812, "state": "Odisha", "region": "East", "pm25": 60.0, "pm10": 130.0, "no2": 25.0, "so2": 18.0, "co": 1.05, "o3": 33.0, "aqi": 142, "is_core": False},
    "Balasore": {"lat": 21.4934, "lon": 86.9135, "state": "Odisha", "region": "East", "pm25": 52.0, "pm10": 110.0, "no2": 23.0, "so2": 11.5, "co": 0.85, "o3": 30.0, "aqi": 125, "is_core": False},

    # ------------------ JHARKHAND (7 cities) ------------------
    "Ranchi": {"lat": 23.3441, "lon": 85.3096, "state": "Jharkhand", "region": "East", "pm25": 56.0, "pm10": 128.0, "no2": 28.0, "so2": 14.0, "co": 0.95, "o3": 32.0, "aqi": 135, "is_core": False},
    "Jamshedpur": {"lat": 22.8046, "lon": 86.2029, "state": "Jharkhand", "region": "East", "pm25": 78.0, "pm10": 165.0, "no2": 42.0, "so2": 26.0, "co": 1.5, "o3": 38.0, "aqi": 175, "is_core": False},
    "Dhanbad": {"lat": 23.7957, "lon": 86.4304, "state": "Jharkhand", "region": "East", "pm25": 86.0, "pm10": 185.0, "no2": 46.0, "so2": 30.0, "co": 1.8, "o3": 42.0, "aqi": 195, "is_core": False},
    "Bokaro": {"lat": 23.6693, "lon": 86.1511, "state": "Jharkhand", "region": "East", "pm25": 72.0, "pm10": 152.0, "no2": 38.0, "so2": 24.0, "co": 1.4, "o3": 36.0, "aqi": 165, "is_core": False},
    "Jorapokhar": {"lat": 23.7022, "lon": 86.4131, "state": "Jharkhand", "region": "East", "pm25": 64.2, "pm10": 149.7, "no2": 24.5, "so2": 22.0, "co": 1.2, "o3": 33.0, "aqi": 159, "is_core": True},
    "Deoghar": {"lat": 24.4826, "lon": 86.7001, "state": "Jharkhand", "region": "East", "pm25": 48.0, "pm10": 105.0, "no2": 22.0, "so2": 11.0, "co": 0.8, "o3": 28.0, "aqi": 118, "is_core": False},
    "Hazaribagh": {"lat": 23.9961, "lon": 85.3695, "state": "Jharkhand", "region": "East", "pm25": 52.0, "pm10": 115.0, "no2": 25.0, "so2": 13.0, "co": 0.88, "o3": 30.0, "aqi": 126, "is_core": False},

    # ------------------ ASSAM (6 cities) ------------------
    "Guwahati": {"lat": 26.1445, "lon": 91.7362, "state": "Assam", "region": "North-East", "pm25": 63.7, "pm10": 116.6, "no2": 24.8, "so2": 11.4, "co": 0.85, "o3": 26.0, "aqi": 140, "is_core": True},
    "Silchar": {"lat": 24.8333, "lon": 92.7789, "state": "Assam", "region": "North-East", "pm25": 44.0, "pm10": 82.0, "no2": 18.0, "so2": 8.0, "co": 0.68, "o3": 22.0, "aqi": 105, "is_core": False},
    "Dibrugarh": {"lat": 27.4728, "lon": 94.9120, "state": "Assam", "region": "North-East", "pm25": 46.0, "pm10": 86.0, "no2": 19.5, "so2": 9.0, "co": 0.72, "o3": 24.0, "aqi": 110, "is_core": False},
    "Jorhat": {"lat": 26.7509, "lon": 94.2037, "state": "Assam", "region": "North-East", "pm25": 42.0, "pm10": 78.0, "no2": 17.0, "so2": 8.2, "co": 0.65, "o3": 21.0, "aqi": 98, "is_core": False},
    "Nagaon": {"lat": 26.3452, "lon": 92.6840, "state": "Assam", "region": "North-East", "pm25": 45.0, "pm10": 84.0, "no2": 19.0, "so2": 8.8, "co": 0.7, "o3": 23.0, "aqi": 106, "is_core": False},
    "Tezpur": {"lat": 26.6528, "lon": 92.7926, "state": "Assam", "region": "North-East", "pm25": 40.0, "pm10": 75.0, "no2": 16.5, "so2": 7.8, "co": 0.62, "o3": 20.0, "aqi": 95, "is_core": False},

    # ------------------ HIMACHAL PRADESH (6 cities) ------------------
    "Shimla": {"lat": 31.1048, "lon": 77.1734, "state": "Himachal Pradesh", "region": "North", "pm25": 22.0, "pm10": 48.0, "no2": 14.0, "so2": 5.5, "co": 0.55, "o3": 28.0, "aqi": 58, "is_core": False},
    "Dharamshala": {"lat": 32.2190, "lon": 76.3234, "state": "Himachal Pradesh", "region": "North", "pm25": 20.0, "pm10": 42.0, "no2": 12.0, "so2": 4.8, "co": 0.5, "o3": 26.0, "aqi": 52, "is_core": False},
    "Solan": {"lat": 30.9045, "lon": 77.0967, "state": "Himachal Pradesh", "region": "North", "pm25": 28.0, "pm10": 60.0, "no2": 18.0, "so2": 6.8, "co": 0.65, "o3": 29.0, "aqi": 72, "is_core": False},
    "Mandi": {"lat": 31.7087, "lon": 76.9320, "state": "Himachal Pradesh", "region": "North", "pm25": 24.0, "pm10": 52.0, "no2": 15.0, "so2": 5.8, "co": 0.58, "o3": 27.0, "aqi": 62, "is_core": False},
    "Baddi": {"lat": 30.9578, "lon": 76.7914, "state": "Himachal Pradesh", "region": "North", "pm25": 48.0, "pm10": 105.0, "no2": 32.0, "so2": 14.0, "co": 0.95, "o3": 34.0, "aqi": 122, "is_core": False},
    "Kullu": {"lat": 31.9579, "lon": 77.1095, "state": "Himachal Pradesh", "region": "North", "pm25": 18.0, "pm10": 38.0, "no2": 11.0, "so2": 4.2, "co": 0.45, "o3": 25.0, "aqi": 48, "is_core": False},

    # ------------------ UTTARAKHAND (6 cities) ------------------
    "Dehradun": {"lat": 30.3165, "lon": 78.0322, "state": "Uttarakhand", "region": "North", "pm25": 38.0, "pm10": 85.0, "no2": 24.0, "so2": 9.5, "co": 0.78, "o3": 30.0, "aqi": 95, "is_core": False},
    "Haridwar": {"lat": 29.9457, "lon": 78.1642, "state": "Uttarakhand", "region": "North", "pm25": 46.0, "pm10": 98.0, "no2": 28.0, "so2": 11.0, "co": 0.9, "o3": 32.0, "aqi": 112, "is_core": False},
    "Roorkee": {"lat": 29.8543, "lon": 77.8880, "state": "Uttarakhand", "region": "North", "pm25": 48.0, "pm10": 102.0, "no2": 30.0, "so2": 12.0, "co": 0.95, "o3": 33.0, "aqi": 118, "is_core": False},
    "Haldwani": {"lat": 29.2183, "lon": 79.5130, "state": "Uttarakhand", "region": "North", "pm25": 36.0, "pm10": 78.0, "no2": 22.0, "so2": 8.8, "co": 0.72, "o3": 28.0, "aqi": 88, "is_core": False},
    "Rishikesh": {"lat": 30.0869, "lon": 78.2676, "state": "Uttarakhand", "region": "North", "pm25": 28.0, "pm10": 62.0, "no2": 17.0, "so2": 6.8, "co": 0.6, "o3": 26.0, "aqi": 72, "is_core": False},
    "Rudrapur": {"lat": 28.9800, "lon": 79.4000, "state": "Uttarakhand", "region": "North", "pm25": 52.0, "pm10": 110.0, "no2": 32.0, "so2": 13.5, "co": 1.05, "o3": 34.0, "aqi": 126, "is_core": False},

    # ------------------ JAMMU & KASHMIR (5 cities) ------------------
    "Srinagar": {"lat": 34.0837, "lon": 74.7973, "state": "Jammu and Kashmir", "region": "North", "pm25": 32.0, "pm10": 68.0, "no2": 18.0, "so2": 7.5, "co": 0.7, "o3": 28.0, "aqi": 80, "is_core": False},
    "Jammu": {"lat": 32.7266, "lon": 74.8570, "state": "Jammu and Kashmir", "region": "North", "pm25": 44.0, "pm10": 95.0, "no2": 26.0, "so2": 10.5, "co": 0.88, "o3": 32.0, "aqi": 108, "is_core": False},
    "Anantnag": {"lat": 33.7311, "lon": 75.1522, "state": "Jammu and Kashmir", "region": "North", "pm25": 26.0, "pm10": 55.0, "no2": 15.0, "so2": 6.0, "co": 0.6, "o3": 25.0, "aqi": 68, "is_core": False},
    "Baramulla": {"lat": 34.2014, "lon": 74.3436, "state": "Jammu and Kashmir", "region": "North", "pm25": 25.0, "pm10": 52.0, "no2": 14.0, "so2": 5.8, "co": 0.58, "o3": 24.0, "aqi": 65, "is_core": False},
    "Udhampur": {"lat": 32.9248, "lon": 75.1340, "state": "Jammu and Kashmir", "region": "North", "pm25": 35.0, "pm10": 74.0, "no2": 20.0, "so2": 8.0, "co": 0.75, "o3": 29.0, "aqi": 88, "is_core": False},

    # ------------------ CHHATTISGARH (6 cities) ------------------
    "Raipur": {"lat": 21.2514, "lon": 81.6296, "state": "Chhattisgarh", "region": "Central", "pm25": 66.0, "pm10": 148.0, "no2": 36.0, "so2": 22.0, "co": 1.25, "o3": 35.0, "aqi": 152, "is_core": False},
    "Bhilai": {"lat": 21.1938, "lon": 81.3509, "state": "Chhattisgarh", "region": "Central", "pm25": 74.0, "pm10": 165.0, "no2": 42.0, "so2": 28.0, "co": 1.45, "o3": 38.0, "aqi": 168, "is_core": False},
    "Bilaspur": {"lat": 22.0797, "lon": 82.1409, "state": "Chhattisgarh", "region": "Central", "pm25": 58.0, "pm10": 128.0, "no2": 30.0, "so2": 18.0, "co": 1.1, "o3": 33.0, "aqi": 138, "is_core": False},
    "Korba": {"lat": 22.3595, "lon": 82.7501, "state": "Chhattisgarh", "region": "Central", "pm25": 82.0, "pm10": 180.0, "no2": 46.0, "so2": 36.0, "co": 1.6, "o3": 40.0, "aqi": 185, "is_core": False},
    "Durg": {"lat": 21.1904, "lon": 81.2849, "state": "Chhattisgarh", "region": "Central", "pm25": 68.0, "pm10": 150.0, "no2": 38.0, "so2": 24.0, "co": 1.3, "o3": 36.0, "aqi": 156, "is_core": False},
    "Rajnandgaon": {"lat": 21.0974, "lon": 81.0396, "state": "Chhattisgarh", "region": "Central", "pm25": 52.0, "pm10": 115.0, "no2": 26.0, "so2": 15.0, "co": 0.95, "o3": 30.0, "aqi": 124, "is_core": False},

    # ------------------ GOA (5 cities) ------------------
    "Panaji": {"lat": 15.4909, "lon": 73.8278, "state": "Goa", "region": "West", "pm25": 28.0, "pm10": 58.0, "no2": 18.0, "so2": 8.0, "co": 0.65, "o3": 26.0, "aqi": 70, "is_core": False},
    "Margao": {"lat": 15.2832, "lon": 73.9862, "state": "Goa", "region": "West", "pm25": 30.0, "pm10": 62.0, "no2": 19.0, "so2": 8.5, "co": 0.7, "o3": 27.0, "aqi": 75, "is_core": False},
    "Vasco da Gama": {"lat": 15.3982, "lon": 73.8113, "state": "Goa", "region": "West", "pm25": 34.0, "pm10": 70.0, "no2": 22.0, "so2": 10.5, "co": 0.8, "o3": 28.0, "aqi": 85, "is_core": False},
    "Mapusa": {"lat": 15.5937, "lon": 73.8142, "state": "Goa", "region": "West", "pm25": 27.0, "pm10": 56.0, "no2": 17.0, "so2": 7.5, "co": 0.62, "o3": 25.0, "aqi": 68, "is_core": False},
    "Ponda": {"lat": 15.4026, "lon": 74.0086, "state": "Goa", "region": "West", "pm25": 29.0, "pm10": 60.0, "no2": 18.5, "so2": 8.0, "co": 0.68, "o3": 26.0, "aqi": 72, "is_core": False},

    # ------------------ MEGHALAYA (5 cities) ------------------
    "Shillong": {"lat": 25.5788, "lon": 91.8933, "state": "Meghalaya", "region": "North-East", "pm25": 30.8, "pm10": 42.2, "no2": 14.5, "so2": 6.8, "co": 0.52, "o3": 22.0, "aqi": 54, "is_core": True},
    "Tura": {"lat": 25.5141, "lon": 90.2032, "state": "Meghalaya", "region": "North-East", "pm25": 24.0, "pm10": 38.0, "no2": 12.0, "so2": 5.5, "co": 0.45, "o3": 20.0, "aqi": 48, "is_core": False},
    "Jowai": {"lat": 25.4529, "lon": 92.2048, "state": "Meghalaya", "region": "North-East", "pm25": 28.0, "pm10": 40.0, "no2": 13.5, "so2": 6.0, "co": 0.48, "o3": 21.0, "aqi": 52, "is_core": False},
    "Nongpoh": {"lat": 25.9037, "lon": 91.8814, "state": "Meghalaya", "region": "North-East", "pm25": 32.0, "pm10": 46.0, "no2": 15.0, "so2": 7.0, "co": 0.55, "o3": 23.0, "aqi": 58, "is_core": False},
    "Cherrapunji": {"lat": 25.2702, "lon": 91.7323, "state": "Meghalaya", "region": "North-East", "pm25": 16.0, "pm10": 26.0, "no2": 8.0, "so2": 3.8, "co": 0.35, "o3": 18.0, "aqi": 35, "is_core": False},

    # ------------------ MIZORAM (5 cities) ------------------
    "Aizawl": {"lat": 23.7271, "lon": 92.7176, "state": "Mizoram", "region": "North-East", "pm25": 17.1, "pm10": 23.4, "no2": 9.5, "so2": 4.2, "co": 0.38, "o3": 19.0, "aqi": 35, "is_core": True},
    "Lunglei": {"lat": 22.8878, "lon": 92.7410, "state": "Mizoram", "region": "North-East", "pm25": 15.0, "pm10": 21.0, "no2": 8.0, "so2": 3.8, "co": 0.32, "o3": 17.0, "aqi": 30, "is_core": False},
    "Champhai": {"lat": 23.4756, "lon": 93.3276, "state": "Mizoram", "region": "North-East", "pm25": 14.0, "pm10": 20.0, "no2": 7.5, "so2": 3.5, "co": 0.3, "o3": 16.0, "aqi": 28, "is_core": False},
    "Serchhip": {"lat": 23.3411, "lon": 92.8504, "state": "Mizoram", "region": "North-East", "pm25": 16.0, "pm10": 22.0, "no2": 8.5, "so2": 4.0, "co": 0.35, "o3": 18.0, "aqi": 32, "is_core": False},
    "Kolasib": {"lat": 24.2244, "lon": 92.6780, "state": "Mizoram", "region": "North-East", "pm25": 18.0, "pm10": 25.0, "no2": 10.0, "so2": 4.5, "co": 0.4, "o3": 20.0, "aqi": 38, "is_core": False},

    # ------------------ TRIPURA (5 cities) ------------------
    "Agartala": {"lat": 23.8315, "lon": 91.2868, "state": "Tripura", "region": "North-East", "pm25": 38.0, "pm10": 76.0, "no2": 19.0, "so2": 8.5, "co": 0.72, "o3": 26.0, "aqi": 88, "is_core": False},
    "Dharmanagar": {"lat": 24.3752, "lon": 92.1645, "state": "Tripura", "region": "North-East", "pm25": 30.0, "pm10": 62.0, "no2": 15.0, "so2": 7.0, "co": 0.6, "o3": 22.0, "aqi": 72, "is_core": False},
    "Udaipur-TR": {"lat": 23.5333, "lon": 91.4833, "state": "Tripura", "region": "North-East", "pm25": 32.0, "pm10": 66.0, "no2": 16.0, "so2": 7.5, "co": 0.65, "o3": 24.0, "aqi": 76, "is_core": False},
    "Kailashahar": {"lat": 24.3297, "lon": 92.0076, "state": "Tripura", "region": "North-East", "pm25": 28.0, "pm10": 58.0, "no2": 14.0, "so2": 6.8, "co": 0.58, "o3": 21.0, "aqi": 68, "is_core": False},
    "Belonia": {"lat": 23.2500, "lon": 91.4500, "state": "Tripura", "region": "North-East", "pm25": 26.0, "pm10": 54.0, "no2": 13.0, "so2": 6.2, "co": 0.55, "o3": 20.0, "aqi": 64, "is_core": False},

    # ------------------ CHANDIGARH (5 sectors) ------------------
    "Chandigarh": {"lat": 30.7333, "lon": 76.7794, "state": "Chandigarh", "region": "North", "pm25": 41.1, "pm10": 85.7, "no2": 22.4, "so2": 9.8, "co": 0.82, "o3": 31.0, "aqi": 96, "is_core": True},
    "Sector 17": {"lat": 30.7415, "lon": 76.7794, "state": "Chandigarh", "region": "North", "pm25": 42.0, "pm10": 88.0, "no2": 24.0, "so2": 10.2, "co": 0.85, "o3": 32.0, "aqi": 98, "is_core": False},
    "Sector 22": {"lat": 30.7300, "lon": 76.7650, "state": "Chandigarh", "region": "North", "pm25": 40.0, "pm10": 84.0, "no2": 22.0, "so2": 9.5, "co": 0.8, "o3": 30.0, "aqi": 94, "is_core": False},
    "Manimajra": {"lat": 30.7200, "lon": 76.8400, "state": "Chandigarh", "region": "North", "pm25": 44.0, "pm10": 92.0, "no2": 25.0, "so2": 10.8, "co": 0.9, "o3": 33.0, "aqi": 104, "is_core": False},
    "Ind Area Chd": {"lat": 30.7050, "lon": 76.8000, "state": "Chandigarh", "region": "North", "pm25": 52.0, "pm10": 110.0, "no2": 32.0, "so2": 14.5, "co": 1.15, "o3": 35.0, "aqi": 126, "is_core": False}
}
