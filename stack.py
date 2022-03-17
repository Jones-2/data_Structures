#implementing stack ADT using List
from inspect import stack


stack_Array=[]
"""Creating a stack list to hold user inputs"""
def push():
    x=int(input("Enter an Element "))
    stack_Array.append(x)
    print(stack_Array)

def pop_Element():
    if not stack_Array:
        raise "You have no element in the stack"
    else:
        element=stack_Array[-1]
    print("You popped", element)
    #print(stack_Array)

while True:
    print("Enter 1 to push, 2 to pop, and 3 to exit")
    choice=int(input())
    if choice==1:
        push()
    if choice==2:
        pop_Element()

    if choice==3:
        break
    else:
        print("you have to make a choice")