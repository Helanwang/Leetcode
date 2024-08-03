
from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:

    for i in range(len(flowerbed)):
        left = i == 0 or flowerbed[i - 1] == 0
        # first iteration, left side or statement is true. i == 0. But right side is wrong.
        # only after yellow it means being executed.
        right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
        # on the first iteration, the right side is true.
        # last iteration 4 == 4. edge case
        if left and right and flowerbed[i] == 0:
            # flowerbed[0] = 1, so this statement is false.
            # must have at least 3 zeros together to place a flower in the middle.
            # also not adjacent with others flower
            flowerbed[i] = 1
            n -= 1

    return n <= 0


print(canPlaceFlowers([1, 0, 1, 0, 0], 1))
