number = 512
dig1 = number % 10
dig2 = ((number % 100) - (number % 10))/10
dig3 = ((number % 1000) - (number % 100))/100
sum = dig1 + dig2 + dig3
print('{}+{}+{}={}'.format(dig1, dig2, dig3, sum))