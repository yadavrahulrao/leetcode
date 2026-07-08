def swap(n):
    s = list(str(n))
    max_num = n
    min_num = n
    length = len(s)

    for i in range(length):
        for j in range(i + 1, length):
            t = s[:]
            t[i], t[j] = t[j], t[i]

            # Leading zero not allowed
            if t[0] == '0':
                continue

            num = int(''.join(t))

            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num

    return (max_num, min_num)