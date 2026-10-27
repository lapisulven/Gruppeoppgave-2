# ERLING: FRA STORMING TIL NORMING
# Et interaktivt tekstspill basert på gruppeoppgave 2 (IS-118).
# Kjør filen med: python erling_spill.py

from collections import namedtuple

# Hvert valg har tekst, effekt på de fire verdiene og en konsekvenstekst.
Valg = namedtuple("Valg", "tekst tillit samarbeid fremdrift motivasjon konsekvens")

# Hver runde har overskrift, situasjonsbeskrivelse, spørsmål og valg.
Runde = namedtuple("Runde", "overskrift beskrivelse sporsmal valg fortsett_tekst")

RUNDER = [
    Runde(
        overskrift="KONFLIKT 1 AV 3: SILJE OG ELIAS",
        beskrivelse=(
            "Silje, som er UX/UI-designer, og Elias, som er IT-rådgiver,\n"
            "er uenige om design, teknisk sikkerhet og kostnader.\n"
            "Uenigheten har blitt personlig, og resten av teamet merker konflikten.\n\n"
            "Dette er en manifest konflikt: uenigheten vises gjennom ord og handlinger."
        ),
        sporsmal="Hva gjør du som prosjektleder?",
        valg=[
            Valg("Ta konflikten opp i plenum, slik at hele gruppen kan diskutere den.",
                 0, 1, 1, 0,
                 "Begge får forklare seg foran gruppen. Det kan skape åpenhet, men noen\n"
                 "kan begynne å velge side. Konflikten kan spre seg til resten av teamet."),
            Valg("Be HR om å hjelpe med en nøytral samtale mellom Silje og Elias.",
                 2, 2, 0, 1,
                 "HR sørger for at begge blir hørt. Det kan bygge tillit og hindre at\n"
                 "konflikten blir større. Samtidig kan prosessen ta litt tid."),
            Valg("La Silje og Elias ordne opp helt på egen hånd.",
                 -2, -2, 1, -1,
                 "Du sparer tid akkurat nå, men konflikten kan fortsette uten at noen\n"
                 "hjelper dem. Resten av gruppen kan bli påvirket."),
        ],
        fortsett_tekst="Trykk Enter for å gå videre ...",
    ),
    Runde(
        overskrift="KONFLIKT 2 AV 3: HAMDI OG HALLGEIR",
        beskrivelse=(
            "Hamdi fra kulturavdelingen ønsker å bruke kommunens egen plattform.\n"
            "Han mener dette gir bedre kontroll over kommunikasjonen.\n"
            "Hallgeir, som er brukerrepresentant, ønsker en åpen løsning der\n"
            "innbyggerne kan dele meninger og komme med forslag.\n\n"
            "Uenigheten er foreløpig rolig, men frustrasjonen vokser."
        ),
        sporsmal="Hvordan håndterer du uenigheten?",
        valg=[
            Valg("Kalle inn Hamdi og Hallgeir til et felles møte.",
                 2, 2, -1, 1,
                 "Begge får forklare behovene sine og lytte til hverandre. Det kan\n"
                 "forebygge en større konflikt. Møtet bruker samtidig tid fra prosjektet."),
            Valg("La dem prøve å finne en løsning selv, uten at du griper inn.",
                 -2, -1, 1, -1,
                 "Du får mer tid til andre oppgaver. Men hvis de ikke blir enige,\n"
                 "kan frustrasjonen vokse og konflikten bli mer synlig."),
            Valg("Bestemme med en gang at kommunen skal bruke sin egen plattform.",
                 -1, -1, 2, -1,
                 "Gruppen kan komme raskere videre. Men Hallgeir kan føle at hans\n"
                 "mening ikke blir tatt på alvor, og tilliten kan bli svakere."),
            Valg("Foreslå en løsning som kombinerer kommunens plattform med åpne\n"
                 "muligheter for innbyggernes innspill.",
                 2, 2, 1, 2,
                 "Du prøver å ta hensyn til begge behovene. Det kan gi en praktisk\n"
                 "løsning og gjøre det lettere for gruppen å samarbeide."),
        ],
        fortsett_tekst="Trykk Enter for å gå videre ...",
    ),
    Runde(
        overskrift="KONFLIKT 3 AV 3: MOTIVASJON I HELE TEAMET",
        beskrivelse=(
            "Konfliktene har tatt tid fra utviklingen av prototypen.\n"
            "Flere i gruppen begynner å bli frustrerte og mindre motiverte.\n"
            "Det er bare tre uker igjen til prototypen skal presenteres.\n\n"
            "Du må finne en balanse mellom gode relasjoner og konkrete resultater."
        ),
        sporsmal="Hva prioriterer du nå?",
        valg=[
            Valg("Sette av tid til relasjonsbygging, felles samtaler og en kort sosial aktivitet.",
                 2, 2, -1, 2,
                 "Teamet får tid til å snakke sammen og bygge tillit. Det kan øke\n"
                 "motivasjonen, men det blir litt mindre tid til å utvikle prototypen."),
            Valg("Prioritere fremdrift: sette tydelige frister og fordele oppgavene.",
                 -1, -1, 3, -1,
                 "Arbeidet blir mer strukturert, og gruppen kan rekke flere oppgaver.\n"
                 "Men hvis konfliktene ikke blir tatt opp, kan frustrasjonen fortsette."),
            Valg("Kombinere korte samtaler om samarbeidet med tydelige frister og oppgaver.",
                 2, 2, 2, 2,
                 "Du bruker litt tid på relasjonene, men holder også fokus på leveransen.\n"
                 "Dette kan gi gruppen både bedre samarbeid og god fremdrift."),
        ],
        fortsett_tekst="Trykk Enter for siste beslutning ...",
    ),
    Runde(
        overskrift="SISTE BESLUTNING: KLARER GRUPPEN Å GÅ VIDERE?",
        beskrivelse=(
            "Det er kort tid igjen før prototypen skal presenteres.\n"
            "Du merker at gruppen har kommet et stykke, men det er fortsatt\n"
            "forskjeller i hvordan medlemmene samarbeider.\n\n"
            "Hva gjør du i den siste fasen?"
        ),
        sporsmal="Velg din siste handling som prosjektleder:",
        valg=[
            Valg("Samle gruppen, bli enige om felles spilleregler og avklare ansvar.",
                 2, 3, 0, 2,
                 "Gruppen får tydeligere felles mål, roller og regler for samarbeid."),
            Valg("La alle jobbe hver for seg for å bli ferdige så raskt som mulig.",
                 -2, -2, 3, -1,
                 "Oppgavene kan bli ferdige raskere, men gruppen får lite trening i\n"
                 "å samarbeide og løse uenigheter sammen."),
            Valg("Ta en siste felles samtale, men la gruppen selv bli enige om roller,\n"
                 "ansvar og hvordan de skal løse uenigheter.",
                 3, 2, 1, 2,
                 "Gruppen får ansvar for samarbeidet selv. Det kan styrke tillit,\n"
                 "ansvarsfølelse og felles forståelse."),
        ],
        fortsett_tekst=None,  # Ingen pause før sluttresultatet
    ),
]


def linje():
    print("\n" + "=" * 68 + "\n")


def juster(verdi, endring):
    """Holder verdien innenfor 0-10."""
    return max(0, min(10, verdi + endring))


def velg_sporsmal(sporsmal, valgliste):
    """Viser et spørsmål og returnerer det valgte alternativet."""
    print("\n" + sporsmal)
    for nummer, valg in enumerate(valgliste, start=1):
        # Flerlinjede alternativer rykkes inn slik at de står pent under hverandre
        tekst = valg.tekst.replace("\n", "\n     ")
        print(f"  {nummer}. {tekst}")
    while True:
        svar = input("\nSkriv nummeret på valget ditt: ").strip()
        if svar.isdigit() and 1 <= int(svar) <= len(valgliste):
            return valgliste[int(svar) - 1]
        print(f"Velg et tall fra 1 til {len(valgliste)}.")


def vis_status(status):
    print("\nSTATUS I PROSJEKTGRUPPEN")
    print(f"  Tillit:       {status['tillit']}/10")
    print(f"  Samarbeid:    {status['samarbeid']}/10")
    print(f"  Fremdrift:    {status['fremdrift']}/10")
    print(f"  Motivasjon:   {status['motivasjon']}/10")


def vis_resultat(status):
    tillit = status["tillit"]
    samarbeid = status["samarbeid"]
    fremdrift = status["fremdrift"]
    motivasjon = status["motivasjon"]
    gjennomsnitt = (tillit + samarbeid + fremdrift + motivasjon) / 4

    linje()
    print("SLUTTRESULTAT: HVILKEN FASE ER GRUPPEN I?")

    if tillit >= 6 and samarbeid >= 6 and motivasjon >= 5:
        print("\n*** GRUPPEN HAR BEVEGET SEG MOT NORMING-FASEN! ***")
        print(
            "\nGruppen har begynt å få bedre tillit og samarbeid. Medlemmene\n"
            "forstår hverandres synspunkter bedre og kan jobbe mot et felles mål.\n"
            "De har ikke nødvendigvis løst alle uenigheter, men de klarer i større\n"
            "grad å snakke sammen og finne løsninger.\n\n"
            "Erling har hjulpet gruppen med å gå fra storming mot norming."
        )
    elif tillit <= 3 or samarbeid <= 3:
        print("\n*** GRUPPEN ER FORTSATT FAST I STORMING-FASEN ***")
        print(
            "\nTillit eller samarbeid er fortsatt svakt. Uenighetene kan ha blitt\n"
            "større, og noen kan føle at de ikke blir hørt. Gruppen trenger mer\n"
            "dialog, tydeligere ansvar og hjelp til å løse konfliktene før den\n"
            "kan gå videre mot norming-fasen."
        )
    else:
        print("\n*** GRUPPEN ER PÅ VEI MOT NORMING, MEN HAR UTFORDRINGER IGJEN ***")
        print(
            "\nGruppen har gjort noen fremskritt, men samarbeidet er ikke helt\n"
            "stabilt ennå. Erling må fortsette å følge opp konfliktene og samtidig\n"
            "sørge for at arbeidet med prototypen går fremover."
        )

    if fremdrift >= 7:
        print("\nPROTOTYPE: Gruppen har god fremdrift og har gode muligheter til å bli ferdig.")
    elif fremdrift >= 4:
        print("\nPROTOTYPE: Gruppen har noe fremdrift, men må prioritere oppgavene godt.")
    else:
        print("\nPROTOTYPE: Gruppen ligger etter planen. Erling må lage en tydelig plan.")

    print(f"\nSamlet poengsnitt: {gjennomsnitt:.1f}/10")
    print(
        "\nHusk: Norming betyr ikke at alle alltid er enige. Det betyr at gruppen\n"
        "har utviklet bedre samarbeid, tydeligere roller og måter å håndtere uenighet på."
    )


def spill():
    linje()
    print("             ERLING: FRA STORMING TIL NORMING")
    print("                 Et interaktivt prosjektspill")
    linje()
    print(
        "Du spiller som Erling, prosjektleder for et internasjonalt prosjekt.\n"
        "Teamet skal utvikle en prototype for digitale folkemøter.\n"
        "Det har gått seks uker siden oppstarten. Den gode stemningen fra\n"
        "begynnelsen har blitt erstattet av uenighet, frustrasjon og tidspress.\n\n"
        "Prototypen skal være klar om tre uker. Du må ta gode valg for å\n"
        "hjelpe gruppen gjennom storming-fasen og videre mot norming-fasen."
    )
    input("\nTrykk Enter for å starte ...")

    status = {"tillit": 5, "samarbeid": 5, "fremdrift": 5, "motivasjon": 5}

    for runde in RUNDER:
        linje()
        print(runde.overskrift)
        print("\n" + runde.beskrivelse)
        valg = velg_sporsmal(runde.sporsmal, runde.valg)

        status["tillit"] = juster(status["tillit"], valg.tillit)
        status["samarbeid"] = juster(status["samarbeid"], valg.samarbeid)
        status["fremdrift"] = juster(status["fremdrift"], valg.fremdrift)
        status["motivasjon"] = juster(status["motivasjon"], valg.motivasjon)

        print("\nKONSEKVENS:")
        print(valg.konsekvens)
        vis_status(status)
        if runde.fortsett_tekst:
            input("\n" + runde.fortsett_tekst)

    vis_resultat(status)
    linje()
    print("Takk for at du spilte Erling!")


def main():
    try:
        while True:
            spill()
            svar = input("\nVil du spille på nytt og prøve andre valg? (j/n): ").strip().lower()
            if svar not in ("j", "ja"):
                print("\nTakk for at du spilte!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\nSpillet ble avsluttet. Takk for at du spilte!")


if __name__ == "__main__":
    main()