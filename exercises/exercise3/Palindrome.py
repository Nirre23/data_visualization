from taipy.gui import Gui
import taipy.gui.builder as tgb

# Variabler för användarinput, resultat och poäng
user_input = ""
result_text = ""
score = 0
is_palindrome = tgb.image("https://raw.githubusercontent.com/kokchun/assets/refs/heads/main/data_visualization/fake_cat.png")  # Bild för felaktiga svar
not_palindrome = tgb.image("fake_sad_rabbit.jpg")  # Bild för korrekta svar

# Funktion för att kontrollera om strängen är ett palindrom
def is_palindrome_func(text):
    cleaned = text.replace(" ", "").lower()  # Ta bort mellanslag och gör allt till små bokstäver
    return cleaned == cleaned[::-1]  # Jämför texten med sig själv baklänges

# Funktion som körs när användaren trycker på Submit-knappen
def submit(state):
    global score
    if is_palindrome_func(state.user_input):
        state.result_text = f"✅ '{state.user_input}' är ett palindrom!"
        state.image_path = is_palindrome
        score += 1  # Öka poängen för ett korrekt svar
    else:
        state.result_text = f"❌ '{state.user_input}' är inte ett palindrom."
        state.image_path = not_palindrome
        score -= 1  # Minska poängen för ett felaktigt svar
    state.score = f"Poäng: {score}"  # Uppdatera poängen på sidan

# Bygg själva Taipy-sidan
with tgb.Page() as page:
    tgb.text("# Palindrome Game", mode="md")
    tgb.text("Skriv in en text för att kolla om det är ett palindrom:", mode="md")
    
    # Inputfält för användaren att skriva in en sträng
    tgb.input("{user_input}")
    
    # Visar strängen användaren skriver
    tgb.text("Du skrev: {user_input}")
    
    # Knapp för att skicka in strängen och kontrollera om den är ett palindrom
    tgb.button(label="Submit", class_name="plain", on_action=submit)
    
    # Visar resultatet om strängen är ett palindrom eller inte
    tgb.text("{result_text}")
    
    # Visar rätt bild baserat på om det är ett palindrom eller inte
  
    
    # Visar poäng
    tgb.text("{score}")

# Kör spelet
if __name__ == '__main__':
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)
