def count_sheeps(sheep):
    contador = 0

    for item in sheep:
        if item == True:
            contador +=1

    return contador

input_list = [
    True,  True, True, True,
    True,  True, True, True ,
    True,  True, True, True,
    True,  True, True, True ,
    True,  True, True, True ,
    True,  True, True, True
]

print(count_sheeps(input_list))        