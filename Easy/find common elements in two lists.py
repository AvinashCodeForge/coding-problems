def commonElements(lst1, lst2):
    result= [num for num in lst1 if num in lst2]
    print(result)
    

lst1 = [1, 2, 3]
lst2 = [2, 3, 4]
commonElements(lst1, lst2)