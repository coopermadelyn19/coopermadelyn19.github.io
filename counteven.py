def count_evens(mylist):
    numeven=0
    for num in mylist: 
        if num % 2==0:
            numeven +=1

    return numeven 

# test function
print(count_evens([2,2,0]))
#it works