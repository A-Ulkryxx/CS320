
def same_elem(list, list_length):
    for i in range(1, list_length):
        if(list[0] != list[i]):
            return False
    return True

def repeat(list):
    if(list == None):
        return None
    
    list_length = len(list)
    if (list_length < 2):
        return None
    
    if(list_length % 2 == 1):
        if(same_elem(list, list_length)):
            return list[0]
        for val in range(2, list_length):
            if(list_length % val == 0):
                
                multiple = list_length // val
                for i in range(1, multiple - 1):
                    section_beg = val * i
                    section_end = val * (i+1)
                    if(list[0: val] != list[section_beg:section_end]):
                        break

    for div in divisors:
        section_end = div * 2
        if (list[0:div] == list[div:section_end]):
            return list[0:div]

liste = [] 
liste = [] 
list1 = [1] 
list2 = [1, 1]
list4 = [1, 1, 1, 1]
list7 = [ 1, 1, 1, 1, 1, 1, 1]
list123 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7] 
list8 = [1, 2, 3, 8, 1, 2, 3 ] 
list135 = [1, 3, 5, 1, 3, 5, 1, 3, 5] 
listab1 = [ 'a', 'b', 1, 'b', 'a', 'b', 1, 'b' ] 
listab4 = [ 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
listab3 = [ 'a', 'b', 'a', 'b', 'a', 'b']
listc = ['a', 'b', 'a', 'b', 'a', 'b', 'c']
listtwelve = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

print(repeat(liste)) # --->None
print(repeat(list1)) # --->None
print(repeat(list2)) # --> [1]
print(repeat(list4)) # --> [1, 1]
print(repeat(list7)) # --> [1]
print(repeat(list123)) # --->[1, 2, 3, 4, 5, 6, 7]
print(repeat(list8)) # --->None
print(repeat(list135)) # ---> [1, 3, 5]
print(repeat(listab1)) # ---> ['a', 'b', 1, 'b']
print(repeat(listab4))  # ---> [ 'a', 'b', 'a', 'b']
print(repeat(listab3))  # ---> [ 'a', 'b']
print(repeat(listc)) # --->None
print(repeat(listtwelve)) # --->[ 1, 2, 3, 1, 2, 3, ]



        
    # if (list_length % 2 == 1):
    #     pattern = []
    #     divisors.remove(1)
    #     divisors.remove(list_length)
    #     divisors.reverse
    #     for div in divisors:
    #         section_end = div * 2
    #         if (list[0:div] == list[div:section_end]):
    #             pattern = list[0:div]
    #     return pattern
    # else:
    #     divisors.remove(list_length)
    #     divisors.remove(1)
    #     divisors.reverse()
    #     for div in divisors:
    #         section_end = div * 2
    #         if (list[0:div] == list[div:section_end]):
    #             return list[0:div]


    # if (highest_occurence(list) == list_length):
    #     sec1_index = divisors[0]
    #     end_index = sec1_index * 2
    #     if (list[0:sec1_index] == list[sec1_index:end_index]):
    #         return list[0:sec1_index]

    # if (one_occurence(list)):
    #     return None