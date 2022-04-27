from LinkedQueue import*

class TwoQueueStack_trans:
    def __init__(self):
        self.__q=LinkedQueue()
        self.__tq=LinkedQueue()
        self.__numItems=0

    def __move_elements1(self,q,tq):
        while self.__numItems>1:
            tq.enqueue(q.dequeue())
            self.__numItems-=1
    
    def __move_elements2(self,tq,q):
        while not tq.isEmpty():
            q.enqueue(tq.dequeue())
            self.__numItems+=1

    def push(self,x):
        self.__q.enqueue(x)
        self.__numItems+=1

    def pop(self):
        self.__move_elements1(self.__q,self.__tq)
        a=self.__q.dequeue()
        self.__numItems-=1
        self.__move_elements2(self.__tq,self.__q)
        return a

if __name__=="__main__":
    st=TwoQueueStack_trans()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.pop())
    print(st.pop())