import random
from matplotlib import pyplot as plt
import os

def CoinThrow(num_times, arch_num):
    coin1 = 0
    coin2 = 0
    coin3 = 0
    coin4 = 0
    coin1_fi = 0
    coin2_fi = 0
    coin3_fi = 0
    coin4_fi = 0
    result = []
    data = []

    for i in range(arch_num):
        filename = "file"+str(i)+".txt"
        file1 = open(filename, "a")
        for j in range(num_times):
            result = []
            coin1 = random.randint(0,1)
            result.append(coin1)
            coin2 = random.randint(0,1)
            result.append(coin2)
            coin3 = random.randint(0,1)
            result.append(coin3)
            coin4 = random.randint(0,1)
            result.append(coin4)
            res = str(result)
            res = res.strip("[")
            res = res.strip("]")
            if num_times > 1:
                file1.write(res+", ")
            elif num_times <= 1:
                file1.write(res)
    for i in range(arch_num):
        filename = "file"+str(i)+".txt"
        file1 = open(filename, "r")
        file_content = file1.read()
        data.append(file_content.split(", "))
        file1.close()
        os.remove(filename)
        for k in range(0, len(data[i]), 4):
            for n in range(1,4):
                if n == 1:
                    coin1_fi += data[i][k]
                elif n == 2:
                    coin2_fi += data[i][k+1]
                elif n == 3:
                    coin3_fi += data[i][k+2]
                elif n == 4:
                    coin4_fi += data[i][k+3]



a = input("How many times you want the money to be thrown: ")            
b = input("How many times you want repeat this process: ")  
CoinThrow(int(a),int(b))