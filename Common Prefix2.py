def common():
    v = ["flower", "flow", "flight"]

    ans = ""

    s = sorted(v)

    first = s[0]
    last = s[-1]

    for i in range(min(len(first), len(last))):
        # min( len(first), len(last) )
        # min between 6
        # which is 0
        if first[i] != last[i]:
            return ans

        ans += first[i]

    return ans


print(common())
