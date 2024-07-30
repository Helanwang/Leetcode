def palindrome(x):
    reverse = 0
    original = x
    if x < 0:
        return False
    while x != 0:
        last_digit = x % 10
        reverse = reverse*10 + last_digit
        x //= 10

    return reverse == original


print(palindrome(121))
print(palindrome(344))

