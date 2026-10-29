poeng = 0 

print("ERLINGS PROSJEKT")

def ask(spørsmål, riktig=["1", "2"]):
    print(spørsmål)
    while True:
        svar = input("Svar 1 eller 2: ").lower().strip()
        if svar in riktig:
            return svar
        else:
            print("Ugyldig svar. Vennligst prøv igjen.")


#nr 1
spørsmål1 = ask("Hvordan håndtere konflikten mellom Silje og Elias?"
"1. La HR bistå."
"2. Ta det opp i plenum.")

if spørsmål1 == "1":
    poeng = poeng + 1
    print("HR passer på at det går på konflikt og ikke person")
else:
    print("Det blir en splittelse i teamet")


#nr 2
spørsmål2= ask("Hvordan forhindre at konflikten mellom Hamdi og Hakkgeir blusser opp?"
               "1. Ta intiativ til et felles møte for å avklare uenigheter"
             "2. Avvente og håpe at partene finner en løsning selv")
if spørsmål2 == "1":
    poeng = poeng + 1
    print("I det felles møtet kommer de frem til en løsning")
else:
    print("De finner ingen løsning selv og sakskonflikten går over til en personkonflikt")

#nr 3
spørsmål3 = ask("Hvordan bevare motivasjonen i teamet som helhet?"
                "1. Sett av tid til relasjonsbygging og sosiale aktiviteter for å gjenopprette tillit" "2. prioritere fremdrift og leveramser for å holde fokus på resultatet")

if spørsmål3 == "1":
    poeng = poeng + 1
    print("Teamet får god stemning og mye motivasjon. De bygger tillit til hverandre")
else:
    print("På kort sikt opprettholder teamet fremdriften, mens samarbeidet på lengre sikt blir dårligere")

print("Du fikk", poeng, "poeng av 3 mulige.")
