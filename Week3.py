# Given an array arr[] of positive integers, where each value represents the number of
# chocolates in a packet. Each packet can have a variable number of chocolates. There
# are m students, the task is to distribute chocolate packets among m students such that -
# i. Each student gets exactly one packet.
# ii. The difference between maximum number of chocolates given to a student and
# minimum number of chocolates given to a student is minimum and return that
# minimum possible difference.

arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5

n = len(arr)

if m == 0 or m > n:
    print(0)
else:
    arr.sort()
    min_diff = arr[m - 1] - arr[0]

    for i in range(1, n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff

    print(min_diff)

# Given a number x and an array of integers arr, find the smallest subarray with sum
# greater than the given value. If such a subarray do not exist return 0 in that case
x = 51
arr = [1, 4, 45, 6, 0, 19]

n = len(arr)
min_len = n + 1
curr_sum = 0
start = 0

for end in range(n):
    curr_sum += arr[end]
    
    while curr_sum > x:
        min_len = min(min_len, end - start + 1)
        curr_sum -= arr[start]
        start += 1

if min_len == n + 1:
    print(0)
else:
    print(min_len)

# Given an array and a range a, b. The task is to partition the array around the range
# such that the array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to
# return the modified array.
arr = [1, 4, 3, 6, 2, 1]
a = 1
b = 3

low = 0
mid = 0
high = len(arr) - 1

while mid <= high:
    if arr[mid] < a:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif a <= arr[mid] <= b:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(True)
print(arr)

# Given an array arr and a number k. One can apply a swap operation on the array any
# number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find
# the minimum number of swaps required to bring all the numbers less than or equal
# to k together, i.e. make them a contiguous subarray.
arr = [2, 1, 5, 6, 3]
k = 3
n = len(arr)

count = 0
for x in arr:
    if x <= k:
        count += 1

bad = 0
for i in range(count):
    if arr[i] > k:
        bad += 1

ans = bad

for i in range(count, n):
    if arr[i - count] > k:
        bad -= 1
    if arr[i] > k:
        bad += 1
    ans = min(ans, bad)

print(ans)

# Given an array arr[] of positive integers. Return true if all the array elements are
# palindrome otherwise, return false
arr = [111, 222, 333, 444, 555]

result = True

for num in arr:
    s = str(num)
    if s != s[::-1]:
        result = False
        break

print(result)

# Given an array arr[] of integers, calculate the median.
arr = [90, 100, 78, 89, 67]

arr.sort()
n = len(arr)

if n % 2 != 0:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

print(median)

# You are given a rectangular matrix mat[][] of size n x m, and your task is to return an
# array while traversing the matrix in spiral form.
def spiralOrder(mat):
    result = []
    if not mat:
        return result

    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1

    return result

mat1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

mat2 = [[1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]]

mat3 = [[32, 44, 27, 23],
        [54, 28, 50, 62]]

print(spiralOrder(mat1))
print(spiralOrder(mat2))
print(spiralOrder(mat3))
