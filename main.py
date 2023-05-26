def sum(number):
    if number < 100 or number > 999:
        return "Число должно быть трехзначным"

    str_number = str(number)
    sum_digits = int(str_number[0]) + int(str_number[1]) + int(str_number[2])

    return sum_digits

user_input = int(input("Введите трехзначное число: "))
print(sum(user_input))
