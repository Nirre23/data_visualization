import plotly.express as px
import taipy.gui.builder as tgb 
from taipy.gui import Gui
import plotly.graph_objects as go

# Data
df = px.data.gapminder()

# Init-variabler
gdppercap_top10 = []
gdp_chart_figure = go.Figure()

# Funktion för att filtrera
def filter_data(state):
    latest_year = df['year'].max()
    latest_df = df[df['year'] == latest_year]  
    
    # Top 10
    top_10 = latest_df.sort_values(by="gdpPercap", ascending=False).head(10)
    state.gdppercap_top10 = top_10[["country", "gdpPercap"]].reset_index(drop=True).to_dict('records')
    
    # Korrekt syntax: marker_color istället för marker
    state.gdp_chart_figure = go.Figure(data=[
        go.Bar(
            x=top_10["country"],
            y=top_10["gdpPercap"],
            marker_color="skyblue"
        )
    ])
    state.gdp_chart_figure.update_layout(
        title="Top 10 GDP per Capita",
        xaxis_title="Country",
        yaxis_title="GDP per Capita",
        template="plotly_white"
    )

# GUI-layout
with tgb.Page() as page:
    with tgb.part(class_name="container card stack-large"):
        tgb.text("# Top 10 countries by GDP per capita", mode="md")
        tgb.button("Show top 10", on_action=filter_data, class_name="plain")
        tgb.table("{gdppercap_top10}")
        tgb.chart(figure="{gdp_chart_figure}")  # <- rätta detta, ta bort type, x, y, color
    
# Starta GUI
Gui(page).run(dark_mode=True, use_reloader=True)
