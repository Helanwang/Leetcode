nums = ([10, 20, 30, 40, 50, 60])
target = 90


def two_sum():
    n = len(nums)  # lengths of the list
    for x in range(n-1):  # iterate except for the last one
        for y in range(x+1, n):  # iterate starts from the next one.
            if nums[x] + nums[y] == target:
                return [x, y]

    return ["Nothing adds up."]


print(two_sum())  # output: [2, 5]
