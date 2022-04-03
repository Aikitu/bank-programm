import os
import time

user = "admin"
pwd = "root123"

age = int(input("Bitte gebe dein Alter ein: "))
user_get = input("Bitte gebe deinen Username ein: ")
pwd_get = input("Bitte gebe dein Passwort ein: ")
login_status = False

if (user_get == user and pwd_get == pwd and age >= 18):
    login_status = True
else:
    login_status = False


print("\n")
print (".......................................................................................................................")
print("\n")

if (login_status == False):
    print("Der User ist entweder zu jung oder hat ein falsches Passwort angegeben! Das Skript wird terminiert...")

elif (login_status == True):
    print("Erfolgreich eingeloggt. Was wollen sie tun? \n[1]Auszahlung\n[2]Einzahlung")


    action = int(input("Eingabe: "))
    
    print("\n")
    print (".......................................................................................................................")
    print("\n")
    
    if (action == 1):
        time.sleep(2)
        os.system('cls')
        auszahlung_betrag = input("AUSZAHLUNG\n\nWie hoch soll der Betrag sein?: ")
        print(auszahlung_betrag + " wurden ausgezahlt! Das Skript wird terminiert...")
        time.sleep(2)
        
    elif (action == 2):
        time.sleep(2)
        os.system('cls')
        einzahlung_betrag = input("EINZAHLUNG\n\nWie hoch soll der Betrag sein?: ")
        print(einzahlung_betrag + " wurden eingezahlt! Das Skript wird terminiert...")
        time.sleep(2)
        
    
    
        