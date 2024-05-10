import sys
sys.set_int_max_str_digits(100000000)
num = int(input('Type a number: '))
total = 0
for x in range(num+1):
    if x == 1:
        total = x
    else:
        total *= x
print(total)