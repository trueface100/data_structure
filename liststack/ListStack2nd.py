class ListStack:
    def __init__(self):
        self.__stack=[]
    
    def push(self,x):
        self.__stack.insert(0,x)

    def pop(self):
        return self.__stack.pop(0)

    def top(self):
        if self.isEmpty():
            print("No element in stack")
        else:
            return self.__stack[0]

    def isEmpty(self):
        return not bool(self.__stack)

    def popAll(self):
        self.__stack.clear()

    def printStack(self):
        for i in range(0,len(self.__stack)):
            print('stack[',i,']:',self.__stack[i])