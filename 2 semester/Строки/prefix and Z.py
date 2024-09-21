def prefix_fun(s):
    l = len(s)
    P = [0 for i in range(l)]
    for i in range(1, len(s)):
        sup = P[i - 1]
        while sup > 0 and s[sup] != s[i]:
            sup = P[sup - 1]
        if s[sup] == s[i]:
            sup += 1
        P[i] = sup
    return P


def Z_fun(s):
    ln = len(s)
    z = [0 for i in range(ln)]
    l = 0
    r = 0
    for i in range(1, len(s)):

        z[i] = max(0, min(r - i, z[i - l]))
        while i + z[i] < ln and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
        if 1 + z[i] > ln:
            r = ln

    return z