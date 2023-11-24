gl = 10

def outer_function():
    out = 8

    def summa(a):
        loc = 5
        list = [gl,out,a,loc]
        print('Сумма = ',sum(list))

    a=int(input('введите число '))
    summa(a)

outer_function()