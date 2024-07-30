from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    for x in range(n-1):  # Iterate through each element in the list except the last one
        for y in range(x+1, n):
            if nums[x] + nums[y] == target:  # nums[x] 7 nums[y], in here is asking for the value of the list.
                #  [] not the index anymore.
                # Check if the sum of the two elements equals the target
                return [x, y]  # return index.
            # nums[x] & nums[y] is value of the list
        # [x, y] is index


result = twoSum([2, 7, 11, 15], 9)
print(result)


#  July/30/2024. first one solved !!!
