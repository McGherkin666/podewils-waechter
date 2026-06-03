import streamlit as st

st.set_page_config(
    page_title="Podewils' Vermächtnis",
    page_icon="🦉",
    layout="centered"
)

# -----------------------------
# DESIGN
# -----------------------------

st.markdown("""
<style>
.stApp {
    background-color: #111111;
    color: #e8e0cf;
}

h1, h2, h3 {
    color: #c8a85a;
}

div.stButton > button {
    background-color: #8a6a2f;
    color: #fff5d6;
    border-radius: 8px;
    border: 1px solid #c8a85a;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #a88138;
    color: white;
}

.waechterbox {
    background-color: #1c1c1c;
    border-left: 5px solid #c8a85a;
    padding: 14px;
    margin: 10px 0;
    border-radius: 8px;
    color: #f1e7d0;
}

.koordinate {
    background-color: #202020;
    border: 1px solid #c8a85a;
    padding: 14px;
    border-radius: 8px;
    font-size: 1.2em;
    color: #f5df9b;
    text-align: center;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# HILFSFUNKTIONEN
# -----------------------------

def waechter_text(text):
    st.markdown(
        f"""
        <div class="waechterbox">
        🦉 <b>Der Wächter:</b><br>{text}
        </div>
        """,
        unsafe_allow_html=True
    )


def koordinate(nord, ost):
    st.markdown(
        f"""
        <div class="koordinate">
        {nord}<br>{ost}
        </div>
        """,
        unsafe_allow_html=True
    )


def gehe_zu(seite):
    st.session_state.seite = seite
    st.rerun()


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


# -----------------------------
# SESSION
# -----------------------------

defaults = {
    "seite": "start",
    "name": "",
    "titel": "",
    "entscheidung_1": "",
    "entscheidung_2": "",
    "entscheidung_3": "",
    "geraeusch": "",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# -----------------------------
# KOPF
# -----------------------------

try:
    st.image("Podewils.jpeg", use_container_width=True)
except Exception:
    st.warning("Titelbild fehlt noch. Bitte Datei 'Podewils.jpeg' in GitHub hochladen.")

st.title("PODEWILS' VERMÄCHTNIS")
st.subheader("Das Urteil des Wächters")
st.divider()


# -----------------------------
# START
# -----------------------------

if st.session_state.seite == "start":

    st.header("Die Aufzeichnungen des Wächters")

    waechter_text(
        "Willkommen. Seit Jahrhunderten beobachte ich Fredersdorf. "
        "Heute beobachte ich dich. Bevor die Prüfung beginnt, will ich wissen, wen ich beurteile."
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
            "treuherzig",
        ],
    )

    if st.button("Prüfung beginnen"):
        if not name.strip():
            st.error("Der Wächter verlangt einen Namen.")
        else:
            st.session_state.name = name.strip()
            st.session_state.titel = titel_bilden(geschlecht, eigenschaft)
            gehe_zu("mausoleum")


# -----------------------------
# MAUSOLEUM
# -----------------------------

elif st.session_state.seite == "mausoleum":

    name = st.session_state.name
    titel = st.session_state.titel

    st.header("Die Wächter der Erinnerung")

    waechter_text(
        f"Willkommen, {name} {titel}. Ein Dorf vergisst schneller, als es zugibt. "
        "Bevor du urteilst, solltest du lernen hinzusehen."
    )

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

    if st.button("Antworten prüfen"):
        if saerge == 4 and ornamente == 1 and kinder == 4:
            gehe_zu("entscheidung_1")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter_text(
                "Bedauerlich. Deine Auffassungsgabe ist in einem Zustand, "
                "der weitere Prüfungen derzeit nicht rechtfertigt. "
                "Schau noch einmal hin. Dies ist ein Mausoleum, kein Schätzspiel."
            )


# -----------------------------
# ENTSCHEIDUNG 1
# -----------------------------

elif st.session_state.seite == "entscheidung_1":

    name = st.session_state.name

    st.header("Die erste Frage")

    waechter_text(
        f"Akzeptabel, {name}. Du kannst zählen und lesen. "
        "Beides wird überschätzt – aber es ist ein Anfang."
    )

    waechter_text(
        "Menschen glauben oft, dass Mauern, Besitz oder Ordnung ein Dorf zusammenhalten. "
        "Sie irren sich erstaunlich häufig."
    )

    entscheidung = st.radio(
        "Was darf niemals verloren gehen?",
        [
            "Ordnung",
            "Geschichten",
            "Wahrheit",
            "Tradition",
            "Die letzte Dorfkneipe",
            "Das Freudenhaus",
        ],
    )

    if st.button("Antwort registrieren"):
        st.session_state.entscheidung_1 = entscheidung
        gehe_zu("urteil_1")


elif st.session_state.seite == "urteil_1":

    entscheidung = st.session_state.entscheidung_1

    st.header("Urteil des Wächters")

    if entscheidung == "Ordnung":
        waechter_text("Preußisch. Berechenbar. Nicht spannend – aber selten völlig falsch.")
    elif entscheidung == "Geschichten":
        waechter_text("Interessant. Menschen nennen Erinnerungen gern Wahrheit. Meist sind sie nur besser erzählt.")
    elif entscheidung == "Wahrheit":
        waechter_text("Mutig. Oder naiv. Wahrheit macht selten beliebt und noch seltener bequem.")
    elif entscheidung == "Tradition":
        waechter_text("Menschen halten erstaunlich lange an Dingen fest. Selbst dann, wenn niemand mehr weiß, warum.")
    elif entscheidung == "Die letzte Dorfkneipe":
        waechter_text("Endlich Ehrlichkeit. Gesellschaftlicher Zusammenhalt entsteht selten nüchtern.")
    elif entscheidung == "Das Freudenhaus":
        waechter_text("Bemerkenswert offen. Historisch schwer zu verteidigen. Menschlich nicht völlig unverständlich.")

    st.subheader("Nächster Ort")
    st.info("Kehre zum Parkplatz zurück und suche dort die Säule. Der nächste Teil der Prüfung erwartet dich bereits.")

    if st.button("Dem Wächter folgen"):
        gehe_zu("saeule")


# -----------------------------
# SÄULE
# -----------------------------

elif st.session_state.seite == "saeule":

    name = st.session_state.name

    st.header("Die zweite Prüfung")

    waechter_text(
        f"Reiß dich zusammen, {name}. Die nächste Prüfung verlangt mehr als bloßes Herumstehen."
    )

    st.write("Welche Symbole erkennst du tatsächlich?")

    symbole = st.multiselect(
        "Wähle alle zutreffenden Antworten:",
        [
            "Amboss mit Werkzeug",
            "Äskulapstab",
            "Pflug",
            "Kanne",
            "Fisch",
            "Turm",
        ],
    )

    richtige_symbole = {
        "Amboss mit Werkzeug",
        "Äskulapstab",
        "Pflug",
        "Kanne",
    }

    if st.button("Symbole prüfen"):
        if set(symbole) == richtige_symbole:
            gehe_zu("entscheidung_2")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter_text(
                "Interessant. Entweder blickst du kreativ auf Symbolik – "
                "oder deine Beobachtungsgabe macht gerade Urlaub. Schau genauer hin."
            )


elif st.session_state.seite == "entscheidung_2":

    st.header("Was hält ein Dorf zusammen?")

    waechter_text(
        "Akzeptabel. Pflug, Äskulapstab, Amboss und Kanne. "
        "Nahrung, Gesundheit, Arbeit und Gemeinschaft. "
        "Und über allem sitzt der Vogel."
    )

    entscheidung = st.radio(
        "Fredersdorf gerät in eine Krise. Was schützt du zuerst?",
        ["Nahrung", "Gesundheit", "Arbeit", "Gemeinschaft"],
    )

    if st.button("Antwort registrieren"):
        st.session_state.entscheidung_2 = entscheidung
        gehe_zu("urteil_2")


elif st.session_state.seite == "urteil_2":

    name = st.session_state.name
    titel = st.session_state.titel
    entscheidung_1 = st.session_state.entscheidung_1
    entscheidung_2 = st.session_state.entscheidung_2

    st.header("Urteil des Wächters")

    if entscheidung_2 == "Nahrung":
        waechter_text("Pragmatisch. Hungrige Menschen diskutieren schlecht.")
    elif entscheidung_2 == "Gesundheit":
        waechter_text("Mitgefühl. Riskant – aber ehrenhaft.")
    elif entscheidung_2 == "Arbeit":
        waechter_text("Verdächtig preußisch. Beeindruckend effizient.")
    elif entscheidung_2 == "Gemeinschaft":
        waechter_text("Überraschend vernünftig.")

    if entscheidung_1 == "Geschichten" and entscheidung_2 == "Gemeinschaft":
        waechter_text(f"Der Wächter hält dich für erstaunlich menschlich, {name} {titel}.")
    elif entscheidung_1 == "Ordnung" and entscheidung_2 == "Arbeit":
        waechter_text(f"Der Wächter vermutet Verwaltungserfahrung, {name} {titel}.")
    else:
        waechter_text(f"Der Vogel hat dich beobachtet, {name}. Noch ist unklar, ob das beruhigend ist.")

    st.subheader("Der nächste Ort")

    waechter_text(
        "Ihr habt gesehen. Ihr habt geurteilt. Nun folgt dem Weg. "
        "Begebt euch an diesen Ort. Der Wächter wartet bereits."
    )

    koordinate("N 52° 30.851'", "E 13° 45.001'")

    if st.button("Dem Wächter folgen"):
        gehe_zu("schwelle")


# -----------------------------
# SCHWELLE / BRÜCKE
# -----------------------------

elif st.session_state.seite == "schwelle":

    name = st.session_state.name

    st.header("Die Schwelle")

    waechter_text(
        f"{name}. Von hier an wird es schwieriger. "
        "Manche Wege verbinden Orte. Andere verbinden Entscheidungen."
    )

    antwort = st.radio(
        "Was siehst du hier?",
        [
            "Eine Brücke",
            "Einen ambitionierten Dorfgraben mit Größenwahn",
            "Eine äußerst preußische Methode, nicht nass zu werden",
        ],
    )

    if st.button("Antwort prüfen"):
        if antwort == "Eine Brücke":
            gehe_zu("tier_pruefung")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter_text("Originell. Aber Kreativität ersetzt keine Beobachtung. Schau genauer hin.")


elif st.session_state.seite == "tier_pruefung":

    name = st.session_state.name

    st.header("Die Prüfung der Aufmerksamkeit")

    waechter_text(
        f"Nicht jeder Wächter besteht aus Stein, {name}. "
        "Nicht jeder Wächter spricht. Manche beobachten einfach."
    )

    tier = st.radio(
        "Welches Tier blickt euch hier entgegen?",
        ["Eule", "Adler", "Fuchs", "Fisch"],
    )

    if st.button("Antwort prüfen"):
        if tier == "Eule":
            gehe_zu("tier_urteil")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter_text("Große Augen wären hilfreich gewesen. Schau dich noch einmal genauer um.")


elif st.session_state.seite == "tier_urteil":

    st.header("Urteil des Wächters")

    waechter_text(
        "Große Augen. Wenige Worte. Der Wächter erkennt Verwandtschaft im Geiste."
    )

    if st.button("Dem Wächter folgen"):
        gehe_zu("hoeren")


elif st.session_state.seite == "hoeren":

    name = st.session_state.name

    st.header("Die Prüfung des Hörens")

    waechter_text(
        f"Nun schweige selbst einen Moment, {name}. "
        "Nicht jede Prüfung verlangt Augen. Schließe sie. Höre genau hin."
    )

    geraeusch = st.radio(
        "Was nimmst du zuerst wahr?",
        [
            "Blätterrascheln",
            "Vogelstimmen",
            "Autolärm",
            "Wind",
            "Die Stimme des Wächters",
        ],
    )

    if st.button("Antwort registrieren"):
        st.session_state.geraeusch = geraeusch
        gehe_zu("hoeren_urteil")


elif st.session_state.seite == "hoeren_urteil":

    name = st.session_state.name
    geraeusch = st.session_state.geraeusch

    st.header("Urteil des Wächters")

    if geraeusch == "Blätterrascheln":
        waechter_text("Die Natur spricht leise. Du hast zugehört.")
    elif geraeusch == "Vogelstimmen":
        waechter_text("Aufmerksam. Nicht jede Botschaft wird mit Worten überbracht.")
    elif geraeusch == "Autolärm":
        waechter_text("Realistisch. Der Wächter respektiert Ehrlichkeit.")
    elif geraeusch == "Wind":
        waechter_text("Viele übersehen ihn. Du offenbar nicht.")
    elif geraeusch == "Die Stimme des Wächters":
        waechter_text("Beunruhigend. Aber nicht grundsätzlich falsch.")

    waechter_text(
        f"Du hast gesehen. Du hast gehört. Noch eine Prüfung, {name}. "
        "Danach fällt das Urteil. Also reiß dich zusammen."
    )

    if st.button("Das Urteil erwarten"):
        gehe_zu("entscheidung_3")


# -----------------------------
# LETZTE FRAGE
# -----------------------------

elif st.session_state.seite == "entscheidung_3":

    st.header("Die letzte Frage")

    waechter_text(
        "Eine Wahrheit über Fredersdorf gelangt in deine Hände. "
        "Sie könnte helfen. Sie könnte verletzen. Sie könnte Unruhe stiften."
    )

    entscheidung = st.radio(
        "Wie handelst du?",
        [
            "Sofort veröffentlichen",
            "Geheim halten",
            "Nur den Betroffenen mitteilen",
        ],
    )

    if st.button("Urteil empfangen"):
        st.session_state.entscheidung_3 = entscheidung
        gehe_zu("endurteil")


# -----------------------------
# ENDURTEIL
# -----------------------------

elif st.session_state.seite == "endurteil":

    name = st.session_state.name
    titel = st.session_state.titel
    entscheidung_3 = st.session_state.entscheidung_3

    st.header("Das Urteil des Wächters")

    if entscheidung_3 == "Sofort veröffentlichen":

        waechter_text(
            f"Bedauerlich, {name}. Der Wächter hatte Hoffnungen. "
            "Nicht besonders große – aber immerhin Hoffnungen."
        )

        waechter_text(
            "Deine Antworten deuten auf spontane Moral, ausgeprägte Transparenz "
            "oder eine bemerkenswerte Neigung zu moralischer Flexibilität hin."
        )

        st.subheader("Vorläufige Beaufsichtigung")
        koordinate("N 52° 30.811'", "E 13° 45.022'")

        st.markdown("**Einstufung: Moralisch flexibel. Beaufsichtigung empfohlen.**")

        st.write("Auch der Wächter gibt jedem eine zweite Chance.")
        st.write("Arbeite an:")
        st.write("□ Integrität")
        st.write("□ Verschwiegenheit")
        st.write("□ Verantwortungsbewusstsein")
        st.write("□ Dorfverwaltungskompetenz")
        st.write("□ Weniger spontane Offenheit")
        st.write("Du darfst selbstverständlich loggen.")
        st.write("Der Wächter glaubt an Entwicklung. Meistens.")

    else:

        if entscheidung_3 == "Geheim halten":
            waechter_text("Verschwiegenheit. Kontrolle. Das gefällt dem Wächter.")
        else:
            waechter_text("Abgewogen. Erstaunlich differenziert.")

        st.subheader("Podewils' Vermächtnis")
        koordinate("N 52° 30.931'", "E 13° 45.063'")

        waechter_text(
            f"Gegen alle Erwartungen erscheinst du geeignet, {name} {titel}. "
            "Du hast gesehen. Du hast zugehört. Du hast geurteilt. "
            "Heute wurdest auch du beurteilt."
        )

        waechter_text(
            "Podewils' Vermächtnis wird dir anvertraut. "
            "Trage dich ein. Bewahre das Vermächtnis. Und schweige mit Würde."
        )

    st.divider()

    if st.button("Prüfung neu beginnen"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
