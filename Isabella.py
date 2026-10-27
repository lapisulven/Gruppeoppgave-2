#introduksjon til interaktiv historie spill 
print("Velkommen til den interaktive historien om Erling")
input("Trykk enter for å gå videre")
print() #del av koden som lager en linje mellom teksten, så det blir lettere å lese 
print ("Du er Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal")
print("Det har nå gått seks uker siden prosjektteamet ditt startet arbeidet, I begynnelsen var motivasjonen høy, men nå har det oppstått konflikter og uenigheter i teamet.")
print ("Den første prototypen skal være klar om tre uker, som proskjektleder må du ta viktige beslutninger for å håndtere konfliktene, bevare motivasjon og sikre fremdrift i proskjektet.")
print("Valgene du tar, vil påvirke hvordan historien utvikler seg og hvordan prosjektet ender.")
print () #mellomrom i tekst 
input("Trykk enter, når du er klar for å gå videre")
print() #Lager mellomrom, så koden blir lettere å lese 
#Scenario 1: konflikten mellom silje og Elias 
print("SCENARIO 1: Konflikten mellom Silje og Elias")
print() #mellomrom i tekst 
print("Silje og Elias er uenige om hvordan prosjektet skal gjennomføres. Konflikten har eskalert, og du må bestemme hvordan du skal håndtere den.")
print() #mellomrom i tekst 
print("Hva vil du gjøre?") #Valgene blir presentert 
print ("A: La HR bistå med å håndtere konflikten.")
print("B: Ta konflikten opp i plenum")

# Nå vil programmet kjøre forklaringen av scenario 1, Situasjonen og valgene er presentert
# Neste steg er å gjøre historien interaktiv 
valg1=input("Skriv A eller B)") #lagrer spillerens valg 
def ugyldig_valg(): #her definerer jeg en funksjon, da jeg skal bruke den flere ganger i koden
    print("Ugyldig valg. Vennligst velg A eller B.")
#input gjør at programmet venter på at spilleren skal skrive inn et svar 
#valg1 er variabelen som lagrer svaret, Hvis spilleren skrive 1, lagrer programmet teksten "1" i variabelen valg1, Hvis spiller skriver 2, lagrer programmet teksten "2"
if valg1 == "A": #hvis spiller skriver 1, vil programmet kjøre koden under
    print("Bra valg! Du har valgt å la HR bistå med å håndtere konflikten.") 
    print("HR håndterer konflikten på en nøytral måte")
    print("Partene fokuserer på konflikten og kommer frem til en løsning.")
    print ("Du er nå klar for å gå videre til scenario 2")
elif valg1 == "B": #hvis spiller skrver 2, vil programmet kjøre koden under 
    print("Intressant valg!, Du velger å ta konflikten opp i plenum.")
    print("Nå begynner flere i teamet begynner å velge side")
    print ("Og som resultat begynner teamet å bli spittet")
    print("Ikke alt kan løses i plenum, men kanskje du kan ta et bedre valg neste gang")
#innrykkende er viktig, fordi da skjønner programmet hvilke linjer som hører til hvilket alternativ
else:
    ugyldig_valg()

input("Trykk enter for å gå videre til scenario 2") 
#nå går vi videre til scenario 2 
print() #mellomrom i tekst 
print("SCENARIO 2: Konflikten mellom Hamdi og Hallgeir" )
print() #mellomrom i tekst 
print("Det har oppstått en uenighet mellom Hamdi og Hallgeir")
print("Gutta er uenige angående rammene for digitale folkemøter")     
print("Du må bestemme hvordan du vil håndtere konflikten mellom Hamdi og Hallgeir")
print() #mellomrom i tekst 
input("Trykk enter for å se valgene dine")
#Presenter valgene for scenario 2 
print () #mellomrom i tekst 
print("Hva vil du gjøre?")
print("A: Ta initiativ til et felles møte for å avklare uenigheten.")
print("B: Avvente og håpe at partene finner en løsning selv.")
print () #mellomrom i tekst 
#lagre spillerens valg 
valg2 = input ("Skriv A eller B: ")
#vis konsekvensene av valget 
if valg2 == "A": #Hvis spiller skrove "A", vil programmet kjøre koden under 
    print("WOW, nice!! Digger svaret ditt! Du valgte å ta initiativ til et felles møte.")
    input("Trykk enter for å fortsette...")
    print() #mellomrom i tekst
    print("Hamdi og Hallgeir får snakket sammen om uenigheten.")
    print ("De kommer frem til en løsning.")
    print ("Bra jobbet! Du håndterte konflikten på en god måte, og teamet er nå mer motivert!!")
    input ("Trykk enter når du er klar for å løse scenario 3")


elif valg2 == "B" : #hvis spiller skriver "B", vil programmet kjøre følgende 
    print() #mellomrom i tekst 
    print("okei, du velger å avvente situasjonen")
    input("Trykk enter for å fortsette...")
    print("Hamdi og Hallgeir finner ingen løsning selv...")
    print ("konflikten utvikler seg og det blir skillelig dårlig stemning")
    print ("Det går fint, du burde kanskje tatt initiativ til et felles møte, men vi har forstatt scenario 3 som skal løses")
    input("Trykk enter for å gå videre til scenario 3") 

else: 
    ugyldig_valg()
#Nå går vi videre til scenario 3 
print() #mellomrom i tekst
print("SCENARIO 3: Hvordan skal du bevare motivasjonen i teamet som helhet?")
print () #mellomrom i tekst 
print("Konfliktene har påvirket sammarbeidet i teamet.")
print("Nå er det på tide at du som prosjektleder tar grep for å bevare motivasjonen i teamet")
#Nå har vi presentert situasjonen, og nå skal vi presentere valgene for scenario 3
print () #mellomrom i tekst
input("Trykk enter for å se valgene du kan ta")
#presenter valgene for scenario 3 
print() #mellomrom i tekst 
print("Hva velger du å gjøre?")
print("A: Prioritere relasjonsbygging og sosiale aktiviteter ")
print("B: Fokusere på å oppnå resultater og fremdrift i prosjektet")
#lagre spillerens valg 
valg3 = input ("Skriv A eller B:")
#nå vises konsekvensene av valget spilleren tar 
if valg3 == "A": #hvis spiller skriver "A", vil programmet kjøre koden under 
    print("Bra valg! Du er en god prosjektleder. Du valgte å prioritere relasjonsbygging og sosiale aktiviteter.")
    input("Trykk enter for å fortsette...")
    print() #mellomrom i tekst 
    print("Teamet deltar i sosiale aktiviteter og bygger sterkere relasjoner.")
    print("Motivasjonen øker, og samarbeidet forbedres.")
    print("Prosjektet går fremover med et mer sammensveiset team!")
    print() #mellomrom i tekst
    input("Trykk enter for å avslutte spillet")
    print("Spillet er nå over. Takk for at du spilte!")
    print("Du var utrolig flink til å håndtere konflikter og motivere teamet. Kanskje prosjektleder jobben er noe for deg, for morro skyld, kan du alltid prøve igjen og ta andre valg for å se hvordan historien utvikler seg.")
elif valg3 == "B": #hvis spiller skriver "B", vil programmet kjøre koden under
    print("Interessant valg! Du valgte å fokusere på å oppnå resultater og fremdrift i prosjektet.")
    input("Trykk enter for å fortsette...")
    print() #mellomrom i tekst 
    print("Teamet jobber hardt for å oppnå resultater, men relasjonene blir bare dårligere.")
    print("Motivasjonen synker, og samarbeidet blir utfordrende.")
    print("Prosjektet går fremover, men produktet blir ikke som forventet.")
    print() #mellomrom i tekst
    input("Trykk enter for å avslutte spillet")
    print("Spillet er nå over. Takk for at du spilte!")
    print("Kanksje prosjektleder jobben ikke er noe for deg, men du kan alltid prøve igjen og ta andre valg for å se hvordan historien utvikler seg.")
else:
    ugyldig_valg()

