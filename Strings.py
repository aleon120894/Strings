# Дана строка. Определить является ли количество символов четным.
# s = 'Nisl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti.'
# ...
# > True or False

def is_even(str):
    if len(str) % 2 == 0:
        print("True")

    else:
        print("False")


is_even(s)


#Сформировать строку из 10 символов. На четных позициях должны находится четные цифры, на нечетных позициях - буквы.
# Пример корректных результатов
# '0a2b4c6d8e', '0a0a0a0a0a'

str = 'aabbccddee'

def complete_str(s):

    for i in s:
        if i % 2 == 0:



#Дана строка. Показать порядковый номер символов, совпадающих с последним символом строки.
 s = 'Nisl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti'
# 2, 12, 58, 67, 69, 71, 78

def number_symbolls(str):
    for i in str:
        pass



# Дана строка. Определите, какой символ в ней встречается раньше: 'x' или 'w'. Если какого-то из символов нет, вывести сообщение об этом.
# нужно использовать конструкцию ветвления if-elif-else

word = "waxx"

def find_x_or_w(str):

   if 'x' not in str:
       return "We don't have x "
   if 'w' not in str:
       return "We don't have w "

   for i in str:
       if i in 'xw':
           return i + " - first element"




# Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов, иначе дополнить строку символами 'o' до длины 12.

def refactor_string(str):

    if len(str) > 10:
        str[:6]
    else:
        while len(str) <= 12:
            str.append('o')


# Дана строка. Посчитать количество слов строке.

string = input("Type the sentence: ")

def count_of_words(str):
    result = str.count(' ') + 1
    return result

count = count_of_words(string)
print(count)

# Дана строка. Заменить каждый четный символ или на 'a', если символ не равен 'a' или 'b', или на 'c' в противном случае.

def even_replace(str):
    for i in str:
        if str[i] % 2 == 0:
            str.replace('a')

# Дана строка. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.

def replace(str):

    for i in str:


# Дано две строки. Сравнить совпадают ли в них первые и последние 4 символа.

s1 = input("Type string: ")
s2 = input("Type 2nd string: ")

def compare_strings(str1, str2):
    if str1[0:3] == str2[0:3]:
        return "First 4 symbols match!"
#    elif str1[0:3: -1] == str2[0:3: -1]
#        return "Last 4 symbols match!"
    else:
        return "symbols does't match!"

compare = compare_strings(s1, s2)

print(compare)
# Дана строка. Вывести средний символ в нижнем регистре.
s = 'Nisl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti.'

def upper_midle_symbol(str):
    length = len(str)
    midle = length // 2

    if length % 2 == 0:
        return "We don't have an midle symbol"
    else:
        return str[midle]


symbol = upper_midle_symbol(s)
print(symbol)



















