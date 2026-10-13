num = input()
nums = ""
for n in num:
    if len(nums) == 0:
        nums += n
    elif nums[0] == n:
        nums += n
    else:
        print(f"{int(nums[0])} {len(nums)}")
        nums = f"{n}"
print(f"{int(nums[0])} {len(nums)}")