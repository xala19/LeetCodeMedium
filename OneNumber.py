len_array = int(input())
array = []

for i in range(len_array):
    num = int(input())
    array.append(num)



for i in range(len(array) - 1):
    flag = 0
    for j in range(len(array)):
        if i != j and array[i] == array[j]:
            flag += 1
            

    if flag == 0:
        print(f'{array[i]}h')

