#!/usr/bin/env python3
import json, os

VEC_FILE     = "C13B0_USER_VECTOR.json"
COLOR_FILE   = "C13B0_TONE_COLOR_MAP.json"
OUT_FILE     = "C13B0_BIAS_COLOR_MAP.json"

HYDROGEN_TERMS = [
    "hydrogen","deuterium","tritium","protium","isotope","quantum hydrogen",
    "rydberg","spectral","frequency","maser","fusion","plasma","ion","electron",
    "proton","neutron","spin","spintronics","bond","enthalpy","entropy"
]

ELEMENTS = [
    "helium","lithium","beryllium","boron","carbon","nitrogen","oxygen",
    "fluorine","neon","sodium","magnesium","aluminum","silicon","phosphorus",
    "sulfur","chlorine","argon","potassium","calcium","titanium","vanadium",
    "chromium","manganese","iron","cobalt","nickel","copper","zinc","gallium",
    "germanium","arsenic","selenium","bromine","krypton","rubidium","strontium"
]

def load_json(p):
    return json.load(open(p)) if os.path.exists(p) else {}

print("[💜 CART G] Loading previous maps…")

user_vec   = load_json(VEC_FILE)
color_map  = load_json(COLOR_FILE)

print("[💜 CART G] Applying hydrogen bias weighting…")

for term in HYDROGEN_TERMS:
    if term in color_map:
        color_map[term] = "purple"
    else:
        color_map[term] = "purple"

print("[💜 CART G] Applying periodic element bias…")

for e in ELEMENTS:
    if e in color_map:
        # elements tend to move toward blue/yellow unless hydrogen-related
        if e in ["helium","lithium"]:
            color_map[e] = "purple"
        else:
            color_map[e] = "blue"
    else:
        color_map[e] = "blue"

print("[💜 CART G] Saving →", OUT_FILE)
json.dump(color_map, open(OUT_FILE,"w"), indent=2)

print("[💜 CART G] Done.")
