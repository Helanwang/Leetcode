def remove_element(nums: list[int], val: int):

    while val in nums:
        nums.remove(val)
    return len(nums), nums


print(remove_element([10, 4, 2, 3, 7, 7, 7, 3, 7], 7))
