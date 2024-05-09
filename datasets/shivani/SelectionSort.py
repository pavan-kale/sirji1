def selection_sort(arr):
  for i in range(len(arr)):
    mini_Value = i
    for j in range(i+1, len(arr)):
      if (arr[j]) < arr[mini_Value]:
        mini_Value = j
    
    arr[i], arr[mini_Value] = arr[mini_Value], arr[i]

  return arr

n = int(input("Enter th number of elements: "))
my_list = []

for i in range (n):
  ele = int(input("Enter Element: "))
  my_list.append(ele)

#my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list)
print(sorted_list)