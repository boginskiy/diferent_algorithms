from collections import deque


stack = deque([1, 2, 3])

stack.appendleft(0)
stack.appendleft(-1)

value = stack.popleft()

print(value)
print(stack)
