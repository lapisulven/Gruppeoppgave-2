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
    print("\n----------------------------------------")
    print("Hvordan håndtere konflikten mellom Silje og Elias?")
    print("1. La HR bistå?")
    print("2. Ta det opp i Plenum?")

    choice = get_choice()

    if choice == "1":
        print(
            "\n--> HR hjelper med en nøytral håndering av konflikten."
            " HR passer på at det går på konflikt og ikke person. De kommer frem til en løsning."
        )

    elif choice == "2":
        print(
            "\n--> Erling tar det opp i plenum og de i teamet begynner å velge side."
            " Det blir en splittesle i teamet."
        )


def spill_scenario2():
    """Scenario 2: Hamdi og Hallgeir"""
    print("\n----------------------------------------")
    print("Hvordan forhindre at konflikten mellom Hamdi og Hallgeir blusser opp?")
    print("1. Ta initativ til et felles møte for å avklare uenigheter?")
    print("2. Avvente og håpe at partene finder en løsning selv?")

    choice = get_choice()

    if choice == "1":
        print("\n--> I det felles møtet så kommer de frem til en løsning"
        )

    elif choice == "2":
        print("\n--> De finner ingen løsning slev og sakskonflikten går over til en personkonflikt."
        )


def spill_scenario3():
    """Scenario 3: Motivasjon i teamet."""
    print("\n----------------------------------------")
    print("Hvordan bevare motivasjnen i teamet som helhet?")
    print("1. Sette av tid til relasjonbygging og sosiale aktiviteter for å gjennoprette tillit?")
    print("2. Prioritere fremdrift og leveranse for å holde fokus på resultatet?")

    choice = get_choice()

    if choice == "1":
        print("\n--> Teamet får god stemning og mye motivasjon."
              " De bygger tillit til hverandre."
        )

    elif choice == "2":
        print("På kort sikt oppretholdet teamet fremdrift, mens samarbeidet på lengre sikt blir dåligere."
        )


def main():
    """Hvordan den skal kjøre spillet."""
    print("==================================================")
    print("      SPILLET OM KONFLIKTHÅNDTERING OG TEAM       ")
    print("==================================================")

    spill_scenario1()
    spill_scenario2()
    spill_scenario3()

    print("\n==================================================")
    print("                  SPILLET ER SLUTT                  ")
    print("====================================================")


if __name__ == "__main__":
    main()
