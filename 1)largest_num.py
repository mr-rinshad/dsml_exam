nums = input("Enter numbers separated by spaces: ").split()

nums = [int(x) for x in nums]

print("Largest number:", max(nums))
