import taipy.gui.builder as tgb
from taipy.gui import Gui


selected = "Data/IT"
slider_value = 10
message = "Välj dina inställningar"
show_tip = True
user_note = ""


def update_message(state):
    state.message = f"Du valde {state.selected} och {state.slider_value} som värde!"
    if state.user_note:
        state.message += f" (Anteckning: {state.user_note})"
    
with tgb.Page() as page:
    with tgb.part(class_name="container card stack large"):
        tgb.text("## Min interaktiva dashboard",mode="md",class_name="custom-title")
        
    with tgb.part(class_name="container card stack-large"):
        with tgb.layout(columns="2 1"):
            with tgb.part():  # Innehåll
                tgb.text("Välj utbildningsområde", mode="md")    
                tgb.selector("{selected}", lov=["Data/IT", "Hälsa", "Teknik", "Ekonomi"], dropdown=True)

                tgb.text("Justera värdet", mode="md")
                tgb.slider("{slider_value}", min=1, max=90, step=1, continuous=False, class_name="slider")

                tgb.button("Uppdatera meddelande", on_action=update_message, class_name="button")    
                tgb.text("{message}", mode="md")

            with tgb.part():  # Bild
                tgb.image("https://careers.dwp.gov.uk/wp-content/uploads/2022/11/Data-header.jpg?x30338", width="100%",height="400%")

        if show_tip:
            with tgb.part(class_name="container card"):
                tgb.text("💡 **Tips:** Du kan kombinera flera UI-element för att skapa mer avancerade dashboards.", mode="md")   
        
if __name__ =='__main__':
    Gui(page,css_file="style.css").run(dark_mode=False,use_reloader=True)        
        