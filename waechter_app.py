import streamlit as st

st.set_page_config(page_title="Podewils' Vermächtnis", page_icon="🦉", layout="centered")

# ---------- DESIGN ----------

st.markdown("""
<style>
.stApp { background-color: #0f0f0f; color: #f1e7d0; }
h1, h2, h3 { color: #d4af62 !important; }
p, label, span { color: #f1e7d0 !important; font-size: 1.06rem !important; }
label { font-weight: 800 !important; }

div[role="radiogroup"] label p,
div[data-testid="stMultiSelect"] label p {
    color: #f1e7d0 !important;
    font-size: 1.08rem !important;
}

.waechterbox {
    background: #252525;
    border-left: 5px solid #d4af62;
    border-radius: 10px;
    padding: 16px;
    margin: 14px 0;
    color: #f1e7d0;
    line-height: 1.55;
}

.waechtertitle {
    color: #d4af62;
    font-weight: 900;
    font-size: 1.1rem;
    margin-bottom: 8px;
}

.koordinate {
    background: #202020;
    border: 1px solid #d4af62;
    border-radius: 10px;
    padding: 18px;
    margin: 16px 0;
    text-align: center;
    color: #ffe29a;
    font-size: 1.35rem;
    font-weight: 900;
    letter-spacing: 0.5px;
}

.symbolbox {
    background: #1d1d1d;
    border: 1px solid #8a6a2f;
    border-radius: 10px;
    padding: 14px;
    margin: 10px 0;
    color: #f1e7d0;
    line-height: 1.5;
}

div.stButton > button {
    background-color: #8a6a2f;
    color: #fff5d6;
    border: 1px solid #d4af62;
    border-radius: 9px;
    font-weight: 900;
    width: 100%;
    padding: 0.8rem;
}

div.stButton > button:hover {
    background-color: #a88138;
    color: white;
}

input, textarea {
    background-color: #f4f4f4 !important;
    color: #111111 !important;
}

div[data-baseweb="select"] > div {
    background-color: #f4f4f4 !important;
    color: #111111 !important;
}
</style>
""", unsafe_allow_html=True)


# ---------- FUNKTIONEN ----------

def waechter(text):
    st.markdown(
        f"""
        <div class="waechterbox">
            <div class="waechtertitle">🦉 Der Wächter</div>
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )


def koordinate(n, e):
    st.markdown(f"<div class='koordinate'>{n}<br>{e}</div>", unsafe_allow_html=True)


def gehe_zu(seite):
    st.session_state.seite = seite
    st.rerun()


def add_punkte(punkte):
    st.session_state.punkte += punkte


def vertrauensquote():
    if st.session_state.max_punkte == 0:
        return 0
    return round((st.session_state.punkte / st.session_state.max_punkte) * 100)


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


# ---------- SESSION ----------

defaults = {
    "seite": "start",
    "name": "",
    "titel": "",
    "entscheidung_1": "",
    "entscheidung_2": "",
    "entscheidung_3": "",
    "brueckenantwort": "",
    "geraeusch": "",
    "punkte": 0,
    "max_punkte": 100,
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ---------- KOPF ----------

try:
    st.image("Podewils.jpeg", use_container_width=True)
except Exception:
    pass

st.title("PODEWILS' VERMÄCHTNIS")
st.subheader("Das Urteil des Wächters")
st.divider()


# ---------- START ----------

if st.session_state.seite == "start":

    st.header("Die Aufzeichnungen des Wächters")

    waechter(
        "Willkommen.<br><br>"
        "Seit Jahrhunderten beobachte ich Fredersdorf.<br><br>"
        "Heute beobachte ich dich.<br><br>"
        "Bevor die Prüfung beginnt, will ich wissen, wen ich beurteile."
    )

    name = st.text_input("Wie lautet dein Name?")
    geschlecht = st.selectbox("Geschlecht", ["weiblich", "männlich", "keine Angabe"])

    eigenschaft = st.selectbox(
        "Welche Eigenschaft beschreibt dich am besten?",
        [
            "wachsam", "neugierig", "beharrlich", "besonnen", "mutig",
            "skeptisch", "aufmerksam", "abenteuerlustig", "gesprächsbereit",
            "optimistisch", "vertrauensselig", "naiv", "eigenwillig",
            "impulsiv", "treuherzig"
        ],
    )

    if st.button("Prüfung beginnen"):
        if not name.strip():
            st.error("Der Wächter verlangt einen Namen.")
        else:
            st.session_state.name = name.strip()
            st.session_state.titel = titel_bilden(geschlecht, eigenschaft)
            gehe_zu("mausoleum_start")


# ---------- MAUSOLEUM ----------

elif st.session_state.seite == "mausoleum_start":

    name = st.session_state.name
    titel = st.session_state.titel

    st.header("Die Wächter der Erinnerung")

    waechter(
        f"Willkommen, {name} {titel}.<br><br>"
        "Ein Dorf vergisst schneller, als es zugibt.<br><br>"
        "Bevor du urteilst, solltest du lernen hinzusehen.<br><br>"
        "Wirf einen Blick in die unteren Fenster des Mausoleums."
    )

    if st.button("Ich sehe hin"):
        gehe_zu("frage_saerge")


elif st.session_state.seite == "frage_saerge":

    st.header("Erste Beobachtung")
    waechter("Zähle genau. Dies ist kein Ort für grobe Schätzungen.")

    saerge = st.number_input("Wie viele sichtbare Särge erkennst du?", min_value=0, max_value=20, step=1)

    if st.button("Antwort prüfen"):
        if saerge == 4:
            add_punkte(10)
            gehe_zu("frage_ornament")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter(
                "Bedauerlich.<br><br>"
                "Deine Auffassungsgabe ist in einem Zustand, der weitere Prüfungen derzeit nicht rechtfertigt.<br><br>"
                "Schau noch einmal hin."
            )


elif st.session_state.seite == "frage_ornament":

    st.header("Zweite Beobachtung")
    waechter("Nicht alles, was sichtbar ist, wurde gleich gestaltet. Achte auf die Details.")

    ornamente = st.number_input(
        "Wie viele dieser Särge tragen ein rundovales Ornament?",
        min_value=0,
        max_value=20,
        step=1
    )

    if st.button("Antwort prüfen"):
        if ornamente == 1:
            add_punkte(10)
            gehe_zu("frage_kinder")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter(
                "Mindestens ein Detail ist dir entgangen.<br><br>"
                "Das ist unpraktisch, wenn man beurteilt werden möchte."
            )


elif st.session_state.seite == "frage_kinder":

    st.header("Dritte Beobachtung")
    waechter("Nun lies. Der Wächter prüft nicht nur Augen, sondern auch Geduld.")

    kinder = st.number_input(
        "Wie viele Kinder hatte Heinrich Graf von Podewils laut Infotafel?",
        min_value=0,
        max_value=20,
        step=1
    )

    if st.button("Antwort prüfen"):
        if kinder == 4:
            add_punkte(10)
            gehe_zu("entscheidung_1")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter(
                "Lesen gehört zu den unterschätzten Kulturtechniken.<br><br>"
                "Schau noch einmal auf die Infotafel."
            )


# ---------- ENTSCHEIDUNG 1 ----------

elif st.session_state.seite == "entscheidung_1":

    name = st.session_state.name

    st.header("Die erste Frage")

    waechter(
        f"Akzeptabel, {name}.<br><br>"
        "Du kannst zählen und lesen.<br><br>"
        "Beides wird überschätzt – aber es ist ein Anfang."
    )

    waechter(
        "Menschen glauben oft, dass Mauern, Besitz oder Ordnung ein Dorf zusammenhalten.<br><br>"
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

        if entscheidung in ["Wahrheit", "Geschichten"]:
            add_punkte(10)
        elif entscheidung in ["Tradition", "Ordnung"]:
            add_punkte(8)
        elif entscheidung == "Die letzte Dorfkneipe":
            add_punkte(7)
        else:
            add_punkte(6)

        gehe_zu("urteil_1")


elif st.session_state.seite == "urteil_1":

    entscheidung = st.session_state.entscheidung_1

    st.header("Urteil des Wächters")

    texte = {
        "Ordnung": "Preußisch. Berechenbar.<br><br>Nicht spannend – aber selten völlig falsch.",
        "Geschichten": "Interessant.<br><br>Menschen nennen Erinnerungen gern Wahrheit.<br><br>Meist sind sie nur besser erzählt.",
        "Wahrheit": "Mutig. Oder naiv.<br><br>Wahrheit macht selten beliebt und noch seltener bequem.",
        "Tradition": "Menschen halten erstaunlich lange an Dingen fest.<br><br>Selbst dann, wenn niemand mehr weiß, warum.",
        "Die letzte Dorfkneipe": "Endlich Ehrlichkeit.<br><br>Gesellschaftlicher Zusammenhalt entsteht selten nüchtern.",
        "Das Freudenhaus": "Bemerkenswert offen.<br><br>Historisch schwer zu verteidigen.<br><br>Menschlich nicht völlig unverständlich.",
    }

    waechter(texte[entscheidung])

    st.subheader("Nächster Ort")
    st.info("Kehre zum Parkplatz zurück und suche dort die Säule. Der nächste Teil der Prüfung erwartet dich bereits.")

    if st.button("Dem Wächter folgen"):
        gehe_zu("saeule")


# ---------- SÄULE ----------

elif st.session_state.seite == "saeule":

    name = st.session_state.name

    st.header("Die zweite Prüfung")

    waechter(
        f"Reiß dich zusammen, {name}.<br><br>"
        "Diese Säule erzählt von den Grundlagen eines funktionierenden Dorfes.<br><br>"
        "Sie sprechen selten laut – aber sie tragen alles.<br><br>"
        "Erkennst du sie?"
    )

    symbole = st.multiselect(
        "Welche Symbole erkennst du tatsächlich?",
        [
            "Amboss mit Werkzeug",
            "Äskulapstab",
            "Pflug",
            "Kanne",
            "Fisch",
            "Turm",
        ],
    )

    richtige_symbole = {"Amboss mit Werkzeug", "Äskulapstab", "Pflug", "Kanne"}

    if st.button("Symbole prüfen"):
        if set(symbole) == richtige_symbole:
            add_punkte(15)
            gehe_zu("entscheidung_2")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter(
                "Interessant.<br><br>"
                "Entweder blickst du kreativ auf Symbolik – oder deine Beobachtungsgabe macht gerade Urlaub.<br><br>"
                "Schau genauer hin."
            )


elif st.session_state.seite == "entscheidung_2":

    st.header("Die zweite Frage")

    waechter(
        "Akzeptabel.<br><br>"
        "Du erkennst zumindest die Grundlagen funktionierender Dorfverwaltung."
    )

    st.markdown("""
    <div class="symbolbox">
    <b>Der Pflug</b><br>
    steht für Nahrung. Ohne sie hungert ein Dorf.<br><br>
    <b>Der Äskulapstab</b><br>
    steht für Gesundheit. Ohne sie leidet ein Dorf.<br><br>
    <b>Der Amboss mit Werkzeug</b><br>
    steht für Arbeit und Handwerk. Ohne sie steht ein Dorf still.<br><br>
    <b>Die Kanne</b><br>
    steht für Versorgung und Gemeinschaft. Ohne sie zerfällt ein Dorf.
    </div>
    """, unsafe_allow_html=True)

    entscheidung = st.radio(
        "Fredersdorf gerät in eine Krise. Was schützt du zuerst?",
        ["Nahrung", "Gesundheit", "Arbeit", "Gemeinschaft"],
    )

    if st.button("Antwort registrieren"):
        st.session_state.entscheidung_2 = entscheidung

        if entscheidung == "Gemeinschaft":
            add_punkte(10)
        elif entscheidung in ["Gesundheit", "Nahrung"]:
            add_punkte(9)
        else:
            add_punkte(8)

        gehe_zu("urteil_2")


elif st.session_state.seite == "urteil_2":

    name = st.session_state.name
    titel = st.session_state.titel
    e1 = st.session_state.entscheidung_1
    e2 = st.session_state.entscheidung_2

    st.header("Urteil des Wächters")

    urteile = {
        "Nahrung": "Pragmatisch.<br><br>Hungrige Menschen diskutieren schlecht.",
        "Gesundheit": "Mitgefühl.<br><br>Riskant – aber ehrenhaft.",
        "Arbeit": "Verdächtig preußisch.<br><br>Beeindruckend effizient.",
        "Gemeinschaft": "Überraschend vernünftig.",
    }

    text = urteile[e2]

    if e1 == "Geschichten" and e2 == "Gemeinschaft":
        text += f"<br><br>Der Wächter hält dich für erstaunlich menschlich, {name} {titel}."
    elif e1 == "Ordnung" and e2 == "Arbeit":
        text += f"<br><br>Der Wächter vermutet Verwaltungserfahrung, {name} {titel}."
    else:
        text += f"<br><br>Der Wächter hat deine Entscheidungen registriert, {name}.<br><br>Noch ist unklar, ob das beruhigend ist."

    waechter(text)

    st.subheader("Der nächste Ort")

    waechter(
        "Ihr habt gesehen. Ihr habt geurteilt.<br><br>"
        "Nun folgt dem Weg.<br><br>"
        "Begebt euch an diesen Ort. Der Wächter wartet bereits."
    )

    koordinate("N 52° 30.851'", "E 13° 45.001'")

    if st.button("Dem Wächter folgen"):
        gehe_zu("schwelle")


# ---------- SCHWELLE ----------

elif st.session_state.seite == "schwelle":

    name = st.session_state.name

    st.header("Die Schwelle")

    waechter(
        f"{name}. Konzentriere dich!<br><br>"
        "Manche Wege verbinden Orte.<br><br>"
        "Andere führen geradewegs in die Quarantänebox."
    )

    antwort = st.radio(
        "Was siehst du hier?",
        [
            "Eine Brücke",
            "Eine äußerst preußische Methode, nicht nass zu werden",
            "Ein bemerkenswert aufwendiger Versuch, fünf Meter Wasser zu überwinden",
        ],
    )

    if st.button("Antwort registrieren"):
        st.session_state.brueckenantwort = antwort

        if antwort == "Eine Brücke":
            add_punkte(10)
            gehe_zu("bruecke_urteil")
        elif antwort == "Eine äußerst preußische Methode, nicht nass zu werden":
            add_punkte(8)
            gehe_zu("bruecke_urteil")
        else:
            add_punkte(7)
            gehe_zu("bruecke_urteil")


elif st.session_state.seite == "bruecke_urteil":

    name = st.session_state.name
    antwort = st.session_state.brueckenantwort

    st.header("Urteil des Wächters")

    if antwort == "Eine Brücke":
        waechter(
            "Sachlich korrekt.<br><br>"
            "Der Wächter notiert: nüchterne Beobachtung."
        )
    elif antwort == "Eine äußerst preußische Methode, nicht nass zu werden":
        waechter(
            "Indirekt korrekt.<br><br>"
            "Der Wächter erkennt Sinn für Verwaltung, Ordnung und trockene Füße."
        )
    else:
        waechter(
            "Ungewöhnlich formuliert.<br><br>"
            "Aber nicht grundsätzlich falsch.<br><br>"
            "Der Wächter wertet es als ausreichende Annäherung an die Wirklichkeit."
        )

    waechter(
        f"Die Antwort wird gewertet, {name}.<br><br>"
        "Fahre fort. Noch ist das Urteil nicht gesprochen."
    )

    if st.button("Dem Wächter folgen"):
        gehe_zu("tier_pruefung")


elif st.session_state.seite == "tier_pruefung":

    name = st.session_state.name

    st.header("Die Prüfung der Aufmerksamkeit")

    waechter(
        f"Nicht jeder Wächter besteht aus Stein, {name}.<br><br>"
        "Nicht jeder Wächter spricht.<br><br>"
        "Manche beobachten einfach."
    )

    tier = st.radio(
        "Welches Tier blickt euch hier entgegen?",
        ["Eule", "Adler", "Fuchs", "Fisch"],
    )

    if st.button("Antwort prüfen"):
        if tier == "Eule":
            add_punkte(10)
            gehe_zu("tier_urteil")
        else:
            st.error("Der Wächter ist nicht überzeugt.")
            waechter("Große Augen wären hilfreich gewesen.<br><br>Schau dich noch einmal genauer um.")


elif st.session_state.seite == "tier_urteil":

    st.header("Urteil des Wächters")

    waechter(
        "Große Augen.<br><br>"
        "Wenige Worte.<br><br>"
        "Der Wächter erkennt Verwandtschaft im Geiste."
    )

    if st.button("Dem Wächter folgen"):
        gehe_zu("hoeren")


elif st.session_state.seite == "hoeren":

    name = st.session_state.name

    st.header("Die Prüfung des Hörens")

    waechter(
        f"Nun schweige selbst einen Moment, {name}.<br><br>"
        "Nicht jede Prüfung verlangt Augen.<br><br>"
        "Schließe sie. Höre genau hin."
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

        if geraeusch == "Die Stimme des Wächters":
            add_punkte(6)
        else:
            add_punkte(5)

        gehe_zu("hoeren_urteil")


elif st.session_state.seite == "hoeren_urteil":

    name = st.session_state.name
    geraeusch = st.session_state.geraeusch

    st.header("Urteil des Wächters")

    texte = {
        "Blätterrascheln": "Die Natur spricht leise.<br><br>Du hast zugehört.",
        "Vogelstimmen": "Aufmerksam.<br><br>Nicht jede Botschaft wird mit Worten überbracht.",
        "Autolärm": "Realistisch.<br><br>Der Wächter respektiert Ehrlichkeit.",
        "Wind": "Viele übersehen ihn.<br><br>Du offenbar nicht.",
        "Die Stimme des Wächters": "Beunruhigend.<br><br>Aber nicht grundsätzlich falsch.",
    }

    waechter(
        texte[geraeusch] +
        f"<br><br>Du hast gesehen. Du hast gehört.<br><br>Noch eine Prüfung, {name}. Danach fällt das Urteil.<br><br>Also reiß dich zusammen."
    )

    if st.button("Das Urteil erwarten"):
        gehe_zu("entscheidung_3")


# ---------- LETZTE FRAGE ----------

elif st.session_state.seite == "entscheidung_3":

    st.header("Die letzte Frage")

    waechter(
        "Eine Wahrheit über Fredersdorf gelangt in deine Hände.<br><br>"
        "Sie könnte helfen.<br><br>"
        "Sie könnte verletzen.<br><br>"
        "Sie könnte Unruhe stiften."
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

        if entscheidung == "Nur den Betroffenen mitteilen":
            add_punkte(10)
        elif entscheidung == "Geheim halten":
            add_punkte(8)
        else:
            add_punkte(0)

        gehe_zu("endurteil")


# ---------- ENDURTEIL ----------

elif st.session_state.seite == "endurteil":

    name = st.session_state.name
    titel = st.session_state.titel
    e3 = st.session_state.entscheidung_3
    quote = vertrauensquote()

    st.header("Das abschließende Urteil")

    if e3 == "Sofort veröffentlichen":

        st.markdown("### Vorläufige Beaufsichtigung")

        waechter(
            f"Bedauerlich, {name}.<br><br>"
            "Der Wächter hatte Hoffnungen.<br><br>"
            "Nicht besonders große – aber immerhin Hoffnungen.<br><br>"
            f"Deine rechnerische Vertrauenswürdigkeit liegt bei <b>{quote} %</b>."
        )

        waechter(
            "Fachlich mag das brauchbar sein.<br><br>"
            "Moralisch bleibt es riskant.<br><br>"
            "Die letzte Antwort überschreibt alle vorherigen Verdienste."
        )

        waechter(
            "Das eigentliche Vermächtnis wird heute anderen anvertraut.<br><br>"
            "Für Personen mit vorläufig eingeschränkter Vertrauenswürdigkeit "
            "unterhält der Wächter jedoch eine gesonderte Einrichtung.<br><br>"
            "Eine kleine Dose für Besucher, deren moralische Flexibilität "
            "noch einer genaueren Beobachtung bedarf.<br><br>"
            "Der Wächter nennt sie gelegentlich:<br><br>"
            "<b>„Die Quarantänebox.“</b><br><br>"
            "Natürlich vollkommen inoffiziell."
        )

        koordinate("N 52° 30.811'", "E 13° 45.022'")

        st.markdown("""
        **Einstufung:** Moralisch flexibel. Beaufsichtigung empfohlen.

        **Arbeite an:**

        🛡️ Integrität  
        🔒 Verschwiegenheit  
        ⚖️ Verantwortungsbewusstsein  
        🏛️ Dorfverwaltungskompetenz  
        👁️ Weniger spontane Offenheit  

        Du darfst selbstverständlich loggen.

        Der Wächter glaubt an Entwicklung. Meistens.
        """)

    else:

        st.markdown("### Podewils' Vermächtnis")

        if e3 == "Geheim halten":
            waechter("Verschwiegenheit.<br><br>Kontrolle.<br><br>Das gefällt dem Wächter.")
        else:
            waechter("Abgewogen.<br><br>Erstaunlich differenziert.")

        waechter(
            f"Vertrauenswürdigkeit: <b>{quote} %</b>.<br><br>"
            "Ergebnis: geeignet."
        )

        koordinate("N 52° 30.931'", "E 13° 45.063'")

        waechter(
            f"Gegen alle Erwartungen erscheinst du geeignet, {name} {titel}.<br><br>"
            "Du hast gesehen.<br><br>"
            "Du hast zugehört.<br><br>"
            "Du hast geurteilt.<br><br>"
            "Heute wurdest auch du beurteilt."
        )

        waechter(
            "Podewils' Vermächtnis wird dir anvertraut.<br><br>"
            "Trage dich ein.<br><br>"
            "Bewahre das Vermächtnis.<br><br>"
            "Und schweige mit Würde."
        )

    st.divider()

    if st.button("Prüfung neu beginnen"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
