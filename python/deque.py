from collections import deque


dq = deque([1, 2, 3, 3, 4, 5])

# FIFO and LIFO

#FIFO
dq.appendleft(10)
value = dq.pop

#LIFO
dq.append(55)
value = dq.pop()

