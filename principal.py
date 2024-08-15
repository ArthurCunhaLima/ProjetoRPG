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
            if poderes[x]["cooldownrodada"] == 0 :
                print (f"{x+1}. {poderes[x]['poder']} : {poderes[x]['dano']}.  Cooldown: Disponível")
            else:
                print (f"{x+1}. {poderes[x]['poder']} : {poderes[x]['dano']}.  Cooldown: {poderes[x]['cooldownrodada']} turnos")
            
        poder = int(input("Tecle o número correspondente ao poder "))
        
        
        if 1 <= poder <= len(poderes):  
            if poderes[(poder-1)]["cooldownrodada"] == 0 :
                poderes[(poder-1)]["cooldownrodada"] = poderes[(poder-1)]["cooldownpadrao"]
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
                    for x in range (len(poderes)):
                        if poderes[(x)]["cooldownrodada"] > 0 :
                            poderes[(x)]["cooldownrodada"] -= 1
                        elif poderes[(x)]["cooldownrodada"] < 0 :
                            poderes[(x)]["cooldownrodada"] = 0
                    
                    if HP_usuario > 0:
                        print(f"Lhe restou apenas {HP_usuario} HP")
                        time.sleep(3)
                    else :
                        print("VOCÊ MORREU.....")
                        print("FIM DE JOGO...")
                        exit()
                                       
           

            else :
                print("\n\nItem disponível em ",poderes[(poder-1)]["cooldownrodada"]," turno\n\n")
                
        else :
            print("\n\nDigite um item válido da sua mochila\n\n")
                    
              
 
    
