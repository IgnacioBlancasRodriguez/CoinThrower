import random
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

num_coins = int(input("How many coins do you want to throw?: "))
num_repeat = int(input("How many times do you want to throw the coins?: "))
num_arch = int(input("How many times do you want to repeat the process?: "))
def Throw(num_coins, num_repeat, num_arch):

#Declaration of the main variables

    names = []
    coins = []
    total_coins = []
    total_process = []
    total_process_sumed = []
    media = []
    placeholder = 0
    medium = []
    final = []

#Here we simulate the throwing

    for j in range(num_arch):
        for k in range(num_repeat):
            for i in range(num_coins):
                coins.append(random.randint(0,1))
            total_coins.append(coins)
            coins = []
        total_process.append(total_coins)
        total_coins = []

#Here we sume the amount of faces

    for i in range (0, len(total_process)):
        total_process_sumed.append([])
        for j in range (0, len(total_process[i])):
            total_process_sumed[i].append([])
            for k in range(0, len(total_process[i][j])):
                placeholder += total_process[i][j][k]
            total_process_sumed[i][j].append(placeholder)
            placeholder = 0

#Here we count the how many times each amount of faces appear

    for i in range(0, len(total_process_sumed)):
        media.append([])
        for k in range (0, num_coins+1):
            media[i].append(0)
        for j in range(0, len(total_process_sumed[i])):
            for n in range(0, num_coins+1):
                if total_process_sumed[i][j][0] == n:
                    media[i][n] += 1

#Here we separete the different amount of faces in diferent groups

    for i in range (0, num_coins+1):
        medium.append([])
    for i in range(0, len(media)):
        for j in range(0, len(media[i])):
            medium[j].append(media[i][j])

#Here we do the media beteween the different simulations

    for i in range(0, len(medium)):
        for n in range(0, len(medium[i])):
            placeholder += medium[i][n]
        placeholder = placeholder / num_arch
        final.append(placeholder)
        placeholder = 0
#Here we create the names displayed
    for i in range(0, num_coins+1):
        names.append(str(i))

#Here we display the graph

    plt.title("The throwing of "+str(num_coins)+" coins "+str(num_repeat)+" times", fontdict={'fontname':'Monserrat', 'fontsize':20})
    plt.xlabel("Medium number of times the coins were facing")
    plt.ylabel("Number of coins facing")

    plt.bar(names, final)

    plt.savefig("Coin_Simulation"+str(num_coins)+str(num_repeat)+str(num_arch)+".png", dpi=300)

    plt.show()

Throw(num_coins,num_repeat, num_arch)

