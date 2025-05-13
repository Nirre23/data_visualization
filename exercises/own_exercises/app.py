import taipy.gui.builder as tgb
from taipy import Gui
import plotly.express as px
import pandas as pd 


df = pd.read_csv("../data/pokemon.csv")
print(df)