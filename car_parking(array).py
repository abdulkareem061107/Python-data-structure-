queue = [None] * 5
front = -1
rear = -1
def enqueue(x):
    global front, rear
    if rear == 4:
        print("Parking lot is FULL! Insertion not possible")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = x
        print("Car is Inserted:", x)
def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("No Car is found!")
    else:
        print("Car left the queue:", queue[front])
        front += 1
def display():
    if front == -1 or front > rear:
        print("No Car is found!")
    else:
        print("List of car:",queue[front:rear+1])
print("PARKING MANAGEMENT SYSTEM....")
while(True):
    print("1,Park")
    print("2,Remove")
    print("3,Exit")
    choice=int(input("Enter a choice:"))
    if choice==1:
        n=int(input("Enter number of cars:"))
        for i in range(n):
            a=input(f"Enter Car{i+1} number:")
            enqueue(a)
        display()
    elif choice==2:
        print("Car left the queue ")
        dequeue()
        display()
    elif choice==3:
        print("End of Program......")
        break
    else:
        print("Invalid")
