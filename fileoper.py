'''
# open file 
f = open("die4.txt","rb") # text mode
t = open("mycopy.png","wb") # text mode

# read file
#print(f.read()) # string
content = "content to write"
t.write(f.read()) # string

# close file
f.close()
t.close()
'''

mylist = ["apple","book","cookie","dog"]

f = open("test.txt","a")
for i in mylist:
    # write i to file
    task = i +"\n"
    f.write(task)

print("done")
