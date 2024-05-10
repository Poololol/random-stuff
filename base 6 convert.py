input = input('Type Num to be converted:')
input = int(input)
def ConvertToBase6(input):
    d5 = int(input/(6**4))
    input -= d5*(6**4)
    d4 = int(input/(6**3))
    input -= d4*(6**3)
    d3 = int(input/(6**2))
    input -= d3*(6**2)
    d2 = int(input/(6**1))
    input -= d2*(6**1)
    d1 = int(input/(6**0))
    return (d5*(10**4))+(d4*(10**3))+(d3*(10**2))+(d2*(10**1))+d1
def ConvertToBase6Other(input):
    d1 = input%6
    input = int(input//6)
    d2 = input%6
    input = int(input//6)
    d3 = input%6
    input = int(input//6)
    d4 = input%6
    input = int(input//6)
    d5 = input%6
    return (d5*(10**4))+(d4*(10**3))+(d3*(10**2))+(d2*(10**1))+d1
print(ConvertToBase6(input))
print(ConvertToBase6Other(input))