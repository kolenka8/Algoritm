### Сложность данной программы O(n*log(n)) ###
def minDifr(arr): # arr - массив различных целых чисел.
        result, min = [], 10**6
        arr.sort()                      # sort() помогает найти разницу между 2 числами рядом друг с другом, 
        for i in range(len(arr)-1):     # и если это минимум, то мы находимся на правильном пути. 
            if arr[i+1] - arr[i] < min:
                result = [[arr[i], arr[i+1]]]
                min = arr[i+1] - arr[i]
            elif arr[i+1] - arr[i] == min:
                result.append([arr[i], arr[i+1]])
        return result # возвращает список пар в порядке возрастания по отношению к парам.