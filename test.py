from Queue.Deque import Deque


d = Deque([2,3,4,5])

while d.size()>0:
    front = d.delete_front()
    rear = d.delete_rear()
    print(front+rear)
