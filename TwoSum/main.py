nums = [3, 5, 8, 15, 22]
target = 30

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] == target-nums[i]:
            print(i,j)