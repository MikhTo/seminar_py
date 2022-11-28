#Исправляем ошибки с предыдущего семинара

#dict (словарь) - аналог map - тоже весьма популярный контейнер
some_dict = {"key1":"first value", "key2":2, "key3": ["списочек в словарике"]}

#обращение по ключу
some_dict["key1"] = "changed value"

#добавляем новую пару ключ-значение
some_dict["key4"] = "new item"

#А вот так нельзя:
#some_dict["key5"] += "don't try it!"

#Но можно так:
def item_appender(some_dict, key, val): # функция тут создана исключительно для удобства
    if key in some_dict.keys():
        some_dict[key]+=val
    else:
        some_dict[key]=val
    return some_dict

some_dict = item_appender({}, "new_key", 1)
some_dict = item_appender(some_dict, "new_key", 1)



#Давайте подробней рассмотрим функции

def simple_func(first_arg, second_arg):
    print("i just print my arguments - first: ", first_arg, " and second: ", second_arg)



simple_func(1,2)

#Если аргументов много и сложно запомнить порядок, то удобно передавать по имени:

simple_func(second_arg="still second", first_arg="still first") 

#обратите внимание, что пердаем сначала первый, потом второй аргумент
#следовательно, порядок в примере выше не важен
 

def func_with_def_arg(arg1, arg2, arg3, arg4=4): #все аргументы со значениями по умолчанию должны идти в конце
    print("Я тоже просто печатаю свои аргументы: первый - ", arg1, " второй - " ,arg2, " третий - " ,arg3, " четвертый - " ,arg4)

func_with_def_arg(1, arg3=3, arg2=2)# заметьте: первый аргумент передали по значению,
#второй и третий - по имени, четвертый - никак (т.е. значение по умолчанию)
# Если хотим комбинировать ращные методы передачи, то ВСЕГДА сначала передаем по позиции, а потом по имени!


def func_with_many_args(arg1, arg2, *args):
    print("Первый аргумент: ", arg1, " второй аргумент: ", arg2, " остальные: ", args)
    print("если хотим избавиться от '[]', то пишем перед args '*': ", *args)

func_with_many_args(1, 2, "another", 1, "argument")

def func_with_many_named_args(arg1, arg2, **kwargs):
    print("Первый аргумент: ", arg1, " второй аргумент: ", arg2, " остальные: ", kwargs)


func_with_many_named_args(1, 2, firstn = "many", secondn = "named", thirdn = "arguments")

#Контрольные вопросы?


# работа с файлами

#откываем файл
f = open("test_read.txt", "r", encoding = "utf-8") # encoding - необязательный параметр
# 'r' - чтение, 'w' - запись (старое содержимое файла стирается), 'a' - дозапись

#можно считать так:
text = f.read()

#А можно так:
text = []
for line in f:
    text.append(line)

f.close()

#чтобы не забывать закрыть файл можно его открыть с помощью with as

with open("test_read.txt", encoding="utf-8") as tr, open("empty_file.txt", "w", encoding="utf-8") as ef:
    text = " ".join(tr) #данный метод создает строку,
    #составленную из элементов контейнера, разделенных исходной строкой
    ef.write(text)


#Строки

#Стоки - набор символов в кавычках:

some_string = "это какая-то строка"

#работа с ними похожа на работу с массивом
print(some_string[2]) #Получаем третий символ

print(some_string[::-1]) #Используем слайсинг

# Однако строки в python неизменяемы:
#some_string[2] = "a" # если разкомментировать, то возникнет ошибка!

# менять строки нельзя, но можно создавать новые с нужными изменениями

some_string = some_string[:2]+"*"+some_string[3:]

some_string = some_string.replace("*", "о", 1)

print(some_string.split("-")) #разделяем по разделителю

index = some_string.find("то", some_string.find("о"))

amount = some_string.count("о")

#очень полезная функция, можно создать счетчик

counter = {symb:some_string.count(symb) for symb in set(some_string)}

another_string = "\n    куча пробельных символов вокруг \n\t"

another_string = another_string.strip()

#raw-строки

raw_string = r'\n любые спец символы теперь просто символы \n\t'

#часто при описании работы r-строк говорят, что специальные символы экранируются 
#raw-строки применяются в регулярных выражениях

#вот так, кстати, подключаются библиотеки
import re

#давайте создадим патерн, чтобы узнать, как много у Ландау слов "очевидно"
pattern = r"\b([оО]чевидно)\b" #\b - знак конца слова
# [] - подходит любой из символов внутри скобок
# () - группировка, чтобы в ответ попало то, что внутри скобок

#чтобы вызвать функцию из библиотеки нужно перед ней, разделяя точкой, имя самой библиотеки

obv = re.findall(pattern, text)
print("слов очевидно: "+ str(len(obv)) + " станиц: 515 => уровень очевидности: "+ str((len(obv)/515)*100) + "%")

#Маловато! Давайте заменим все слова, начинающиеся с "о" и заканчивающиеся на "о" словом "очевидно"

pattern = r"\b([Оо][а-яА-Я]*о)\b" #[а-яА-Я] - любая русская буква, * - любое количество
# P.s. для поиска английских можно использовать \w - очень удобно

text = re.sub(pattern, "очевидно", text)

obv = re.findall(r"\b([оО]чевидно)\b", text)
print("Новый уровень очевидности: " + str((len(obv)/515)*100) + "%")

#Как видете, очень удобно!
# другие полезные обозначения:
# * - сколько угодно символов, + - один или больше, ? - один или ноль
# . - любой символ, \w - любая англ. буква, \d - любая цифра, \s - любой пробел
# Это, конечно, далеко не все возможности регулярок

#однако стоит помнить, что легко ошибиться в создании паттерна
#Одно из мудрейших изречений:

# Некоторые люди, сталкиваясь с проблемой, думают: 
# «Я знаю, я буду использовать регулярные выражения!». 
# Теперь у них две проблемы.

#f-строки
# Когда мы высчитывали, уровень очевидности Ландау, приходилось писать сл. выражение
# print("слов очевидно: "+ str(len(obv)) + " станиц: 515 => уровень очевидности: "+ str((len(obv)/515)*100) + "%")
# Неудобно!
# для таких целей придуманы форматирванные строки

print(f"слов очевидно:{len(obv)}  станиц: 515 => уровень очевидности: {(len(obv)/515)*100}%")

#Возможности форматированнния гораздо шире, чем просто подстановка значений

#можно указывать ширину
print(f"раз число: {10: 10d}, два число: {10: 5d}")

#попросить вывести знак:

print(f"десять {10}, еще десять {10:+}, минус десять {-10} ")

#или вывести с определенной точностью:
e = 2.7182818284
print(f"e: {e:.3f}, тоже e: {e:.5f}")

#это, конечно, далеко не все возможности. Остальные всегда можно отыскать в интернете 
pass


