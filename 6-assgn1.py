def test(list1):
    list2=[]
    for i in list1:
        if type(i)==int:
            list2.append(i)
        elif type(i)==list:
            for j in i:
                if type(j)==int:
                    list2.append(j)
        elif type(i)==set:
            for j in i:
                if type(j)==int:
                    list2.append(j)
        elif type(i)==dict:
            for j in i.keys():
                if type(j)==int:
                    list2.append(j) 
            for j in i.values():
                if type(j)==int:
                    list2.append(j)
                elif type(j)==list:
                    for i in j:
                        list2.append(i)
                elif type(j)==tuple:
                    for i in j:
                        list2.append(i)        
        elif type(i)==tuple:
                    for j in i:
                        list2.append(j)       
    return list2
a=test([1,2,3,4,[44,55,66,True],False,(34,56,78,89,34),{1,2,3,3,2,1},{1:34,"key2":[55,67,78,89],4:(45,21,61,34)},[56,"data science"],"machine learning"])
print(a)            
                
                