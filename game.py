import random
import sys
import os
import time

os.system ("clear")

banner='''
               WELCOME
-----------------------------------------
[+] Github : https://github.com/zaeni123 |
[+] Jangan lupa follow yah...^^          |
-----------------------------------------
'''

print(banner)

time.sleep(1)

print("Game Batu, Gunting, Kertas")
print("Silahkan pilih : ")
print("1. Batu")
print("2. Gunting")
print("3. Kertas")

def mulai ():
    kamu     = int(input("Masukkan Pilihanmu : "))
    com      = random.choice(["Batu", "Gunting", "Kertas"])
    if kamu == 1:
        print ("Kamu     : Batu ")
        print ("Komputer :", com)
        if com == "Batu":
            print ("Lah kok sama sih < ")
        if com == "Gunting":
            print ("Kamu menang horee...! ")
        if com == "Kertas":
            print ("Kamu kalah < gpp coba lagi semangat...!")
    if kamu == 2:
        print ("Kamu     : Gunting ")
        print ("Komputer :", com)
        if com == "Gunting":
            print ("Lah kok sama sih < ")
        if com == "Kertas":
            print ("Kamu menang horee...! ")
        if com == "Batu":
            print ("Kamu kalah < gpp coba lagi semangat...!")
    if kamu == 3:
        print ("Kamu     : Kertas ")
        print ("Komputer :", com)
        if com == "Kertas":
            print ("Lah kok sama sih < ")
        if com == "Batu":
            print ("Kamu menang horee...! ")
        if com == "Gunting":
            print ("Kamu kalah < gpp coba lagi semangat...!")
    if kamu >= 4:
        print("Gak ada pilihannya! ngetik yg bener wkwkwk")

mulai()

time.sleep(4)
os.system("python3 game.py")