class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize an integer k that updates the kth index of the array...
        # only when the current element does not match either of the two previous indexes. ...
        k = 0
        # Traverse all elements through loop...
        for i in nums:
            # If the index does not match elements, count that element and update it...
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k       # Return k after placing the final result in the first k slots of nums...


"""


Record: 

1: 
k = 0
k < 2
nums[0] = 8 
i = 8 

k += 1
k = 1
-- 
2: 
k = 1
k < 2

nums[1] = 8
i = 8

k += 1 
k = 2

--
nums = [8, 8, 8, 9, 9, 10, 10, 10, 11]

3: i != nums[k - 2]:
k = 2 
i = 8

nums[k-2] 
nums[2-2]
nums[0] = 8

8 == 8
no increment
--
4: i != nums[k - 2]
k = 2
i = 9 

nums[k-2]
nums[2-2]
nums[0] = 8

9 != 8
nums[k] = i

nums[2] = 8 
i = 4

replace nums[2] with 4
k += 1
k = 3

5: i != nums[k - 2]
i = 9
k = 3
nums[3-2]
nums[1] = 8
9 != 8

nums[3] = 9
replace 9
k += 1 
k = 4

6: 
i = 10
k = 4
nums[4-2]  = nums[2] = 

"""