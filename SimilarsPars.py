len_array = int(input())
array = []

for i in range(len_array):
    num = int(input())
    array.append(num)

sorted_array = sorted(array)

counter = 0
for i in range(len(sorted_array) - 1):
    for j in range(i + 1, len(sorted_array)):  # Исправлены индексы
        if sorted_array[i] == sorted_array[j]:
            counter += 1

print(counter)
