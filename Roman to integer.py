def roman_number():
    s = "MI"
    # make sure set the input to start debugg.
    # can't use inspection if you ask user input. 

    m = {"I": 1,
         "V": 5,
         "X": 10,
         "L": 50,
         "C": 100,
         "D": 500,
         "M": 1000}
    # This is the dictionary that stores the value

    # This stores the total values adds up.
    ans = 0

    for i in range(len(s)):  # scan the lengths of the answer, and set range.
        if i < len(s)-1 and m[s[i]] < m[s[i+1]]:
            # make sure that i+1 later is not out of range.
            # m[s[i]] < m[s[i+1]]: make sure that i+1 is not greater than i.
            # because it has to be minus.
            ans -= m[s[i]]
        #      if 10 < 100 = 90
        #  then 10 has to be subtracted from the total ans.
        else:
            ans += m[s[i]]
    #     if that does not happen then, just accumulate the Roman number.

    return ans


print(roman_number())
