def big_diff(mylist):
    largest = mylist[0]
    for num in mylist:
        if num > largest:
            largest = num
    
    smallest = mylist[0]
    for num in mylist:
        if num < smallest:
            smallest = num
    return largest - smallest
# test it
print(big_diff([2,10,7,2]))
#it works