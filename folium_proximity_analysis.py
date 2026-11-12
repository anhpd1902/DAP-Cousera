"""SpaceX capstone Folium distance exercise - sample reference points only."""
from pathlib import Path
from math import radians, sin, cos, sqrt, asin
import pandas as pd
import folium
from folium.plugins import MarkerCluster
DATA = pd.read_csv(Path(__file__).with_name("spacex_sample_90_reconstructed.csv"))
SITES = {"CCAFS SLC 40":(28.563197,-80.576820),
         "KSC LC 39A":(28.573255,-80.646895),
         "VAFB SLC 4E":(34.632834,-120.610746)}
SITE = SITES["CCAFS SLC 40"]
POIS = {"Coastline":(28.56409,-80.56806),
        "Highway":(28.56385,-80.57088),
        "Railway":(28.57217,-80.58528),
        "City (Melbourne point)":(28.10469,-80.64784)}
def haversine_km(p,q):
    lat1,lon1,lat2,lon2=map(radians,(*p,*q))
    dlat,dlon=lat2-lat1,lon2-lon1
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return 2*6371*asin(sqrt(a))
def create_map(output="SpaceX_Folium_Proximity_Analysis.html"):
    m=folium.Map(location=SITE,zoom_start=10,tiles="OpenStreetMap")
    for name,coords in SITES.items():
        data=DATA[DATA.LaunchSite==name]
        folium.CircleMarker(coords,radius=10,color="navy",fill=True,
            popup=f"{name}: {int(data.Class.sum())}/{len(data)} successful").add_to(m)
    for name,coords in POIS.items():
        km=haversine_km(SITE,coords)
        folium.Marker(coords,tooltip=f"{name}: {km:.2f} km").add_to(m)
        folium.PolyLine([SITE,coords],tooltip=f"{km:.2f} km",weight=3).add_to(m)
    m.save(output)
    return output
if __name__=="__main__":
    print(create_map())
    for name,coords in POIS.items():
        print(f"{name}: {haversine_km(SITE,coords):.3f} km (straight line)")
