print("\n======== queue_import ========")

from queue import Queue

q = Queue()
q.put(1)
q.put(5)
q.put(10)

# 안됨.... 강의 오류...
print("my queue is : ", q)
print("removed value is : ", q.get())
print("my queue is : ", q)
# print("peeked value is : ", q.peek())
print("my queue is : ", q)
