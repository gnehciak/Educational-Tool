def qr_formula(in_a, in_b, in_c):

    discrim = int(in_b * in_b - (4 * in_a * in_c))
    # No solution
    if discrim < 0:
        print("No solution")
        return True, 1, discrim

    n = discrim ** 0.5
    # Perfect Square
    if n == int(n):
        return False, n, 0

    # Simplify
    for i in reversed(range(2, discrim + 1)):
        if discrim % (i * i) == 0:
            print(f"±√{discrim} = ±{i}√{int(discrim / (i * i))}")
            return True, i, int(discrim / (i * i))

    # Surd
    return True, 1, discrim


def simplify_qr_fraction(in_a, in_b, in_c):
    i = in_c
    while i > 0:
        if in_a % i == 0 and in_b % i == 0 and in_c % i == 0:
            return int(in_c / i), int(in_a / i), int(in_b / i), i
        i -= 1
    return in_a, in_b, in_c, 1


def simplify_fraction(in_a, in_b):
    i = b
    while i > 0:
        if a % i == 0 and b % i == 0:
            return str(a / i) + "/" + str(b / i)
        i -= 1

    return str(a + b)


print("ax^2 ±√b^2 - 4ac / 2a")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print(f"-{b}±√{b}*{b} - 4*{a}*{c} / 2*{a}")


isSurd, surdSimplify, surd = qr_formula(a, b, c)
print(f"Is Surd: {isSurd}")

if surd == 0:
    print(f"{-b}±{surdSimplify} / {2 * a}")
elif surdSimplify == 1:
    print(f"{-b}±√{surd} / {2 * a}")
else:
    print(f"{-b}±{surdSimplify}√{surd} / {2 * a}")

finalDenominator, finalNumerator, surdMultiple, multiple = simplify_qr_fraction(-b, surdSimplify, 2 * a)

Denominator = " / " + str(finalDenominator)
Numerator = str(finalNumerator)
SurdM = str(surdMultiple)
Surd = "√" + str(surd)

if finalDenominator == 1:
    Denominator = ""
if surdMultiple == 1 and surd != 0:
    SurdM = ""
if surd == 0:
    Surd = ""
print(Numerator + "±" + SurdM + Surd + Denominator + "  " + "(/", multiple, ")", sep='')
print()
x1 = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)

print(f"({x1} : {x2})")
print(f"({round(x1, 2) if round(x1, 2) != int(round(x1, 2)) else int(round(x1, 2))} : {round(x2, 2) if round(x2, 2) != int(round(x2, 2)) else int(round(x2, 2))})")
if not isSurd:
    print(f"{simplify_fraction(-b / multiple + surdMultiple, finalDenominator)} : {simplify_fraction(-b / multiple - surdMultiple, finalDenominator)}")
print()
print(Numerator + "±" + SurdM + Surd)
equationLength = len(Numerator + "±" + SurdM + Surd)

if finalDenominator != 1:
    i = equationLength
    while i > 0:
        print("-", end='')
        i -= 1
    print()
    for i in range(int(equationLength / 2)):
        print(' ', end='')
    print(finalDenominator)

input()