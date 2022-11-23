### Сложность данной программы O(n) ###
def amount(jewels, stones): # функция принимает камни и камни (драгоценные)
        count = 0 # кол-во драг. камней
        for num in stones:
            if num in jewels:
                count+=1
        return count # возвращает кол-во камней, которые являются драгоценными камнями.