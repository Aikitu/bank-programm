# * it's just a little bank-programm. pretty bad and basic but hey, it's something

import os
import time

user = "admin" # username
pwd = "root123" # passwort

age = int(input("Bitte gebe dein Alter ein: ")) # muss ueber 18 sein
user_get = input("Bitte gebe deinen Username ein: ") # muss "admin" sein
pwd_get = input("Bitte gebe dein Passwort ein: ") # muss "root123" sein
login_status = False # deklaration von login_status

if (user_get == user and pwd_get == pwd and age >= 18): # überprüfen ob alles stimmt/richtig ist
    login_status = True # login erfolgreich
else:
    login_status = False # login fehlgeschlagen


print("\n")
print (".......................................................................................................................")
print("\n")

if (login_status == False): # wenn login fehlgeschlagen, dann terminieren
    print("Der User ist entweder zu jung oder hat ein falsches Passwort angegeben! Das Skript wird terminiert...")

elif (login_status == True): # wenn login erfolgreich, Eingabeabfrage
    print("Erfolgreich eingeloggt. Was wollen sie tun? \n[1]Auszahlung\n[2]Einzahlung")


    action = int(input("Eingabe: ")) # abfrage nach 1 (Auszahlung) oder 2 (Einzahlung)
    
    print("\n")
    print (".......................................................................................................................")
    print("\n")
    
    if (action == 1): # ueberpruefen von abfrage
        time.sleep(2)
        os.system('cls')
        auszahlung_betrag = input("AUSZAHLUNG\n\nWie hoch soll der Betrag sein?: ")
        print(auszahlung_betrag + " wurden ausgezahlt! Das Skript wird terminiert...")
        time.sleep(2)
        
    elif (action == 2): # ueberpruefen von abfrage
        time.sleep(2)
        os.system('cls')
        einzahlung_betrag = input("EINZAHLUNG\n\nWie hoch soll der Betrag sein?: ")
        print(einzahlung_betrag + " wurden eingezahlt! Das Skript wird terminiert...")
        time.sleep(2)
        
    
    
        