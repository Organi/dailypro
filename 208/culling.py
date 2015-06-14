def culling(nums):
	return " ".join([nums[i] for i, no in enumerate(nums) if no not in nums[:i]])

numbers = input().split(' ')

print (culling(numbers))
