from flask import Blueprint, jsonify
from map_engine import generate_world_map

map_api = Blueprint("map_api", __name__)

WORLD_MAP = generate_world_map()


@map_api.route("/api/map")
def api_map():
    return jsonify({"regions": WORLD_MAP})
