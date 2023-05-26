def lucky_ticket(number):
    if number < 100000 or number > 999999:
        return "Число должно быть шестизначным"

    str_number = str(number)
    first_three = int(str_number[0]) + int(str_number[1]) + int(str_number[2])
    last_three = int(str_number[3]) + int(str_number[4]) + int(str_number[5])

    if first_three == last_three:
        return "yes"
    else:
        return "no"

user_input = int(input("Введите шестизначное число: "))
print(lucky_ticket(user_input))
