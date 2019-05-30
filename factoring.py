def factoring(number):
    factor = []
    radix = 2
    exponent = 0
    while radix * radix <= number:
        while number % radix == 0:
            number //= radix
            exponent += 1
        if exponent > 0:
            factor.append([radix, exponent])
        radix += 1
        exponent = 0
    if number > 1:
        factor.append([number, 1])
        return factor


target = int(input('素因数分解したい数値を入力してください：'))
print(factoring(target))