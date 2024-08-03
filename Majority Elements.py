list1 = [1, 2, 3, 1, 1, 4, 1, 1, 1, 5]

n = len(list1)
print(n/2)  # when i appears on list more than 5 times, then is majority.

list1.sort()
print(list1)
print([n//2])


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[n // 2]

