#!/bin/bash

echo "[∞] Starting Research Writer pipeline…"

# go to project root
cd "$(dirname "$0")"

# make sure all carts are executable
find . -type f -name "cart*.py" -exec chmod +x {} \;

echo "[∞] Stage 1 — import & dictionary…"
./cart201_import_search_terms.py
./cart202_import_equations.py
./cart203_import_websites.py
./cart204_master_dictionary.py

echo "[∞] Stage 2 — fusion engines…"
./cart205_pair_fusion.py
./cart206_trio_fusion.py
./cart207_quad_fusion.py
./cart208_omni_fusion.py
./cart209_cross_domain_engine.py

echo "[∞] Stage 3 — vectorizers…"
./cart220_scientific_vectorizer.py
./cart221_historical_context_vectorizer.py
./cart222_material_science_vectorizer.py
./cart223_geometry_expansion_engine.py
./cart224_scifi_science_mapper.py
./cart225_equation_domain_mapper.py
./cart226_entropy_scorer.py
./cart227_semantic_graph_builder.py
./cart228_crossover_weight_calibrator.py
./cart229_infinity_seed_generator.py

echo "[∞] Stage 4 — research writers…"
./cart301_ruo_summarizer.py
./cart302_research_threader.py
./cart303_research_weaver.py
./cart304_short_paper_writer.py
./cart305_long_paper_writer.py
./cart320_infinity_vector_writer.py
./cart330_full_research_bundle_writer.py

echo "[∞] Stage 5 — compile & feed…"
./cart813_research_compiler.py
./cart351_link_feed.py
./cart352_term_feed.py
./cart353_equation_feed.py
./cart804_feed_generator.py

echo "[∞] Research Writer pipeline finished."
echo "[∞] Check CART804_FEED_BUFFER.json and related output files."
