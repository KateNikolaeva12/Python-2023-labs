# TODO Найдите количество книг, которое можно разместить на дискете

V = 1.44  #Объем дискеты
pages = 100  #Количество страниц в книге
lines = 50  #Число строк на странице
symbols = 25  #Количество символов в строке
b = 4  #Для хранения кода одного символа
book = V//(pages*lines*symbols*b/1024/1024)
print("Количество книг, помещающихся на дискету:", int(book))
