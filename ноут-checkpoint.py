def gcd(a, b):
    try:
        a, b = int(a), int(b)
        while b != 0:
            a, b = b, a % b
        return a
    except ValueError:
        return "Ошибка: входные данные должны быть числами!"

print(f"НОД(16, 36) = {gcd(16, 36)}")
print(f"НОД(12, 54) = {gcd(12, 54)}")
print(f"НОД(23, 'строка') = {gcd(23, 'строка')}")
