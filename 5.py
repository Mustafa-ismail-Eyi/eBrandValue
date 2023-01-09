# Soru 5: verilen listedeki None değerleri, kendinden önceki None olmayan değerle değiştirip yeni bir liste oluşturan fonksiyon

def replace_nones(list1 : list):

    # get the copy of list1 because question asked for new list
    new_list = list1.copy()
    prev = 0
    head = 1

    while(head < len(new_list)):
        if new_list[head] is None:
            new_list[head] = new_list[prev]
    
        head +=1
        prev +=1

    return new_list

print(replace_nones([3, None, 2, None, None, None, 'Veli', None, 10, 11, 12, None]))