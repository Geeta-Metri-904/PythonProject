def remove_duplicates(s):
    empty_list=[]
    for i in s:
        if i not in empty_list:
            empty_list.append(i)
    return empty_list

print(remove_duplicates([1,2,2,3,4,4,5]))