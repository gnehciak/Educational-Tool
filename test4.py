import fractions

a = fractions.Fraction(29,3).limit_denominator()
print(a)

num = int(input('Type numerator'))
dem = int(input('Type denominator'))

a = num // dem
b = num % dem
print ('The mixed number is {} and {}/{}'.format(a, b, dem))