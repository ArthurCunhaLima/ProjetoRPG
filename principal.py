from funcoes import monstros,ataque,mochila
from random import randint
import time
while True :
    #Comandos iniciais
    poderes = mochila(None)
    HP_usuario = 100
    monstro = monstros(None)
    caminhada = randint(1,20)
    for x in range(caminhada) :
            print("CAMINHANDO...")
            time.sleep(0.5)
    
    #Briga
    print("Você encontrou o " ,monstro["nome"], " !!!\n"
        "HP :" ,monstro["HP"])
    while monstro["HP"] > 0:
        
        #Ataque
        print("Na sua mochila tem :")
        for x in range(len(poderes)) :
            print (f"{x+1}. {poderes[x]['poder']} : {poderes[x]['dano']}")
        poder = int(input("Tecle o número correspondente ao poder "))
        
                
        if 1 <= poder <= len(poderes):
            dano_poder = poderes[(poder-1)]["dano"]
            monstro["HP"] -= dano_poder
            print("ATAQUE REALIZADO !! \n HP DO MONSTRO : " , {monstro["HP"]})
            if monstro["HP"] == 0 or monstro["HP"] < 0:
                print("OPONENTE DERROTADO !!!!")
                time.sleep(10)
            else :
                print("VEZ DO OPONENTE")
                ataque_oponente = ataque(monstro)
                print(f"OPONENTE UTILIZOU {ataque_oponente[0]}")
                HP_usuario -= ataque_oponente[1]
                if HP_usuario > 0:
                    print(f"Lhe restou apenas {HP_usuario} HP")
                    time.sleep(3)
                else :
                    print("VOCÊ MORREU.....")
                    print("FIM DE JOGO...")
                    exit()
        else :
            print("Digite um item válido da sua mochila")
                    
              
 
    
