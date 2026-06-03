import streamlit as st

st.set_page_config(
    page_title="Podewils' Vermächtnis",
    page_icon="🏰"
)

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
    elif geschlecht == "männlich":
        return maennlich
    else:
        return neutral


def waechter_text(text):
    st.markdown(f"> {text}")


def gehe_zu(seite):
    st.session_state.seite = seite
    st.rerun()


defaults = {
    "seite": "start",
    "name": "",
    "titel": "",
    "entscheidung_1": "",
    "entscheidung_2": "",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


st.title("PODEWILS' VERMÄCHTNIS")
st.subheader("Das Urteil des Wächters")
st.divider()


# START

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
            gehe_zu("mausoleum")


# STATION 1

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

    st.number_input("1. Wie viele sichtbare Särge erkennst du?", min_value=0, max_value=20, step=1)
    st.number_input("2. Wie viele dieser Särge tragen ein rundovales Ornament?", min_value=0, max_value=20, step=1)
    st.number_input("3. Wie viele Kinder hatte Heinrich Graf von Podewils laut Infotafel?", min_value=0, max_value=20, step=1)

    st.info("Für diesen Test wird jede Eingabe akzeptiert. Die richtigen Zahlen tragen wir später ein.")

    if st.button("Antworten prüfen"):
        gehe_zu("entscheidung_1")


# ENTSCHEIDUNG 1

elif st.session_state.seite == "entscheidung_1":

    name = st.session_state.name
    titel = st.session_state.titel

    st.header("Die erste Frage des Wächters")

    st.success("Akzeptabel.")
    waechter_text(f"Du hast hingesehen, {name} {titel}.")
    waechter_text("Die meisten Menschen laufen an Erinnerungen vorbei, ohne sie zu bemerken.")

    st.divider()

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
        gehe_zu("urteil_1")


# URTEIL 1

elif st.session_state.seite == "urteil_1":

    entscheidung = st.session_state.entscheidung_1

    st.header("Urteil des Wächters")

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

    if st.button("Weiter zur Säule"):
        gehe_zu("saeule")


# STATION 2

elif st.session_state.seite == "saeule":

    st.header("Station 2 – Die Säule")
    st.subheader("Was hält ein Dorf zusammen?")

    waechter_text("Vier Kräfte tragen jedes Dorf.")
    waechter_text("Wer sie vergisst, verwaltet irgendwann nur noch Ruinen.")

    st.divider()

    st.subheader("Beobachtungsaufgabe")

    st.write("Welche Symbole erkennst du tatsächlich auf der Säule?")
    st.caption("Mehrfachauswahl möglich – der Wächter mag Genauigkeit.")

    symbole = st.multiselect(
        "Wähle alle erkennbaren Symbole aus:",
        [
            "Amboss mit Werkzeug",
            "Äskulapstab",
            "Pflug",
            "Kanne",
            "Fisch",
            "Turm"
        ]
    )

    richtige_symbole = {
        "Amboss mit Werkzeug",
        "Äskulapstab",
        "Pflug",
        "Kanne"
    }

    if st.button("Symbole prüfen"):

        auswahl = set(symbole)

        if auswahl == richtige_symbole:
            gehe_zu("entscheidung_2")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter_text("Interessant.")
            waechter_text("Entweder blickst du kreativ auf Symbolik – oder deine Beobachtungsgabe macht gerade Urlaub.")
            waechter_text("Podewils hätte dich gebeten, das noch einmal zu prüfen.")
            waechter_text("Schau genauer hin.")


# ENTSCHEIDUNG 2

elif st.session_state.seite == "entscheidung_2":

    st.header("Die zweite Frage des Wächters")

    st.success("Akzeptabel.")
    waechter_text("Du erkennst zumindest die Grundlagen funktionierender Dorfverwaltung.")

    st.divider()

    st.subheader("Der Wächter erklärt")

    waechter_text("Der Pflug steht für Nahrung.")
    waechter_text("Der Äskulapstab für Gesundheit.")
    waechter_text("Der Amboss für Arbeit.")
    waechter_text("Die Kanne für Gemeinschaft.")
    waechter_text("Und über allem sitzt der Vogel.")
    waechter_text("Ob er beobachtet oder urteilt, darüber streiten sich die Geschichten.")

    st.divider()

    waechter_text("Fredersdorf gerät in eine Krise.")
    waechter_text("Was schützt du zuerst?")

    entscheidung = st.radio(
        "Wähle deine Antwort:",
        [
            "Nahrung",
            "Gesundheit",
            "Arbeit",
            "Gemeinschaft"
        ]
    )

    if st.button("Antwort registrieren"):
        st.session_state.entscheidung_2 = entscheidung
        gehe_zu("urteil_2")


# URTEIL 2

elif st.session_state.seite == "urteil_2":

    name = st.session_state.name
    titel = st.session_state.titel
    entscheidung_1 = st.session_state.entscheidung_1
    entscheidung_2 = st.session_state.entscheidung_2

    st.header("Urteil des Wächters")

    if entscheidung_2 == "Nahrung":
        waechter_text("Pragmatisch.")
        waechter_text("Hungrige Menschen diskutieren schlecht.")

    elif entscheidung_2 == "Gesundheit":
        waechter_text("Mitgefühl.")
        waechter_text("Riskant – aber ehrenhaft.")

    elif entscheidung_2 == "Arbeit":
        waechter_text("Verdächtig preußisch.")
        waechter_text("Beeindruckend effizient.")

    elif entscheidung_2 == "Gemeinschaft":
        waechter_text("Überraschend vernünftig.")

    st.divider()

    st.subheader("Persönliche Einordnung")

    if entscheidung_1 == "Geschichten" and entscheidung_2 == "Gemeinschaft":
        waechter_text(f"Der Wächter hält dich für erstaunlich menschlich, {name} {titel}.")

    elif entscheidung_1 == "Ordnung" and entscheidung_2 == "Arbeit":
        waechter_text(f"Der Wächter vermutet Verwaltungserfahrung, {name} {titel}.")

    elif entscheidung_1 == "Wahrheit" and entscheidung_2 == "Gesundheit":
        waechter_text("Idealistisch.")
        waechter_text("Das endet nicht immer gut.")

    elif entscheidung_1 == "Die letzte Dorfkneipe" and entscheidung_2 == "Gemeinschaft":
        waechter_text("Der Wächter erkennt ein ausgeprägtes Verständnis für soziale Infrastruktur.")

    elif entscheidung_1 == "Das Freudenhaus":
        waechter_text("Der Wächter notiert: moralisch interessant, historisch schwer einzuordnen.")

    else:
        waechter_text("Der Wächter notiert deine Entscheidungen.")
        waechter_text("Noch ist unklar, ob das beruhigend ist.")

    st.divider()

    waechter_text(f"Der Vogel hat dich beobachtet, {name} {titel}.")
    waechter_text("Vorläufig fällt das Urteil akzeptabel aus.")
    waechter_text("Der Wächter gewährt dir den nächsten Ort.")

    st.subheader("Koordinate zur Brücke")
    st.success("N 52° 30.851'")
    st.success("E 13° 45.001'")

    if st.button("Weiter zur Brücke"):
        gehe_zu("bruecke")


# STATION 3 PLATZHALTER

elif st.session_state.seite == "bruecke":

    st.header("Station 3 – Die Brücke")
    st.write("Diese Station bauen wir in Version 4 ein.")

    st.info("Bis hierhin funktioniert Version 3.1.")
