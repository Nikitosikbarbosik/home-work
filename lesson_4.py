# Задание 1 Урок 4
string = input("Введите строку: ")
max_len = 0
current_len = 0
max_sequence = ""
for char in string:
    if char == "н":
        current_len += 1
    if current_len > max_len:
        max_len = current_len
        max_sequence = "н" * max_len
    else:
        current_len = 0
    if char == "!":
        string = string.replace("!", ".")
print("Самая длинная последовательность букв 'н':", max_sequence)
print("Преобразованная строка:", string)

#Задание 2 урок 4 
print(input().split("(")[-1].split(")")[0])

Задание 3
text = input('введите текст ')
 
print(list(filter(lambda x: x.startswith("а"), text.split())))
print(list(filter(lambda x: x.endswith("я"), text.split())))
