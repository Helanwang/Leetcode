def flower():

    flowerbed = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1]
    n = 2

    for i in range(len(flowerbed)):
        left = (i == 0) or (flowerbed[i - 1] == 0)
        right = (i == (len(flowerbed) - 1)) or (flowerbed[i + 1] == 0)

        if left and right and flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True

    return n <= 0


print(flower())
