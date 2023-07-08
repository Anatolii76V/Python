while True:
    try:
        a = int(input('Введите положительное число не больше 100000: '))
        if a < 0 or a > 100000:
            print('Вы ввели не допустимое значение. ')
        else:
            num = True
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    num = False
                    break
            if num:
                print('Число является простым. ')
            else:
                print('Число является составным. ')
        break
    except ValueError:
        print('Ошибка: Введите целое числовое значение .')
