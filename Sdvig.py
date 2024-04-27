len_array = int(input())
array = []

for i in range(1,len_array + 1):
    array.append(i)

temp = array[-1]
#array[0] = array[-1]

for i in range(len(array)-1, 0, -1):
    array[i] = array[i - 1]
array[0] = temp
  #  array[i + 1] = temp1
#array[1] = temp

print(array)
               
   