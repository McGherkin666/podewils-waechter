import streamlit as st

st.set_page_config(
    page_title="Podewils' Vermächtnis",
    page_icon="🏰"
)

st.title("PODEWILS' VERMÄCHTNIS")
st.subheader("Die Prüfung des Wächters")

st.write(
    """
    Willkommen in Fredersdorf.

    Seit Jahrhunderten beobachtet der Wächter die Geschicke des Dorfes.

    Heute beobachtet er dich.
    """
)

name = st.text_input("Wie lautet dein Name?")

geschlecht = st.selectbox(
    "Geschlecht",
    ["weiblich", "männlich", "keine Angabe"]
)

eigenschaft = st.selectbox(
    "Welche Eigenschaft beschreibt dich am besten?",
    [
        "wachsam",
        "neugierig",
        "beharrlich",
        "besonnen",
        "mutig",
        "skeptisch",
        "aufmerksam",
        "abenteuerlustig",
        "gesprächsbereit",
        "optimistisch",
        "vertrauensselig",
        "naiv",
        "eigenwillig",
        "impulsiv",
        "treuherzig"
    ]
)

if name:

    if geschlecht == "weiblich":
        titel = f"die {eigenschaft.capitalize()}"
    elif geschlecht == "männlich":
        titel = f"der {eigenschaft.capitalize()}"
    else:
        titel = eigenschaft

    st.success(
        f"Willkommen, {name}. Der Wächter führt dich als {titel}."
    )
