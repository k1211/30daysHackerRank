# Given an array, a , of size n containing distinct elements, sort array in ascending order using the Bubble Sort Algorithm.
# Once sorted, print the following  lines:
# swaps - the number of swaps that took place
# first_element - first element of the sorted array
# last_element - last  element of the sorted array

a = map(int,raw_input().strip().split(' '))

def bubble_sort(arr):
    swaps = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr, swaps


print "Array is sorted in " + str(bubble_sort(a)[1]) +" swaps."
print "First Element: " + str(bubble_sort(a)[0][0])
print "Last Element: " + str(bubble_sort(a)[0][len(a)-1])
