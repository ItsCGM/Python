# Find the maximum subarray sum (Kadane's Algorithm).

# Subarray is a continuous part of a array.

# The no. of subarray of a arrays is equal to (n*(n+1))/2

arr_1 = [1,2,-5,-3,-4,-5,12]
arr_2 = []
arr_3 = []

i = 0 
while i<len(arr_1):
    j = len(arr_1)
    while j-2>i:
        s=(arr_1[i:j])
        arr_2.append(s)
        j-=1
    i+=1
    
for i in arr_2:
    arr_3.append(sum(i))


index = (arr_3.index(max(arr_3)))

print(arr_2[index], "and the sum is:", max(arr_3))


