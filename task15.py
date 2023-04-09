minim = 5
maxim = 5
for i in 5, 1, 6, 5, 9:
    if i < minim:
        minim = i
    elif i > maxim:
        maxim = i
print (minim)
print (maxim)



# n = int(input('Введите число n: '))
# maxWeight = 0
# minWeight = 100
# i = 1
# while i <= n:
#    countWeight = int(input('Введите вес арбуза: '))
#    if countWeight > maxWeight:
#        maxWeight = countWeight
#    if countWeight < minWeight:
#        minWeight = countWeight
#    i += 1
# print(maxWeight)
# print(minWeight)