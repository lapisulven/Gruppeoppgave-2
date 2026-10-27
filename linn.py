print("======================================")
print("     ERLING OG INNBYGGERPORTALEN")
print("======================================")
print()
print("Velkommen til konfliktspillet!")

# Nå starter spillet
# Vi starter med null poeng
# Denne variabelen teller hvor mange gode valg du tar
poeng = 0

def still_spoersmaal(spoersmaal, valg_a, valg_b):
    print()
    print("=" * 50)
    print(spoersmaal)
    print("=" * 50)
    print("A) " + valg_a)
    print("B) " + valg_b)
    while True:
        svar = input("Ditt valg (skriv A eller B): ").lower().strip()
        if svar == "a" or svar == "b":
            return svar
        print("Ugyldig svar. Skriv bare A eller B.")

# START

print("Du er Erling, og du er leder for et team")
print("Dine valg avgjør hvordan det går med teamet")

# Valg 1
valg1 = still_spoersmaal(
    "Hvordan håndtere konflikten mellom Silje og Elias?",
    "La HR bistå",
    "Ta det opp i plenum",
)

if valg1 == "a":
    print("HR hjelper med en nøytral håndtering av konflikten.")
    print("HR passer på at det går på konflikt og ikke person.")
    print("De kommer frem til en løsning.")
    poeng = poeng + 1
else:
    print("Erling tar det opp i plenum, og de i teamet begynner å velge side.")
    print("Det blir en splittelse i teamet.")

# Valg 2
valg2 = still_spoersmaal(
    "Hvordan forhindre at konflikten mellom Hamdi og Hallgeir blusser opp?",
    "Ta initiativ til et felles møte for å avklare uenigheter",
    "Avvente og håpe at partene finner en løsning selv",
)

if valg2 == "a":
    print("I det felles møtet kommer de frem til en løsning.")
    poeng = poeng + 1
else:
    print("De finner ingen løsning selv, og sakskonlfkten")
    print("går over til en personkonflikt.")

# Valg 3
valg3 = still_spoersmaal(
    "Hvordan bevare motivasjonen i teamet som helhet?",
    "Sette av tid til telasjonsbygging og i sosiale aktiviteter for å gjenopprette tillit",
    "Prioritere fremdrift og leverandre for å holde fokus på resultatet"
)
if valg3 == "a":
    print("Teamet får god stemning og mye motivasjon.")
    print("De bygger tillit til hverandre.")
    poeng = poeng + 1
else:
    print("På kort sikt opprettholder teamet fremdriften,")
    print("mens samarbeidet på lengre sikt blir dårligere.")

# Slutt

print()
print("=" * 50)
print("SPILLET ER FERDIG!")
print("Du tok " + str(poeng) + " av 3 gode valg!")

if poeng == 3:
    print("Fantastisk! Du er en dyktig leder.")
elif poeng >= 1:
        print("Ikke dårlig, men det er rom for forbedring.")
else:
        print("Teamet sliter... Prøv igjen og velg annerledes!")
print("=" * 50)

