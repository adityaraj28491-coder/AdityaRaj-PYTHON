#Reverse list:-
l1 = [1,2,8,9,4,5]
l2 = []
for i in range (len(l1)-1,-1,-1):
    l2.append(l1[i])
print("reverse : ",l2)


# max and min
l3 = [10,20,30,40,50]
a = l3[0]
#max
for i in range (0,5):
    if (a < l3[i]):
        a = l3[i]
print("max : ",a)
b = l3[0]
#min
for i in range (0,5):
    if (b > l3[i]):
        b = l3[i]
print("min :",b)

# Given an integer array arr[] and an integer k, your task is to find and return
# the k th smallest element in the given array
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
n = len(arr)


for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

# kth smallest element
print(arr[k - 1])


# You are given two arrays a[] and b[], return the Union of both the arrays in any
# order.
# The Union of two arrays is a collection of all distinct elements present in either of
# the arrays. If an element appears more than once in one or both arrays, it should be
# included only once in the result
# Given arrays
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]


union_set = set()


for x in a:
    union_set.add(x)


for x in b:
    union_set.add(x)


union_list = list(union_set)

print(union_list)

#Given an array arr[]. The task is to find the largest element and return it
# Given array
arr = [1, 8, 7, 56, 90]

# Assume first element is the largest
largest = arr[0]


for num in arr:
    if num > largest:
        largest = num


print(largest)


#Given an array arr, rotate the array by one position in clockwise direction.
arr = [1, 2, 3, 4, 5]
last = arr[-1]

for i in range(len(arr) - 1, 0, -1):
    arr[i] = arr[i - 1]
arr[0] = last

print(arr)

#You are given an integer array arr[]. You need to find the maximum sum of a 
#subarray (containing at least one element) in the array arr[].
arr = [2, 3, -8, 7, -1, 2, 3]

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)

# Given a sorted array of distinct integers and a target value, return the index if the
# target is found. If not, return the index where it would be if it were inserted in
# order
nums = [1, 3, 5, 6]
target = 5

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(left)

# Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target.
nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(nums)):
    diff = target - nums[i]
    if diff in seen:
        print([seen[diff], i])
        break
    seen[nums[i]] = i

# You are given an array arr[] of non-negative numbers. Each number tells you
# the maximum number of steps you can jump forward from that position
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)

if n <= 1:
    print(0)
elif arr[0] == 0:
    print(-1)
else:
    jumps = 1
    maxReach = arr[0]
    steps = arr[0]

    for i in range(1, n):
        if i == n - 1:
            print(jumps)
            break

        maxReach = max(maxReach, i + arr[i])
        steps -= 1

        if steps == 0:
            jumps += 1
            if i >= maxReach:
                print(-1)
                break
            steps = maxReach - i
          
