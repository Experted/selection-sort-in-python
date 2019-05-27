# selection-sort-in-python
Python Selection Sort Logic Code Example

#First declare a function selection_Sort for a list numbers.
def selection_Sort(numbers):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if numbers[j]<numbers[minpos]:
                minpos=j
        temp=numbers[i]
        numbers[i]=numbers[minpos]
        numbers[minpos]=temp
        print(numbers)

numbers=[8,3,5,7,4,6]
selectionSort(numbers)
print(numbers)
