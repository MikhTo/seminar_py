#Для разминки рассмотрим некоторые особенности функций в Python

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
#ВАЖНО:
#Если хотим комбинировать разные методы передачи, 
# то сначала передаем по ПОЗИЦИИ, а потом по ИМЕНИ!

#Можно создать функцию, принимающую произвольное кол-во ПОЗИЦИОННЫХ аргументов
#Функции ниже принимает 2 и больше
def func_with_many_args(arg1, arg2, *args):
    print("Первый аргумент: ", arg1, " второй аргумент: ", arg2, " остальные: ", args)
    #есть идеи, что такое args?
    print("если хотим избавиться от '[]', то пишем перед args '*': ", *args)

func_with_many_args(1, 2, "another", 1, "argument")

#Можно создать функцию, принимающую произвольное кол-во ИМЕНОВАННЫХ аргументов
def func_with_many_named_args(arg1, arg2, **kwargs):
    print("Первый аргумент: ", arg1, " второй аргумент: ", arg2, " остальные: ", kwargs)
    #есть идеи, что такое kwargs?
    pass


func_with_many_named_args(1, 2, firstn = "many", secondn = "named", thirdn = "arguments")

#Генераторы и все,все,все

#на первом же занятии мы познакомились с list comprehension
lst = [i**2 for i in range(1, 11)]
# бывает очень удобно создать такой список и итерироваться по нему, 
# выполняя какие-то преобразования

#однако список может быть очень большим
# enormous_list = [i**2 for i in range(1, 10**100+1)]
#и тогда он либо не создастся (не хватит памяти, либо будет создаваться очень долго)

#Для этих случаев удобно воспользоваться генератором:

my_gen = (i**2 for i in range(1, 10**100+1))
print(f"Тип объекта my_gen: {type(my_gen)}")

#воспользоваться им можно с помощью функции next

print(next(my_gen),end=" ")
print(next(my_gen),end=" ")
print(next(my_gen),end=" ")

#можно переберать в цикле

for next_element in my_gen:
    print(next_element, end=" ")
    if (next_element >= 100):
        break #иначе цикл будет ОЧЕНЬ долгим

#Определение, от которого не легче: генератор - это итератор, 
#который можно перебрать лишь один раз

#Итератор - это объект, который может по очереди перебирать элементы контейнера,
# при помощи функции next

#итератор можно сделать из любого контейнера или сторки
str_it = iter("\nHi!")

print(next(str_it))
print(next(str_it))
print(next(str_it))

#генераторы можно создавать, как функции

def factorail_func(n):
    fac = 1
    res = []
    for i in range(1, n+1):
        fac*=i
        res.append(fac)
    return res


def factorail_gen(n):
    fac = 1
    for i in range(1, n+1):
        fac*=i
        yield fac
        print("I'am here!")


res1 = factorail_func(10)

res2 = factorail_gen(10)

for n in res2:
    print(n)


#Работа с интернетом
import requests



