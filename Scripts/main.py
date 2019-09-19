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
    count = []
    total_count = []

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
        data[i].remove('')
        coin1_fi = 0
        coin2_fi = 0
        coin3_fi = 0
        coin4_fi = 0
        for k in range(0, len(data[i]), 4):
            count = []
            for n in range(0,4):
                if n == 0:
                    data1 = int(data[i][k])
                    coin1_fi += data1
                elif n == 1:
                    data2 = int(data[i][k+1])
                    coin2_fi += data2
                elif n == 2:
                    data3 = int(data[i][k+2])
                    coin3_fi += data3
                elif n == 3:
                    data4 = int(data[i][k+3])
                    coin4_fi += data4
            count.append(coin1_fi)
            count.append(coin2_fi)
            count.append(coin3_fi)
            count.append(coin4_fi)
        total_count.append(count)
    print(data)
    print(data[0][2])
    print(total_count)



a = input("How many times you want the money to be thrown: ")            
b = input("How many times you want repeat this process: ")  
CoinThrow(int(a),int(b))