stack=[]
def push():
    ele=int(input("enter element:"))
    stack.append(ele)
def pop():
    if not stack:
        print("stack is empty")
    else:
        stack.pop()
        print("element deleted sucessfully")
def peek():
    if not stack:
        print("stack is empty")
    else:
        print("Top element is:",stack[-1/])
def display():
    if not stack:
        print("stack is empty")
    else:
        print("the elements are:")
        for i in stack:
            print(i,end=" ")
while(1):
    print()
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.DISPLAY")
    print("5.EXIT")
    c=int(input("enter your choice:"))
    if c==1:
        push()
    if c==2:
        pop()
    if c==3:
        peek()
    if c==4:
        display()
    if c==5:
        break
    if c>5:
        print("invalid choice")
    