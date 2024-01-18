import os 
import random

x = int(input("quantidade de fichas: "))
cards = [
    "A_Ouros","A_Espadilha","A_Copas","A_Paus",
    "2_Ouros","2_Espadilha","2_Copas","2_Paus",
    "3_Ouros","3_Espadilha","3_Copas","3_Paus",
    "4_Ouros","4_Espadilha","4_Copas","4_Paus",
    "5_Ouros","5_Espadilha","5_Copas","5_Paus",
    "6_Ouros","6_Espadilha","6_Copas","6_Paus",
    "7_Ouros","7_Espadilha","7_Copas","7_Paus",
    "8_Ouros","8_Espadilha","8_Copas","8_Paus",
    "9_Ouros","9_Espadilha","9_Copas","9_Paus",
    "10_Ouros","10_Espadilha","10_Copas","10_Paus",
    "J_Ouros","J_Espadilha","J_Copas","J_Paus",
    "Q_Ouros","Q_Espadilha","Q_Copas","Q_Paus",
    "K_Ouros","K_Espadilha","K_Copas","K_Paus"
]
bigB = "BB"
smallB = "SB"
hand = []
y = 8




def newGame():
    random.shuffle(cards)
    player_1= [x, cards[0], cards[1]]
    player_2= [x, cards[2], cards[3]]
    player_3= [x, cards[4], cards[5]]
    player_4= [x, cards[6], cards[7]]

    print(f"Sua quantidade de fichas é :", x)
    print(f"Sua mão inicial é: ",player_1[1], ",", player_1[2])

    

def setCardsinTable():
    table = []
    table.append[cards[y]]
    y += 1
        
def questionRound():
    #if 
    response = input("1 -Pass,"
                         "2 -To Cover,"
                         "3 -Increase,"
                         "4 -Get Away")
    print(response)


#def verifyRoundStts():
    





newGame()
questionRound()
