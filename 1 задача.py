### Сложность данной программы O(n) ###
def steps(num): # num - число, которое мы уменьшаем до нуля.
        c = 0 # кол-во шагов
        while num!=0:
            if num%2==0: # если текущее число четное, мы делим его на 2.
                num /= 2
            else: # в противном случае вычитаем один.
                num -= 1
            c +=1
        return c # возвращает количество шагов, чтобы уменьшить число до нуля.
