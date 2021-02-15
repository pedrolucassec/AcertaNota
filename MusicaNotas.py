#!/usr/bin/python3

import os
import random
from playsound import playsound


def jogo():
    os.system("clear")
  
    notas = random.choice(['Cmaior.mp3', 'Famaior.mp3', 'Lamaior.mp3', 'Remaior.mp3', 'Simaior.mp3', 'Solmaior.mp3'])
    print("Prepare o Ouvido!, Daqui a 3 segundos o Som surgirá!!")
    os.system("sleep 3 && clear")
    print("[Tocando] ~")

#C Maior
    if notas == "Cmaior.mp3":
        playsound('Notas/Cmaior.mp3')
        print("[Vou Repetir Ok?]")
        os.system("sleep 2")
        playsound('Notas/Cmaior.mp3')
        print("Mais Uma Vez..")
        os.system("sleep 2")
        playsound('Notas/Cmaior.mp3')   
        
        os.system("clear")
        cmaior_escolha = int(input("[1] Dó Maior <<\n[2] Fá Maior <<\n[3] Lá Maior <<\n[4] Ré Maior <<\n[5] Sí Maior <<\n[6] Sol Maior <<\n\n[ESCOLHA]: "))
        
        if cmaior_escolha == 1:
            print("\033[1;92m"+"\n\n[Parabéns Você acertou!]\n")
        
        else:
            os.system("clear")
            print("Você Errou!!\n\nA Resposta era: Dó Maior [C]")
            tentar_novamente = int(input("\nDeseja tentar novamente?\n\n[1] Sim\n[2] Não\n\n[ESCOLHA]: "))
        
            if tentar_novamente == 1:
                jogo()
            
            else:
                exit(0)
       
#Fa Maior
    if notas == "Famaior.mp3":
        playsound('Notas/Famaior.mp3')
        print("[Vou Repetir Ok?]")
        os.system("sleep 2")
        playsound('Notas/Famaior.mp3')
        print("Mais Uma Vez..")
        os.system("sleep 2")
        playsound('Notas/Famaior.mp3')

        os.system("clear")
        famaior_escolha = int(input("[1] Dó Maior <<\n[2] Fá Maior <<\n[3] Lá Maior <<\n[4] Ré Maior <<\n[5] Sí Maior <<\n[6] Sol Maior <<\n\n[ESCOLHA]: "))

        if famaior_escolha == 2:
            print("\033[1;92m"+"\n\n[Parabéns Você acertou!]\n")
        
        else:
            os.system("clear")
            print("Você Errou!!\n\nA Resposta era: Fá Maior [F]")
            tentar_novamente = int(input("\nDeseja tentar novamente?\n\n[1] Sim\n[2] Não\n\n[ESCOLHA]: "))

            if tentar_novamente == 1:
                jogo()

            else:
                exit(0)

#La Maior
    if notas == "Lamaior.mp3":
        playsound('Notas/Lamaior.mp3')
        print("[Vou Repetir Ok?]")
        os.system("sleep 2")
        playsound('Notas/Lamaior.mp3')
        print("Mais Uma Vez..")
        os.system("sleep 2")
        playsound('Notas/Lamaior.mp3')

        os.system("clear")
        lamaior_escolha = int(input("[1] Dó Maior <<\n[2] Fá Maior <<\n[3] Lá Maior <<\n[4] Ré Maior <<\n[5] Sí Maior <<\n[6] Sol Maior <<\n\n[ESCOLHA]: "))

        if lamaior_escolha == 3:
            print("\033[1;92m"+"\n\n[Parabéns Você acertou!]\n")
        
        else:
            os.system("clear")
            print("Você Errou!!\n\nA Resposta era: Lá Maior [A]")
            tentar_novamente = int(input("\nDeseja tentar novamente?\n\n[1] Sim\n[2] Não\n\n[ESCOLHA]: "))

            if tentar_novamente == 1:
                jogo()

            else:
                exit(0)

#Ré Maior
    if notas == "Famaior.mp3":
        playsound('Notas/Remaior.mp3')
        print("[Vou Repetir Ok?]")
        os.system("sleep 2")
        playsound('Notas/Remaior.mp3')
        print("Mais Uma Vez..")
        os.system("sleep 2")
        playsound('Notas/Remaior.mp3')

        os.system("clear")
        remaior_escolha = int(input("[1] Dó Maior <<\n[2] Fá Maior <<\n[3] Lá Maior <<\n[4] Ré Maior <<\n[5] Sí Maior <<\n[6] Sol Maior <<\n\n[ESCOLHA]: "))

        if remaior_escolha == 4:
            print("\033[1;92m"+"\n\n[Parabéns Você acertou!]\n")
        
        else:
            os.system("clear")
            print("Você Errou!!\n\nA Resposta era: Ré Maior [D]")
            tentar_novamente = int(input("\nDeseja tentar novamente?\n\n[1] Sim\n[2] Não\n\n[ESCOLHA]: "))

            if tentar_novamente == 1:
                jogo()

            else:
                exit(0)

#Sí Maior
    if notas == "Simaior.mp3":
        playsound('Notas/Simaior.mp3')
        print("[Vou Repetir Ok?]")
        os.system("sleep 2")
        playsound('Notas/Simaior.mp3')
        print("Mais Uma Vez..")
        os.system("sleep 2")
        playsound('Notas/Simaior.mp3')

        os.system("clear")
        simaior_escolha = int(input("[1] Dó Maior <<\n[2] Fá Maior <<\n[3] Lá Maior <<\n[4] Ré Maior <<\n[5] Sí Maior <<\n[6] Sol Maior <<\n\n[ESCOLHA]: "))

        if simaior_escolha == 5:
            print("\033[1;92m"+"\n\n[Parabéns Você acertou!]\n")
        
        else:
            os.system("clear")
            print("Você Errou!!\n\nA Resposta era: Sí Maior [B]")
            tentar_novamente = int(input("\nDeseja tentar novamente?\n\n[1] Sim\n[2] Não\n\n[ESCOLHA]: "))

            if tentar_novamente == 1:
                jogo()

            else:
                exit(0)

#Sol Maior
    if notas == "Solmaior.mp3":
        playsound('Notas/Solmaior.mp3')
        print("[Vou Repetir Ok?]")
        os.system("sleep 2")
        playsound('Notas/Solmaior.mp3')
        print("Mais Uma Vez..")
        os.system("sleep 2")
        playsound('Notas/Solmaior.mp3')

        os.system("clear")
        solmaior_escolha = int(input("[1] Dó Maior <<\n[2] Fá Maior <<\n[3] Lá Maior <<\n[4] Ré Maior <<\n[5] Sí Maior <<\n[6] Sol Maior <<\n\n[ESCOLHA]: "))

        if solmaior_escolha == 6:
            print("\033[1;92m"+"\n\n[Parabéns Você acertou!]\n")

        else:
            os.system("clear")
            print("Você Errou!!\n\nA Resposta era: Sol Maior [G]")
            tentar_novamente = int(input("\nDeseja tentar novamente?\n\n[1] Sim\n[2] Não\n\n[ESCOLHA]: "))

            if tentar_novamente == 1:
                jogo()

            else:
                exit(0)

def main():
    os.system("clear")
    print('\033[1;97m'+"Author: Pedro Lucas ~\n"+"\033[1;31m"+"\n[Github]: www.github.com/pedrolucassec\n"+"\033[1;32m"+"[Instagram]: https://www.instagram.com/pedrodev.c")
    escolha = int(input("\033[1;97m"+"\n*************************\n"+"\033[1;94m"+"[1] Jogar\n"+"\033[1;92m"+"[2] Instruções\n"+"\033[1;97m"+"*************************\n\n"+"\033[1;33m"+"[ESCOLHA]: "))
    
    if escolha == 1:
        jogo()

    elif escolha == 2:
        os.system("clear")
        print("----------------------------------------------\nEscute a Nota sem Pressionar nenhuma tecla,\nApós aparecer a mensagem de escolha,\ndigite o número desejado.\n----------------------------------------------")
        os.system("sleep 4")
        main()
    else:
        print("Opção Inválida!")
        exit(0)
main()
