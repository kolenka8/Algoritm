### Сложность данной программы O(n) ###
def remove(skob): # skob - строка со скобками
    result = ''
    storage = []
    trash = '' # trash используется для хранения предыдущего значения
    for s in skob:
        if s == '(':
            storage.append(s)
        else:
            storage.pop()
        trash += s
        # если storage пуст, это означает, что у нас есть допустимая декомпозиция.
        # убираем внешние скобки, помещаем его в result и очищаем корзину.
        if not storage:
            result += trash[1:-1]
            trash = ''           
    return result # возвращает строку после удаления крайних скобок каждой строки в разложении.