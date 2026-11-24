import io
from flask import Flask, render_template, jsonify, request, Response, send_file
import numpy as np
import pandas as pd

from services.data_service import (
    load_historical_dataset,
    get_available_cities,
    get_city_history,
    records_to_json,
    get_map_data,
    get_all_cities_rankings,
    get_city_trends,
    compare_cities_data,
    get_city_report_data
)

from services.weather_service import get_live_weather_and_aqi
from services.advisory_service import get_health_advisory

from models.dbscan_model import run_dbscan
from models.hierarchical import run_hierarchical
from models.evaluation import evaluate_clustering


app = Flask(__name__)

# In-memory cached dataset for instant response times
_CACHED_DF = None


# -----------------------------------------
# DATA LOADING
# -----------------------------------------

def load_dataset():
    """Load or retrieve cached historical air pollution dataset."""
    global _CACHED_DF
    if _CACHED_DF is None:
        _CACHED_DF = load_historical_dataset()
    return _CACHED_DF


# -----------------------------------------
# HELPER FUNCTION
# -----------------------------------------

def make_json_safe(value):
    """Convert NumPy and Pandas values into JSON-safe values."""
    if isinstance(value, dict):
        return {
            str(key): make_json_safe(val)
            for key, val in value.items()
        }

    if isinstance(value, (list, tuple)):
        return [make_json_safe(item) for item in value]

    if isinstance(value, np.ndarray):
        return make_json_safe(value.tolist())

    if isinstance(value, (np.integer,)):
        return int(value)

    if isinstance(value, (np.floating,)):
        return float(value) if np.isfinite(value) else None

    if isinstance(value, (np.bool_,)):
        return bool(value)

    if pd.isna(value):
        return None

    return value


# -----------------------------------------
# PAGE ROUTES
# -----------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/map")
def map_page():
    return render_template("map.html")


@app.route("/explorer")
def explorer():
    return render_template("explorer.html")


@app.route("/discovery")
def discovery():
    return render_template("discovery.html")


@app.route("/insights")
def insights():
    return render_template("insights.html")


@app.route("/compare")
def compare_page():
    return render_template("compare.html")


@app.route("/rankings")
def rankings_page():
    return render_template("rankings.html")


@app.route("/report/<path:city>")
def report_page(city):
    return render_template("report.html", city=city)


# -----------------------------------------
# API: GET ALL AVAILABLE CITIES
# -----------------------------------------

@app.route("/api/cities")
def api_cities():
    try:
        df = load_dataset()
        cities = get_available_cities(df)
        return jsonify({
            "success": True,
            "cities": cities
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# API: GET CITY POLLUTION DATA
# -----------------------------------------

@app.route("/api/city/<path:city>")
def api_city(city):
    try:
        df = load_dataset()
        city_data = get_city_history(df, city)

        if city_data.empty:
            return jsonify({
                "success": False,
                "error": f"City '{city}' not found in the dataset."
            }), 404

        total_records = len(city_data)
        recent_data = city_data.head(30)
        recent_records = records_to_json(recent_data)
        latest_record = recent_records[0] if recent_records else {}

        # Fetch live weather/AQI simulation or reading
        weather_info = get_live_weather_and_aqi(city, latest_record=latest_record)

        # Health advisory
        advisory = get_health_advisory(
            latest_record.get("AQI") or weather_info.get("aqi"),
            pm25=latest_record.get("PM2.5"),
            pm10=latest_record.get("PM10"),
            city=city
        )

        return jsonify(make_json_safe({
            "success": True,
            "city": city,
            "total_records": total_records,
            "latest_record": latest_record,
            "recent_records": recent_records,
            "weather": weather_info,
            "advisory": advisory
        }))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# API: INTERACTIVE MAP DATA
# -----------------------------------------

@app.route("/api/map-data")
def api_map_data():
    try:
        df = load_dataset()
        data = get_map_data(df)
        return jsonify(make_json_safe({
            "success": True,
            **data
        }))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# API: LIVE WEATHER & AIR QUALITY
# -----------------------------------------

@app.route("/api/live/<path:city>")
def api_live(city):
    try:
        df = load_dataset()
        city_data = get_city_history(df, city, limit=1)
        latest_record = {}
        if not city_data.empty:
            rec_list = records_to_json(city_data)
            if rec_list:
                latest_record = rec_list[0]

        data = get_live_weather_and_aqi(city, latest_record=latest_record)
        return jsonify(make_json_safe({
            "success": True,
            **data
        }))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# API: CITY COMPARISON
# -----------------------------------------

@app.route("/api/compare")
def api_compare():
    try:
        cities_param = request.args.get("cities")
        if not cities_param:
            cities_list = request.args.getlist("city")
        else:
            cities_list = [c.strip() for c in cities_param.split(",") if c.strip()]

        if not cities_list or len(cities_list) < 2:
            return jsonify({
                "success": False,
                "error": "Please provide at least two cities to compare (e.g. ?cities=Delhi,Mumbai)."
            }), 400

        df = load_dataset()
        comparison = compare_cities_data(df, cities_list)
        return jsonify(make_json_safe({
            "success": True,
            **comparison
        }))
    except ValueError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# API: HISTORICAL POLLUTION TRENDS
# -----------------------------------------

@app.route("/api/trends/<path:city>")
def api_trends(city):
    try:
        df = load_dataset()
        trends = get_city_trends(df, city)
        if not trends:
            return jsonify({
                "success": False,
                "error": f"No trend data found for city '{city}'."
            }), 404

        return jsonify(make_json_safe({
            "success": True,
            **trends
        }))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# API: RANKINGS (CLEANEST & MOST POLLUTED)
# -----------------------------------------

@app.route("/api/rankings")
def api_rankings():
    try:
        df = load_dataset()
        rankings = get_all_cities_rankings(df)
        return jsonify(make_json_safe({
            "success": True,
            **rankings
        }))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# API: HEALTH ADVISORY
# -----------------------------------------

@app.route("/api/advisory/<path:city>")
def api_city_advisory(city):
    try:
        df = load_dataset()
        city_data = get_city_history(df, city, limit=1)
        if city_data.empty:
            return jsonify({
                "success": False,
                "error": f"City '{city}' not found."
            }), 404

        row = city_data.iloc[0]
        advisory = get_health_advisory(
            row.get("AQI"),
            pm25=row.get("PM2.5"),
            pm10=row.get("PM10"),
            city=city
        )
        return jsonify(make_json_safe({
            "success": True,
            **advisory
        }))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/api/advisory/aqi/<int:aqi_val>")
def api_aqi_advisory(aqi_val):
    try:
        advisory = get_health_advisory(aqi_val)
        return jsonify(make_json_safe({
            "success": True,
            **advisory
        }))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# API: DATA EXPORT (CSV & JSON)
# -----------------------------------------

@app.route("/api/export/csv/<path:city>")
def api_export_csv(city):
    try:
        df = load_dataset()
        city_data = df[df["City"].str.casefold() == city.strip().casefold()].copy()
        if city_data.empty:
            return jsonify({
                "success": False,
                "error": f"City '{city}' not found."
            }), 404

        output = io.StringIO()
        city_data.to_csv(output, index=False)
        output.seek(0)

        filename = f"AirInsight_{city.replace(' ', '_')}_pollution_records.csv"
        return Response(
            output.getvalue(),
            mimetype="text/csv",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/api/export/json/<path:city>")
def api_export_json(city):
    try:
        df = load_dataset()
        report_data = get_city_report_data(df, city)
        return jsonify(make_json_safe({
            "success": True,
            "exported_at": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
            **report_data
        }))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# API: AI POLLUTION DISCOVERY
# -----------------------------------------

@app.route("/api/discovery/<method>/<path:city>")
def api_discovery(method, city):
    try:
        df = load_dataset()
        city_data = df[
            df["City"].str.casefold() == city.strip().casefold()
        ].copy()

        if city_data.empty:
            return jsonify({
                "success": False,
                "error": "No records found for this city."
            }), 404

        if method.lower() == "dbscan":
            eps = float(request.args.get("eps", 0.8))
            min_samples = int(request.args.get("min_samples", 5))
            output = run_dbscan(
                city_data,
                eps=eps,
                min_samples=min_samples
            )
            algorithm_name = "DBSCAN"

        elif method.lower() == "hierarchical":
            n_clusters = int(request.args.get("n_clusters", 4))
            output = run_hierarchical(
                city_data,
                n_clusters=n_clusters
            )
            algorithm_name = "Hierarchical Clustering"

        else:
            return jsonify({
                "success": False,
                "error": "Invalid clustering algorithm."
            }), 400

        # Evaluation
        evaluation = evaluate_clustering(
            output["scaled_data"],
            output["labels"]
        )

        pca_coordinates = output.get("pca", output.get("pca_data", []))

        result = {
            "success": True,
            "algorithm": algorithm_name,
            "city": city,
            "cluster_count": output["cluster_count"],
            "noise_count": output["noise_count"],
            "total_records": len(output["labels"]),
            "labels": output["labels"],
            "pca": pca_coordinates,
            "pca_data": pca_coordinates,
            "cluster_summary": output["cluster_summary"],
            "cluster_profiles": output["cluster_profiles"],
            "features": output["features"],
            "evaluation": evaluation
        }

        return jsonify(make_json_safe(result))

    except ValueError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        app.logger.exception("Clustering failed")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------------------
# ERROR HANDLERS
# -----------------------------------------

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        "error": "Requested page or resource was not found."
    }), 404


# -----------------------------------------
# RUN APPLICATION
# -----------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
