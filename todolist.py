todolist = ['eat', 'watch tv', 'sleep']

task = input("What is the task? ")
priority = input("What is the priority of the task? ")

if priority == "high":
     todolist[0:0]=(task)
elif priority == "normal":
     todolist.append=(task)


print("The top three tasks are " +str(todolist))

