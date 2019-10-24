'''
if grade >=90:
    print("A")
elif grade >=80:
    print("B")
elif grade >=70:
    print("C")
else: 
    print("F")   
'''

#midterm question 11
grades = [96, 100, 78, 56]
ans = 0 
for i in grades:
    ans = ans + i
    ans = ans/len(grades)
print(ans)


def lettergrade(scorelist):
    if grades >=90:
        print("A")
    elif grades >=87:
        print("B+")
    elif grades >=80:
        print("B")
    elif grades >=75:
        print("C+")
    elif grades >=68:
        print("C")
    elif grades >=65:
        print("D+")
    elif grades >=60:
        print("D")
    else: 
        print("F")
    
    
