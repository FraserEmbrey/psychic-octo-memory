#!/usr/bin/env python3
"""
weather_haiku.py
Local weather → tiny haiku. Uses Open-Meteo (free, no API key).
Usage:
  python weather_haiku.py "Brighton"
  python weather_haiku.py      # will prompt for a city
"""

import sys
import json
import random
import urllib.parse
import urllib.request
from datetime import datetime

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# WMO weather codes → coarse condition buckets
WMO_BUCKETS = {
    "clear": [0],
    "mainly_clear": [1],
    "partly_cloudy": [2],
    "overcast": [3],
    "fog": [45, 48],
    "drizzle": [51, 53, 55, 56, 57],
    "rain": [61, 63, 65, 66, 67, 80, 81, 82],
    "snow": [71, 73, 75, 77, 85, 86],
    "thunder": [95, 96, 99],
}

BUCKET_BY_CODE = {code: name for name, codes in WMO_BUCKETS.items() for code in codes}

# Haiku templates per bucket. Keep it simple, vibe first, syllables… close enough.
TEMPLATES = {
    "clear": [
        ("quiet blue morning",
         "sun stains the roofs with honey",
         "air tastes like new plans"),
        ("glass-hard kind of light",
         "shadows keep their sharp secrets",
         "day hums, low and bright"),
    ],
    "mainly_clear": [
        ("clouds loiter politely",
         "sun negotiates the sky",
         "we call it good luck"),
    ],
    "partly_cloudy": [
        ("patchwork sky above",
         "gulls edit the margins wide",
         "breeze flips the city"),
    ],
    "overcast": [
        ("grey writes a soft rule",
         "streets rehearse their quiet lines",
         "patience tastes like tea"),
    ],
    "fog": [
        ("world reduced to breath",
         "footsteps invent their own maps",
         "ghosts mind their business"),
    ],
    "drizzle": [
        ("thin rain, kind of kind",
         "a coat learns small arithmetic",
         "drop after small drop"),
    ],
    "rain": [
        ("rain drums out the beat",
         "puddles audition for sky",
         "windows do the rest"),
        ("gutters talk in code",
         "city rinsed of yesterday",
         "plans bloom, slightly damp"),
    ],
    "snow": [
        ("silence hires the air",
         "angles soften, rules relax",
         "footprints sign the page"),
    ],
    "thunder": [
        ("sky clears its throat twice",
         "lightning underlines a point",
         "every dog agrees"),
    ],
    "default": [
        ("weather plays coy cards",
         "somewhere a forecast guesses",
         "we live in between"),
    ],
}

def http_get_json(url: str, params: dict) -> dict:
    query = urllib.parse.urlencode(params)
    full = f"{url}?{query}"
    with urllib.request.urlopen(full, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))

def geocode_city(name: str):
    data = http_get_json(GEOCODE_URL, {"name": name, "count": 1})
    results = data.get("results") or []
    if not results:
        return None
    r = results[0]
    return {
        "name": r.get("name"),
        "country": r.get("country"),
        "lat": r["latitude"],
        "lon": r["longitude"],
        "tz": r.get("timezone", "UTC"),
    }

def fetch_current_weather(lat: float, lon: float, tz: str):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,weather_code,wind_speed_10m,precipitation",
        "timezone": tz,
    }
    data = http_get_json(FORECAST_URL, params)
    cur = data.get("current") or {}
    return {
        "temperature": cur.get("temperature_2m"),
        "weather_code": cur.get("weather_code"),
        "wind_speed": cur.get("wind_speed_10m"),
        "precipitation": cur.get("precipitation"),
        "time": cur.get("time"),
    }

def bucket_for(code: int) -> str:
    return BUCKET_BY_CODE.get(code, "default")

def pick_template(bucket: str):
    options = TEMPLATES.get(bucket) or TEMPLATES["default"]
    return random.choice(options)

def decorate(title: str) -> str:
    bar = "─" * len(title)
    return f"{title}\n{bar}"

def main():
    if len(sys.argv) >= 2:
        city = " ".join(sys.argv[1:]).strip()
    else:
        city = input("City name: ").strip()

    if not city:
        print("Give me literally any city. Your street. A vibe. Something.")
        sys.exit(1)

    place = geocode_city(city)
    if not place:
        print(f"Could not find ‘{city}’. Try a bigger place or proper spelling.")
        sys.exit(2)

    wx = fetch_current_weather(place["lat"], place["lon"], place["tz"])
    code = wx["weather_code"]
    bucket = bucket_for(code if code is not None else -1)
    line1, line2, line3 = pick_template(bucket)

    # Tiny status line
    temp = wx["temperature"]
    wind = wx["wind_speed"]
    when = wx["time"]
    nice_time = datetime.fromisoformat(when).strftime("%Y-%m-%d %H:%M") if when else "now"

    header = decorate(f"Haiku for {place['name']}, {place['country']} — {nice_time} ({place['tz']})")
    status = f"• {bucket.replace('_',' ')} | {temp}°C | wind {wind} m/s"

    print(header)
    print(status)
    print()
    print(line1)
    print(line2)
    print(line3)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Even the poem rolled its eyes.")