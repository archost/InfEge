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

Далее пойдет список всех функций с кратким описанием и инструкцией к применению:

1) CC(p,k,m) - перевод числа m из сс с основанием p в сс с основанием k. То есть передается сначала изначальное основание, затем целевое, затем само число. Например, если нужно перевести число 10232 из 4-ричной в 15-тиричную, я напишу CC(4,15,10232) (функция вернет мне 10232 в 15-ричной сс). Тип возвращаемого значения - integer.
