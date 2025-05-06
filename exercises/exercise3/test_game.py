from taipy.gui import Gui
import taipy.gui.builder as tgb

# Initiala variabler
user_input = ""
result_text = ""
image_path = ""
score = 0

# Bild-URL: du kan även använda lokala bilder i din assets-mapp
palindrome_image_local = "fake_cat.png"
not_palindrome_image_local = "fake_sad_rabbit.png"

# Palindromkontroll
def is_palindrome_func(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# När man klickar på knappen
def submit(state):
    if not hasattr(state, "score"):
        state.score = 0

    if is_palindrome_func(state.user_input):
        state.result_text = f"✅ '{state.user_input}' är ett palindrom!"
        state.image_path = palindrome_image_local
        state.score += 1
    else:
        state.result_text = f"❌ '{state.user_input}' är inte ett palindrom."
        state.image_path = not_palindrome_image_local
        state.score -= 1

# Sidan
with tgb.Page() as page:
    tgb.text("# 🧠 Palindromspelet", mode="md")
    tgb.text("Skriv en text och tryck på knappen:", mode="md")

    with tgb.layout(columns="1 1"):  # Två kolumner
        with tgb.part():  # Vänster kolumn
            tgb.input("{user_input}")
            tgb.text("Du skrev: **{user_input}**", mode="md")
            tgb.button(label="Kontrollera", class_name="plain", on_action=submit)
            tgb.text("{result_text}", mode="md")
            tgb.text("⭐ Poäng: {score}", mode="md")

        with tgb.part():  # Höger kolumn
            tgb.image("{image_path}",width="200px")
            

# Starta
if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)
