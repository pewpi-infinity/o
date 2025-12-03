#!/usr/bin/env python3
# CART353 — 250 Equation Feed
import json

OUTPUT = "CART353_EQUATION_FEED.json"

eq = [
    "E = mc^2",
    "F = ma",
    "V = IR",
    "P = IV",
    "λ = h/p",
    "a^2 + b^2 = c^2",
    "∇⋅E = ρ/ε₀",
    "∇×E = -∂B/∂t",
    "∇⋅B = 0",
    "∇×B = μ₀J + μ₀ε₀ ∂E/∂t",
    "ψ(x,t) = Ae^{i(px-Et)/ħ}",
    "σ = F/A",
    "PV = nRT",
    "Q = mcΔT",
    "I = dq/dt",
    "ω = 2πf",
    "C = Q/V",
    "Z = R + iX",
    "Δx ≥ ħ/(2Δp)",
    "H = T + V",
    "S = k ln Ω",
    "c = λf",
    "τ = r × F",
    "∮E⋅dl = -dΦB/dt",
    # … continue up to 250 …
]

while len(eq) < 250:
    eq.append(f"gen_equation_{len(eq)} = placeholder")

with open(OUTPUT, "w") as f:
    json.dump(eq, f, indent=4)

print("[CART353] equation feed generated →", OUTPUT)
