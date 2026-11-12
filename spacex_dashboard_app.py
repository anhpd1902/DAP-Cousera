"""Simple exploratory dashboard for historical SpaceX sample. Run: python spacex_dashboard_app.py"""
from pathlib import Path
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
df=pd.read_csv(Path(__file__).with_name("spacex_sample_90_reconstructed.csv"))
app=Dash(__name__)
app.layout=html.Div([
    html.H1("SpaceX Falcon 9 Launch Analysis"),
    dcc.Dropdown(id="metric",options=[
      {"label":"Launches by year","value":"year"},
      {"label":"Landing success by site","value":"site"},
      {"label":"Payload vs outcome","value":"payload"}],value="year",clearable=False),
    dcc.Graph(id="chart"),
    html.P("Historical educational reproduction; data are not live SpaceX mission records.")
])
@app.callback(Output("chart","figure"),Input("metric","value"))
def update_chart(metric):
    if metric=="site":
        sub=df.groupby("LaunchSite",as_index=False)["Class"].mean()
        return px.bar(sub,x="LaunchSite",y="Class",title="Landing success fraction by launch site")
    if metric=="payload":
        return px.scatter(df,x="PayloadMass_kg",y="FlightNumber",color="Class",
              title="Payload mass, flight number and landing outcome")
    sub=df.groupby("Year",as_index=False)["Class"].agg(["count","mean"]).reset_index()
    return px.line(sub,x="Year",y="mean",markers=True,title="Landing success fraction by year")
if __name__=="__main__":
    app.run(debug=False,port=8050)
