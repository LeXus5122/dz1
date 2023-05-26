def can_break_chocolate(n, m, k):
    if k > n * m:
        return "no"

    if k % n == 0 or k % m == 0:
        return "yes"
    else:
        return "no"

n = int(input("Введите количество долек по длине шоколадки: "))
m = int(input("Введите количество долек по ширине шоколадки: "))
k = int(input("Введите количество долек, которое нужно отломить: "))
print(can_break_chocolate(n, m, k))
