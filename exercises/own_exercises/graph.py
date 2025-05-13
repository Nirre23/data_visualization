import taipy.gui.builder as tgb
from taipy import Gui
import plotly.express as px

# Ladda gapminder-data
df = px.data.gapminder()
df_2007 = df[df['year'] == 2007]

# Skapa Plotly-graf
fig = px.scatter(
    df_2007,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=50,
    title="Livslängd vs BNP per capita 2007"
)

# Spara grafen som HTML-sträng
html_graph = fig.to_html(full_html=False)

# Skapa sidan korrekt
page = tgb.Page()

with page:
    with tgb.part(class_name="container card"):
        tgb.text("# Gapminder graf", mode="md")
        
        # Visa HTML-strängen direkt
        tgb.html(html_graph)

Gui(page).run(dark_mode=True, use_reloader=True)
