import taipy.gui.builder as tgb
from taipy.gui import Gui
from pandas import DataFrame
import numpy as np

# Globala variabler
dice_count = 10
throw_count = 30001
hist_data = {"value": [], "count": [], "variable": []}
theoretical_mean = 3.5
calculated_mean = 0.0
difference = 0.
rows_per_page = 10

    # Funktionen måste definieras INNAN den används
def simulate(state):
        throws = np.random.randint(1, 7, size=(state.throw_count, state.dice_count))
        data = {f"Dice {i+1}": throws[:, i] for i in range(state.dice_count)}
        data["Throw"] = list(range(state.throw_count))
        state.df = DataFrame(data)  # Uppdatera DataFrame med simuleringens resultat

        means = throws.mean(axis=1)
        state.calculated_mean = round(means.mean(), 3)
        state.difference = round(abs(state.theoretical_mean - state.calculated_mean), 3)

        unique_means, counts = np.unique(np.round(means, 1), return_counts=True)
        state.hist_data = {
            "value": unique_means.tolist(),
            "count": counts.tolist(),
            "variable": [0] * len(unique_means)
        }



with tgb.Page() as page:
        with tgb.part(class_name="container card", style="max-width: 1200px; margin: 0 auto 30px auto; padding: 20px;"):
            tgb.text("# Dices simulations", mode="md")
            
            with tgb.part(class_name="container", style="max-width: 1200px; margin: 0 auto;"):
                with tgb.layout(columns="1 1", gap="20px"):
                    with tgb.part(class_name="container card", style="padding: 20px; background-color:#b3e5fc !important;,width:100%"):
                        tgb.selector("{rows_per_page}", values=[10, 25, 50, 100])
                        df = DataFrame(columns=["Throw"] + [f"Dice {i+1}" for i in range(dice_count)])
                        
                        tgb.table("{df}",style= "width:100%,table-layout:fixed")  # Se till att tabellen refererar till korrekt state.df
                        tgb.text("Number of dices chosen {dice_count}")
                        tgb.slider("{dice_count}", min=1, max=10)
                        tgb.text("Number of throws {throw_count}")
                        tgb.slider("{throw_count}", min=1, max=100000)
                        tgb.button("SIMULATE", on_action=simulate,class_name="plain")

                    with tgb.part(class_name="container card", style="padding: 20px; background-color:#b3e5fc !important;"):
                        with tgb.layout(columns="1 1 1", gap="10px", style="margin-bottom: 20px;"):
                            with tgb.part(class_name="container card", style="padding: 10px; text-align: center; background-color:#b3e5fc !important;"):
                                tgb.text("Theoretical mean {theoretical_mean}")
                                
                            with tgb.part(class_name="container card", style="padding: 10px; text-align: center; background-color:#b3e5fc !important;"):
                                tgb.text("Calculated mean {calculated_mean}")
                                
                            with tgb.part(class_name="container card", style="padding: 10px; text-align: center; background-color:#b3e5fc !important;"):
                                tgb.text("Difference {difference}")

                        tgb.text("Mean value of {dice_count} dices for {throw_count} throws")
                        tgb.chart("{hist_data}", type="bar", x="value", y="count", color="blue")
                        tgb.text("This histogram has been calculated through taking mean values for each throw")

Gui(page).run(dark_mode=False,use_reloader=True)
