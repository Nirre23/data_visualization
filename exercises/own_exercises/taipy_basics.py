import taipy.gui.builder as tgb
from taipy import Gui
import plotly.express as px

initial_state = {
    "message": "",
    "name": "",
    "greeting": "",
    "selected_country": "",
    "population": "",
    "gdp": "",
    "life_expectancy": "",
    "dices": 10,
    "show_graph": False
}

def toggle_graph(state):
    state.show_graph = not state.show_graph


# Ladda Gapminder data
df = px.data.gapminder()

# Funktion för att visa information om landet
def show_info(state):
    selected_country = state.selected_country  # Hämta det valda landet från state
    country_data = df[df['country'] == selected_country].iloc[0]
    state.population = country_data['pop']
    state.gdp = country_data['gdpPercap']
    state.life_expectancy = country_data['lifeExp']

# Hämta unika länder från datasetet
countries = df['country'].unique()

# Funktion för att visa meddelandet
def show_message(state):
    state.message = "Knappen har klickats!"

# Hälsningsfunktion
def greet_user(state):
    state.greeting = f"Hej {state.name}!"

# Skapa sidan
with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        
        tgb.text("### Välkommen till Taipy", mode="md")
        
        tgb.button("Klicka här", on_action=show_message, class_name="plain")
        
        tgb.text("{message}", mode="md")
        
        tgb.text("# Hälsning", mode="md")
        
        tgb.input("{name}", label="Namn")
        
        tgb.button("Hälsa", on_action=greet_user,class_name="plain")
        
        tgb.text("{greeting}")
    
        tgb.text("# Välj ett land från Gapminder", mode="md")
        tgb.text("### Data från 1952-2007",mode="md")
        
        # Skapa en dropdown (selector) för att välja land
        tgb.selector(lov= df['country'].unique(),
                     label="Välj land",
                     value="{selected_country}",
                     dropdown=True)
        
        tgb.button("Visa info", on_action=show_info,class_name="plain")
        
        tgb.text("Befolkning: {population}")
        tgb.text("Gdp per capita: {gdp}")
        tgb.text("Livslängd: {life_expectancy}")
        
    with tgb.part(class_name="container card"):
        tgb.text("Välj antal tärningskast")
        tgb.slider(value="{dices}",min=1,max=10,step=1,labels="Antal tärningskast")
        tgb.text("Valt antal tärningskast: {dices}")
        


                        
                    
                
        

# Starta applikationen
Gui(page,**initial_state).run(dark_mode=True, use_reloader=True)
