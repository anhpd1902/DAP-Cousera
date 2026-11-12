# SpaceX Falcon 9 | IBM Applied Data Science Capstone

Public course-sample **independent reproduction** of SpaceX Falcon 9 first-stage landing analysis, created to accompany the IBM Data Science Capstone Project Report. This is not a claim of having executed the original API, scraping, or other labs on behalf of the course learner.

## Project and lab files

| Area | Files |
|---|---|
| Data inspection / preparation | [01_Data_Review_Wrangling.ipynb](01_Data_Review_Wrangling.ipynb) |
| EDA visualizations | [02_EDA_Visualization.ipynb](02_EDA_Visualization.ipynb) |
| SQL analysis | [03_EDA_SQL.ipynb](03_EDA_SQL.ipynb) |
| Folium launch sites and proximity | [04_Folium_Interactive_Map.ipynb](04_Folium_Interactive_Map.ipynb), [folium_proximity_analysis.py](folium_proximity_analysis.py) |
| Machine learning | [05_Machine_Learning.ipynb](05_Machine_Learning.ipynb), [train_models.py](train_models.py) |
| Dashboard | [spacex_dashboard_app.py](spacex_dashboard_app.py) |
| Input and summaries | [spacex_sample_90_reconstructed.csv](spacex_sample_90_reconstructed.csv), [folium_proximity_measurements.csv](folium_proximity_measurements.csv), [model_results.csv](model_results.csv) |

The final report references this repository: **https://github.com/anhpd1902/DAP-Cousera**.

## Reproducing locally

```bash
python -m pip install -r requirements.txt
jupyter lab
python folium_proximity_analysis.py
python train_models.py
python spacex_dashboard_app.py
```

## Method and caveats

- Historic course sample: 90 selected records, 2010–2020, reconstructed from public IBM material; **not live SpaceX data**.
- The map uses manually selected reference coordinates and Haversine/geodesic *straight-line* distances. It does not prove each point is the nearest road, rail, coast, or city boundary.
- Baseline classifier scores are illustrative course-sample reproductions, not deployed predictions.
- These notebooks cover data review, descriptive EDA, SQL, Folium, and ML. The original IBM API-collection and web-scraping lab deliverables are **not yet included**; do not claim full official-lab reproducibility until those are added and executed.

### Sources
- Public course example: https://raw.githubusercontent.com/itsskofficial/ibm-data-science-capstone/master/dataset_part_2.csv
- Lab map methodology: https://sentinel-1.github.io/IBM-Applied-Data-Science-Capstone/Interactive%20Visual%20Analytics%20with%20Folium%20lab/
