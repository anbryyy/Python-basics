def my_func():
    s = 0
    in_list = input('enter the numbers separated by a space or Q: ').upper().split()
    for i in in_list:
        if i == 'Q':
            return s, True
        try:
            s += int(i)
        except ValueError:
            pass
    return s, False

res = 0
while True:
    a, b = my_func()
    res += a
    print(res)
    if b:
        break