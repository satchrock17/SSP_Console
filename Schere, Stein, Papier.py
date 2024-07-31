import random

def Spiel():
    print("Schere, Stein, Papier")
    
    Eingabe = input().lower()
    
    def Ausgabe():
        return random.randint(1,3)
    result = Ausgabe()
    
    
    if result == 1:
        print("Schere")
    elif result == 2:
        print("Stein")
    elif result == 3:
        print("Papier")
        
#Gewonnen, Verloren oder Unentschieden?
    
    #Unentschieden
    if result == 1 and Eingabe == "schere" or result == 2 and Eingabe == "stein" or result == 3 and Eingabe == "papier":
        print("leider Unentschieden ._.")
        
    #Gewonnen
    if result == 1 and Eingabe == "stein" or result == 2 and Eingabe == "papier" or result == 3 and Eingabe == "schere":
        print("Du hast Gewonnen! :D")
        
    #Verloren
    if result == 1 and Eingabe == "papier" or result == 2 and Eingabe == "schere" or result == 3 and Eingabe == "stein":
        print("Du hast Verloren :°(")


while True:
    Spiel()
