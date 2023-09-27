string = input("Введите строку: ")
words = string.split() # разбиваем строку на слова
longest_word = ""
try:
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print("Самое длинное слово в строке:", longest_word)
except:
    print("Произошла ошибка при поиске самого длинного слова.")
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")

