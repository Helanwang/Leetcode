from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    for x in range(n-1):
        for y in range(x+1, n):
            if nums[x] + nums[y] == target:
                return [x, y]


result = twoSum([2, 7, 11, 15], 9)
print(result)


#  July/30/2024. first one solved !!!
