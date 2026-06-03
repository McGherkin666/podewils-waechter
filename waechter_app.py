import streamlit as st

st.set_page_config(
    page_title="Podewils' Vermächtnis",
    page_icon="🏰"
)

# -----------------------------
# Hilfsfunktionen
# -----------------------------

def titel_bilden(geschlecht, eigenschaft):
    formen = {
        "wachsam": ("die Wachsame", "der Wachsame", "wachsam"),
        "neugierig": ("die Neugierige", "der Neugierige", "neugierig"),
        "beharrlich": ("die Beharrliche", "der Beharrliche", "beharrlich"),
        "besonnen": ("die Besonnene", "der Besonnene", "besonnen"),
        "mutig": ("die Mutige", "der Mutige", "mutig"),
        "skeptisch": ("die Skeptische", "der Skeptische", "skeptisch"),
        "aufmerksam": ("die Aufmerksame", "der Aufmerksame", "aufmerksam"),
        "abenteuerlustig": ("die Abenteuerlustige", "der Abenteuerlustige", "abenteuerlustig"),
        "gesprächsbereit": ("die Gesprächsbereite", "der Gesprächsbereite", "gesprächsbereit"),
        "optimistisch": ("die Optimistische", "der Optimistische", "optimistisch"),
        "vertrauensselig": ("die Vertrauensselige", "der Vertrauensselige", "vertrauensselig"),
        "naiv": ("die Naive", "der Naive", "naiv"),
        "eigenwillig": ("die Eigenwillige", "der Eigenwillige", "eigenwillig"),
        "impulsiv": ("die Impulsive", "der Impulsive", "impulsiv"),
        "treuherzig": ("die Treuherzige", "der Treuherzige", "treuherzig"),
    }

    weiblich, maennlich, neutral = formen[eigenschaft]

    if geschlecht == "weiblich":
        return weiblich
    if geschlecht == "männlich":
        return maennlich
    return neutral


def waechter_text(text):
    st.markdown(f"> {text}")


# -----------------------------
# Session State
# -----------------------------

if "seite" not in st.session_state:
    st.session_state.seite = "start"

if "name" not in st.session_state:
    st.session_state.name = ""

if "titel" not in st.session_state:
    st.session_state.titel = ""

if "entscheidung_1" not in st.session_state:
    st.session_state.entscheidung_1 = ""


# -----------------------------
# Kopf
# -----------------------------

st.title("PODEWILS' VERMÄCHTNIS")
st.subheader("Das Urteil des Wächters")

st.divider()


# -----------------------------
# STARTSEITE
# -----------------------------

if st.session_state.seite == "start":

    st.header("QR-Code gescannt")

    waechter_text("Willkommen.")
    waechter_text("Seit Jahrhunderten beobachte ich Fredersdorf.")
    waechter_text("Heute beobachte ich dich.")
    waechter_text("Doch bevor die Prüfung beginnt, möchte ich wissen, wen ich beurteilen werde.")

    st.subheader("Die Aufzeichnungen des Wächters")

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

    if st.button("Prüfung beginnen"):
        if not name.strip():
            st.error("Der Wächter verlangt einen Namen.")
        else:
            st.session_state.name = name.strip()
            st.session_state.titel = titel_bilden(geschlecht, eigenschaft)
            st.session_state.seite = "mausoleum"
            st.rerun()


# -----------------------------
# STATION 1 – MAUSOLEUM
# -----------------------------

elif st.session_state.seite == "mausoleum":

    name = st.session_state.name
    titel = st.session_state.titel

    st.header("Station 1 – Das Mausoleum")
    st.subheader("Die Wächter der Erinnerung")

    waechter_text(f"Willkommen, {name} {titel}.")
    waechter_text("Ein Dorf vergisst schneller, als es zugibt.")
    waechter_text("Bevor du urteilst, solltest du lernen hinzusehen.")

    st.divider()

    st.subheader("Beobachtungsaufgaben")

    saerge = st.number_input(
        "1. Wie viele sichtbare Särge erkennst du?",
        min_value=0,
        max_value=20,
        step=1
    )

    ornamente = st.number_input(
        "2. Wie viele dieser Särge tragen ein rundovales Ornament?",
        min_value=0,
        max_value=20,
        step=1
    )

    kinder = st.number_input(
        "3. Wie viele Kinder hatte Heinrich Graf von Podewils laut Infotafel?",
        min_value=0,
        max_value=20,
        step=1
    )

    st.info("Die richtigen Zahlen tragen wir später noch fest im Code ein. Für diesen Test gilt: Jede Eingabe wird akzeptiert.")

    if st.button("Antworten prüfen"):

        st.success("Akzeptabel.")

        waechter_text(f"Du hast hingesehen, {name} {titel}.")
        waechter_text("Die meisten Menschen laufen an Erinnerungen vorbei, ohne sie zu bemerken.")

        st.session_state.seite = "entscheidung_1"
        st.rerun()


# -----------------------------
# ENTSCHEIDUNG 1
# -----------------------------

elif st.session_state.seite == "entscheidung_1":

    name = st.session_state.name
    titel = st.session_state.titel

    st.header("Die erste Frage des Wächters")

    waechter_text("Menschen glauben oft, dass Mauern, Besitz oder Ordnung ein Dorf zusammenhalten.")
    waechter_text("Sie irren sich erstaunlich häufig.")
    waechter_text("Wenn Fredersdorf eines Tages in eine Krise gerät – was darf niemals verloren gehen?")

    entscheidung = st.radio(
        "Wähle deine Antwort:",
        [
            "Ordnung",
            "Geschichten",
            "Wahrheit",
            "Tradition",
            "Die letzte Dorfkneipe",
            "Das Freudenhaus"
        ]
    )

    if st.button("Antwort registrieren"):

        st.session_state.entscheidung_1 = entscheidung

        st.subheader("Urteil des Wächters")

        if entscheidung == "Ordnung":
            waechter_text("Preußisch. Berechenbar.")
            waechter_text("Nicht besonders spannend – aber Dörfer sind selten an zu viel Ordnung zugrunde gegangen.")

        elif entscheidung == "Geschichten":
            waechter_text("Interessant.")
            waechter_text("Menschen nennen Erinnerungen gern Wahrheit.")
            waechter_text("Meist sind sie nur besser erzählt.")

        elif entscheidung == "Wahrheit":
            waechter_text("Mutig.")
            waechter_text("Oder naiv.")
            waechter_text("Wahrheit macht selten beliebt und noch seltener bequem.")

        elif entscheidung == "Tradition":
            waechter_text("Menschen halten erstaunlich lange an Dingen fest.")
            waechter_text("Selbst dann, wenn niemand mehr weiß, warum.")

        elif entscheidung == "Die letzte Dorfkneipe":
            waechter_text("Endlich Ehrlichkeit.")
            waechter_text("Gesellschaftlicher Zusammenhalt entsteht selten nüchtern.")
            waechter_text("Podewils hätte widersprochen.")
            waechter_text("Vermutlich mit einem Glas in der Hand.")

        elif entscheidung == "Das Freudenhaus":
            waechter_text("Bemerkenswert offen.")
            waechter_text("Historisch schwer zu verteidigen.")
            waechter_text("Menschlich allerdings nicht völlig unverständlich.")

        st.success("Antwort registriert.")

        waechter_text("Der Wächter gewährt dir den nächsten Ort.")

        st.subheader("Koordinate zur Säule")
        st.warning("Koordinate zur Säule wird hier später eingetragen.")

        if st.button("Weiter zur Station 2"):
            st.session_state.seite = "saeule"
            st.rerun()


# -----------------------------
# PLATZHALTER STATION 2
# -----------------------------

elif st.session_state.seite == "saeule":

    st.header("Station 2 – Die Säule")
    st.write("Diese Station bauen wir in Version 3 ein.")

    st.info("Bis hierhin funktioniert Version 2.")
