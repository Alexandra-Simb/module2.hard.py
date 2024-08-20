def generate_pass(n):
    password = ""
    for i in range(1, n):
        for j in range(i+1, n+1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

n = int(input('Введите число от 3 до 20: '))
password = generate_pass(n)
print('Пароль:', password)