
def maximum1(*args):
    
    list2= list(args)
    if list2==[]:
        return 0
    maxi=list2[0]
    list1=[]
   
    for i in list2:
        if i> maxi:
            maxi= i
            list1.append(i)
    list3=list2.remove(maxi)
    if list3==[]:
        return
    else:
     maximum1(list3)
           
maximum1(2,9,4,0,1,4)

    

    