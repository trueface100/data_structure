from liststack.ListStack import*

class TwoStackQueue:
    def __init__(self):
        self.__s=ListStack()
        self.__ts=ListStack()

    def __move_elements(self,s,ts):
        while not s.isEmpty():
            ts.push(s.pop())

    def enqueue(self,x):
        self.__move_elements(self.__s,self.__ts)
        self.__s.push(x)
        self.__move_elements(self.__ts,self.__s)

    def dequeue(self):
        return self.__s.pop()

if __name__=="__main__":
    st=TwoStackQueue()
    st.enqueue(1)
    st.enqueue(2)
    st.enqueue(3)
    print(st.dequeue())
    print(st.dequeue())
    print(st.dequeue())