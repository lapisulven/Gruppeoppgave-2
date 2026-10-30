poeng = 0
#Starter på 0, går til 3

#Gjør at man får beskjed hvis man skriver feil
def get_choice():
    """Gjør som at spiller putter in enten 1 eller 2. """
    while True:
        choice = input("Skriv inn 1 eller 2: ")
        if choice == "1" or choice == "2":
            return choice

        else:
            print("Ugyldig valg. Prøv igjen.")


def spill_scenario1():
    """Scenario 1: Silje og Elias"""
    global poeng #bruker den globale variabelen poeng
    print("\n----------------------------------------")
    print("Hvordan håndtere konflikten mellom Silje og Elias?")
    print("1. La HR bistå?")
    print("2. Ta det opp i Plenum?")

    choice = get_choice()

    if choice == "1":
        print(
            "\n--> HR hjelper med en nøytral håndtering av konflikten."
            " HR passer på at det går på konflikt og ikke person. De kommer frem til en løsning."
        )
        poeng = poeng + 1

    
    elif choice == "2":
        print(
            "\n--> Erling tar det opp i plenum og de i teamet begynner å velge side."
            " Det blir en splittelse i teamet."
        )


def spill_scenario2():
    """Scenario 2: Hamdi og Hallgeir"""
    global poeng
    print("\n----------------------------------------")
    print("Hvordan forhindre at konflikten mellom Hamdi og Hallgeir blusser opp?")
    print("1. Ta initiativ til et felles møte for å avklare uenigheter?")
    print("2. Avvente og håpe at partene finner en løsning selv?")

    choice = get_choice()

    if choice == "1":
        print("\n--> I det felles møtet så kommer de frem til en løsning"
        )
        poeng = poeng + 1

    elif choice == "2":
        print("\n--> De finner ingen løsning selv og sakskonflikten går over til en personkonflikt."
        )


def spill_scenario3():
    """Scenario 3: Motivasjon i teamet."""
    global poeng
    print("\n----------------------------------------")
    print("Hvordan bevare motivasjonen i teamet som helhet?")
    print("1. Sette av tid til relasjonsbygging og sosiale aktiviteter for å gjenopprette tillit?")
    print("2. Prioritere fremdrift og leveranse for å holde fokus på resultatet?")

    choice = get_choice()

    if choice == "1":
        print("\n--> Teamet får god stemning og mye motivasjon."
              " De bygger tillit til hverandre."
        )
        poeng = poeng + 1

    elif choice == "2":
        print("På kort sikt oppretholder teamet fremdrift, mens samarbeidet på lengre sikt blir dårligere."
        )


def main():
    """Hvordan den skal kjøre spillet."""
    print("==================================================")
    print("      SPILLET OM KONFLIKTHÅNDTERING OG TEAM       ")
    print("==================================================")

    spill_scenario1()
    spill_scenario2()
    spill_scenario3()

    print("\nDu fikk", poeng, "poeng av 3 mulige.")
    print("\n==================================================")
    print("                  SPILLET ER SLUTT                  ")
    print("====================================================")


if __name__ == "__main__":
    main()
