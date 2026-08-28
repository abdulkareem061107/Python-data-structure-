from collections import deque

s = input("Enter a string:")
dq = deque()

for i in s:
    if i.isalnum():
        dq.append(i.lower())

ispali = True
while len(dq) > 1:
    front = dq.popleft()
    rear = dq.pop()

    if front != rear:
        ispali = False
        break

if ispali:
    print("palindrome")
else:
    print("Not palindrome")
