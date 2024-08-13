from random import randint
def monstros(variavel):


    dic_monstros = [
        {"nome": "Dragão Flamejante" , "Golpe" : "Sopro de Fogo" ,
          "Dano_Ataque" : 30, 
         "Ultimate": "Garra Flamejante",
          "Dano_Ultimate" : 100,
          "HP" : 180 },
        {"nome": "Espectro Sombrio"  ,
               
         "Golpe" : "Toque Sombrio" ,
         "Dano_Ataque": 30 , 
         "Ultimate" : "Assombração Lancinante ",
         "Dano_Ultimate" : 100 ,
         "HP" : 150  },
        
        {"nome" : "Górgona Petrificadora",
        "Golpe": "Olhar Petrificante",
        "Dano_Ataque": 30 ,
        "Ultimate" : "Mordida Venenosa",
        "Dano_Ultimate" : 100,
        "HP" : 160
        },
        {"nome" : "Kraken Abissal", 
         
         "Golpe": "Tentáculo Sugador" ,
         "Dano_Ataque" : 30 ,
         "Ultimate" : "Tempestade Marinha" ,
         "Dano_Ultimate" : 100,
         "HP" : 200},
        
        {"nome" : "Golem de Obsidiana", 
        "Golpe" : "Esmagamento Rochoso",
        "Dano_Ataque" : 30,
        "Ultimate" : "Colisão Sísmica",
        "Dano_Ultimate" : 100,
         "HP" : 190},
        {"nome" : "Banshee Lamentosa" , 
         "Golpe" : "Grito Agudo" ,
         "Dano_Ataque" : 30 ,
         "Ultimate" : "Lamento Fantasmagórico" ,
         "Dano_Ultimate" : 100,
         "HP" : 170},
        
        {"nome" : "Hidra Venenosa",
         "Golpe": "Baforada Tóxica " ,
           "Dano_Ataque": 30 ,
          "Ultimate " : "Mordida Venenosa" 
          ,"Dano_Ultimate" : 100 , 
          "HP" : 180 },
 
    ]
    num = randint(0,(len(dic_monstros))-1)
    variavel = dic_monstros[num]
    return variavel
def mochila(variavel):
    inventario = [
        {"poder" : "Bola de fogo" , "dano" : 20},
        {"poder" : "Raio" , "dano" : 50},
        {"poder" : "Rajada de Vento" , "dano" : 80}
    ]
    return inventario
def ataque(variavel) : 
    dado = randint( 1 , 20 )
    if dado == 15 :
      ataque = variavel["Ultimate"]
      dano_ataque = variavel["Dano_Ultimate"]
      return ataque , dano_ataque
    else :
      ataque = variavel ["Golpe"]
      dano_ataque = variavel["Dano_Ataque"]
      return ataque , dano_ataque