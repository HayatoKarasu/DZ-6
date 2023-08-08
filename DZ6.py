import random

n = 40
arr = list()

for i in range(n):
    num = random.randint(1, 100)
    arr.append(num)

to_se = random.randint(1, 100)
answ = -1

arr.sort()
left = 0
right = len(arr) - 1
while left <= right and to_se >= arr[left] and to_se <= arr[right]:
    part1 = float(right - left) / (arr[right] - arr[left])
    part2 = to_se - arr[left]

    index = left + int(part1 * part2)

    if arr[index] == to_se:
        answ = index
        break
    if arr[index] < to_se:
        left = index + 1
    else:
        right = index - 1

print(arr)
print(to_se)

if answ != -1:
    print(f"Элемент найден! Его индекс: {answ}")
else:
    print("Элемент не найден!")

print()

n = 100
arr = []

for i in range(n):
    arr.append(i)

arr[1] = 0

for i in range(n):
    if arr[i] != 0:
        j = i * 2
        while j < n:
            arr[j] = 0
            j += i

for elem in arr:
    if elem != 0:
        print(elem, end = " ")


print()


str_w = "юные мутанты ниндзя чебурашки"
str_f = "ы н"
index_w = 0
index_f = 0
len_w = len(str_w)
len_f = len(str_f)

while index_w <= len_w - len_f and index_f < len_f:
    if str_w[index_w + index_f] == str_f[index_f]:
        index_f += 1
    else:
        index_w += 1
        index_f = 0

print(f"'{str_w}'")
print(f"'{str_f}'")
if index_f == len_f:
    print(f"Подстрока найдена! Ее начало тут: {index_w}")
else:
    print("Подстрока не найдена!")