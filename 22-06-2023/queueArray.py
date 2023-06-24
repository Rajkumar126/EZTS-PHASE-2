queue=[]
def enqueue():
    ele=int(input("enter element:"))
    queue.append(ele)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        queue.pop(0)
        print("element deleted sucessfully")
def display():
    if not queue:
        print("queue is empty")
    else:
        print("the elements are:")
        for i in queue:
            print(i,end=" ")
while(1):
    print()
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.DISPLAY")
    print("4.EXIT")
    c=int(input("enter your choice:"))
    if c==1:
        enqueue()
    if c==2:
        dequeue()
    if c==3:
        display()
    if c==4:
        break
    if c>4:
        print("invalid choice")
    