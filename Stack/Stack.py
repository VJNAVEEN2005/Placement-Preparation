stack = []

stack.append(1)
stack.append(2)

top = stack.pop()

peek = stack[-1] if stack else None

print("Top Element : " , top)
print("Peek Element : " , peek)
