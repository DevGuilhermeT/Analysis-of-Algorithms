def kdigits(k, even_s, odd_s, ans, result_size):
    if k > 0:
        digit = 0
        if ans == "":
            digit = 1
        while digit <= 9:
            if result_size % 2 == 0:
                kdigits(k - 1, even_s + digit, odd_s, ans + str(digit), result_size + 1)
            else:
                kdigits(k - 1, even_s, odd_s + digit, ans + str(digit), result_size + 1)
            digit = digit + 1
    elif k == 0 and even_s == odd_s:
        print(ans, end=" ")


k = 3
kdigits(k, 0, 0, "", 0)
