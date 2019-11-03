import random
from matplotlib import pyplot as plt
import os

def CoinThrow(num_times, arch_num):
    coin1 = 0
    coin2 = 0
    coin3 = 0
    coin4 = 0
    x0_fi = 0
    x1_fi = 0
    x2_fi = 0
    x3_fi = 0
    x4_fi = 0
    x0_fi_sum = 0
    x1_fi_sum = 0
    x2_fi_sum = 0
    x3_fi_sum = 0
    x4_fi_sum = 0
    num_fi = 0
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
        x0_fi = 0
        x1_fi = 0
        x2_fi = 0
        x3_fi = 0
        x4_fi = 0
        for k in range(0, len(data[i]), 4):
            count = []
            num_fi = 0
            for n in range(0,4):
                if int(data[i][k+n]) == 0:
                    num_fi += int(data[i][k+n])
                elif int(data[i][k+n]) == 1:
                    num_fi += int(data[i][k+n])
                
            
            if num_fi == 0:
                x0_fi += 1
            elif num_fi == 1:
                x1_fi += 1
            elif num_fi == 2:
                x2_fi += 1
            elif num_fi == 3:
                x3_fi += 1
            elif num_fi == 4:
                x4_fi += 1

            count.append(x0_fi)
            count.append(x1_fi)
            count.append(x2_fi)
            count.append(x3_fi)
            count.append(x4_fi)
        total_count.append(count)
        for i in range(0, len(total_count)):
            for n in range(0,5, 5):
                if n == 0:
                    print("x")
                    x0_fi_sum += int(total_count[i][n])
                elif n == 1:
                    print("n")
                    x1_fi_sum += int(total_count[i][n])
                elif n == 2:
                    x2_fi_sum += int(total_count[i][n])
                elif n == 3:
                    x3_fi_sum += int(total_count[i][n])
                elif n == 4:
                    x4_fi_sum += int(total_count[i][n])

    print("Fi "+ str(x1_fi_sum))
    x0_fi_sum_0 = x0_fi_sum / arch_num
    x1_fi_sum_1 = x1_fi_sum / arch_num
    x2_fi_sum_2 = x2_fi_sum / arch_num
    x3_fi_sum_3 = x3_fi_sum / arch_num
    x4_fi_sum_4 = x4_fi_sum / arch_num

    print(data)
    print(data[0][2])
    print(total_count)
    print(num_fi)
    print(x1_fi)
    print("final "+ str(x1_fi_sum_1))




a = input("How many times you want the money to be thrown: ")            
b = input("How many times you want repeat this process: ")  
CoinThrow(int(a),int(b))