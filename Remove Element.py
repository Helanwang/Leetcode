def remove_element(nums: list[int], val: int):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1

    return index, nums[:index]


print(remove_element([4, 1, 1, 2, 1, 3, 1, 4], 1))  # removed all the 1. return the length after removed.



