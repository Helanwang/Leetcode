def palindrome2(x):
    original = x
    reverse = 0

    if x < 0:
        return False

    while x != 0:
        last_digits = x % 10
        reverse = reverse*10 + last_digits
        x = x // 10

    return original == reverse


print(palindrome2(949))
print(palindrome2(121))
print(palindrome2(432))
