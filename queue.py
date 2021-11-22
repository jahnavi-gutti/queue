class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class queue:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0
    def enqueue(self,element):
        newnode=node(element)
        if self.__head is None:
            self.__head=newnode
            self.__tail=newnode
        else:
            self.__tail.next=newnode
            self.__tail=newnode
        self.__count+=1
    def dequeue(self):   
        if self.__head is None:
            print("empty")
            return
        data =self.__head.data
        self.__head=self.__head.next
        self.__count-=1
        return data
    def front(self):   
        if self.__head is None:
            print("empty")
            return
        data =self.__head.data
        return data
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size()==0
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
while q.isEmpty() is False:
    print(q.dequeue())
q.front()


"""
20
30
empty
"""
