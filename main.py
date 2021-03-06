
# sıralama
def bubbleSort(array):
    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i+1] < array[i]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

    result = []

    for i in range(len(array)):
        result.append(array[i])

    return result


# ortalama bulma
def mean(array):
    sum = 0
    for i in range(len(array)):
        sum = sum + array[i]
    result = sum/len(array)

    return result


# ortanca bulma
def median(array):
    array = bubbleSort(array)
    result = 0

    if len(array) % 2 == 0:
        medianorder = (int)(len(array)/2-1)
        result = (array[medianorder] + array[medianorder+1])/2
    else:
        medianorder = (int)((len(array)+1)/2-1)
        result = array[medianorder]

    return result


# En çok tekrar edeni bulma
def mode(array):
    most = 0
    returnvalue = 0
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count = count + 1
        if count > most:
            returnvalue = array[i]
            most = count
    return returnvalue
