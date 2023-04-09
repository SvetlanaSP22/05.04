
# n = int (input())
# f = 1

# n = 5
# res = 1
# i = 1
# while i <= n:
#    res *= i
#   i += 1
# print(res)

a = int (input('Введите число a ='))
count = 1
result = 1
while count <= a:
    result *= count
    count += 1
    if a == 0:
        print(f"a! = 1")
print (result)


