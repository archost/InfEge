Библиотеки python - это набор функций, которые можно использовать точно так же, как и те, которые вы написали в программе сами.
Например, мне необходимо написать функцию, которая бы прибавляла к переменной единицу. Выглядело бы это как-то так:

    def Plus_One(n):
        return n+1
  
Я написал функцию Plus_One, которую могу дальше использовать в своей программе, например, создать переменную a и прибавить к ней единицу:

    a=0
    Plus_One(a)

После этого a станет равной 1. 
Думаю, принцип работы функций понятен, а также понятно, что в нее можно засунуть любой функционал, будь то вычисление НОД чисел или перевод в другую систему счисления.
InfEge будет обычной библиотекой, в которой будут собраны функции, облегчающие написание экзамена, и не только, думаю добавить туда еще много интересных вещей.
Библиотеки скачиваются с помощью pip. Для этого нужно открыть терминал (в винде это Win+R -> cmd) и написать pip install [название библиотеки].
После этого нужно импортировать библиотеку в свою программу. Существует несколько способов это сделать, вот два из них:

1)import [название библиотеки]

после того, как вы написали это в своей программе, вы можете использовать функции из этой библиотеки таким образом: [название библиотеки].[название функции]
то есть доступ к функции определенной библиотеки осуществляется через точку. Например:

    import math #библиотека math
    math.pi #вернет число пи

2)from [название библиотеки] import *

Эта команда импортирует в вашу программу все функции библиотеки напрямую, и чтобы использовать их, не нужно писать название библиотеки с точкой. 
С одной стороны, это более удобно, но есть риск конфликта имен, когда встроенные функции или функции из других библиотек будут иметь такие же названия, как и в новой импортированной либе. Например:

    from math import *
    pi #вернет число пи, обратите внимание, я не писал math. но теперь мы не сможем создать свою переменную с названием pi. 

Нашу библиотеку пока нельзя скачать, но скоро будет можно. Несмотря на это, вы можете скопировать код файла infege.py, вставить в свой файл, поместить в папку с другими программами и в них прописывать import infege (или from infege import * ) и использовать функции в своей проге.

#Документацию к либе и инфу о том, как ее использовать, добавлю позже.#

В файле infege.py содержится код самой либы, скоро там будут и строки документации. В файле comments.py будут те же функции, но полностью закомментированны так, чтобы вы смогли понять, как они работают.

Далее пойдет список всех функций с кратким описанием и инструкцией к применению:

1) CC(p,k,m) - перевод числа m из сс с основанием p в сс с основанием k. То есть передается сначала изначальное основание, затем целевое, затем само число. Например, если нужно перевести число 10232 из 4-ричной в 15-тиричную, я напишу CC(4,15,10232) (функция вернет мне 10232 в 15-ричной сс). Тип возвращаемого значения - integer.
2) gcd(p,q) - нахождение НОД чисел p и q. На вход подаются два целочисленных значения. Тип возвращаемого значения - integer.
3) lcm(p,q) - нахождение НОК чисел p и q. На вход подаются два целочисленных значения. Тип возвращаемого значения - float.
4) Factor(n) - возвращает факторизацию числа n. (разложение на простые множители, причем если число p входит в разложение больше, чем в 1 степени, то оно просто повторяется. Например Factor(4) -> [2,2]) На вход подается одно целочисленное значение. Тип возвращаемого значения - list.
5) Div_Count(n) - нахождение количества делителей числа n. На вход подается одно целочисленное значение. Тип возвращаемого значения - integer.
6) Dividers(n) - возвращает список всех множителей числа n. Работает независимо от Factor(n). На вход подается одно целочисленное значение. Тип возвращаемого значения - list.
7) Task_23(start,end,multi=[],plus=[],minus=[],inc=[],ex=[]) - решение задачи 23 в общем виде. На вход подается сначала два числа - начальное и конечное значение, затем список из чисел в командах * , потом список команд + или -, затем список обязательно включаемых значений, потом исключаемых. Все, кроме начального и конечного значения, опционально. Т.е. если у вас в задаче нет условия, например, на исключение каких-то чисел, то вы просто не прописываете этот параметр. Все параметры, кроме начального и конечного значения, рекомендуется вписывать с соответствующими ключами, дабы избежать ошибок. Например: найти количество программ, переводящих число 2 в число 17, если есть команды +1, +3, * 2, * 3, и траектория должна содержать число 12, но не должна проходить через 7 и 9: print(Task_23(2,17,multi=[2,3],plus=[1,3],inc=[12],ex=[7,9])
8) Palindrome(n) - проверяет, является ли число палиндромом. На вход подается одно целочисленное значение. Тип возвращаемого значения - Boolean.
9) Prime(n) - проверяет, является ли число простым (O(sqrt(n)). На вход подается одно целочисленное значение. Тип возвращаемого значения - Boolean.

