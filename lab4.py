#Q.4 Store and manipulate data using different data structures.

# #Array
# Age =[25,27,21,29,22]

# #Manipulate
# Age.append(27)
# Age.append(24)
# Age.append(26)
# Age.remove(29)

# Age[1]=22
# print("Age :",Age)



# #Stack
# name =[]

# name.append("Mohit kumar")
# name.append("Vinay Kaushik")
# name.append("Ankur Kumar")
# name.append("Raja Babu")
# name.append("Dipak Kumar")
# name.pop()
# print("Name :",name)


#Queue

from collections import  deque

queue =deque()

queue.append("Cr1")
queue.append("Cr2")
queue.append("Cr3")
queue.append("Cr4")
queue.append("Cr5")

print(queue.pop())
print(queue.popleft())
print(queue)
