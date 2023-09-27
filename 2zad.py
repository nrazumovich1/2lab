def esli_kollekciya(arg):
    if type(arg) == list:
        print("Изначальный список: ", arg)
        arg = set(arg) # преобразовали во множество чтобы удалить повтор
        listik = list(arg)
        sum_after_positive = 0
        positive_found = False
        for num in listik:
            if num > 0 and not positive_found:
                positive_found = True
            elif positive_found:
                sum_after_positive += num
        if sum_after_positive == 0:
            print('нет положительных')
        else:
            print('Cумма после первого положительного элемента', sum_after_positive)
        print('Новый список без повторений:', listik)
    elif type(arg) == dict:
        val_list = list(arg.values())
        val_list.sort()
        for i in range(3):
            print(val_list[i])
    elif type(arg) == int or type(arg) == float:
        if arg <= 1:
            print(arg, "не является простым числом")
        else:
            is_prime = True
            for i in range(2, int(arg ** 0.5) + 1):
                if arg % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(arg, "является простым числом")
            else:
                print(arg, "не является простым числом")
    elif type(arg) == str:
        words = arg.split()  # разбиваем строку на слова
        longest_word = ""
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
        print("Самое длинное слово в строке:", longest_word)

while 1:
    print('1. Cписок\n'
          '2. Cловарь\n'
          '3. Число\n'
          '4. Строка\n'
          '5. Конец\n')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        prinarg = [-1, -2, 3, 3, -5, 2, 4, 6]  # принимаемый аргумент
        esli_kollekciya(prinarg)
    elif choice == '2':
        prinarg = {'first': 100, 'sec': 7, 'tri': 32, 'myka': 9, 'fifa': 5}
        esli_kollekciya(prinarg)
    elif choice == '3':
        prinarg = 29
        esli_kollekciya(prinarg)
    elif choice == '4':
        prinarg = 'Расчувствовавшаяся Лукерья расчувствовала нерасчувствовавшегося Николку'
        esli_kollekciya(prinarg)
    elif choice == '5':
        print("good bye")
        break
    else:
        print('Неверно выбран пункт меню')
