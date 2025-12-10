class MyQueue:

    def __init__(self):
        self.stack_a = []
        self.stack_b = []
        

    def push(self, x: int) -> None:
        self.stack_a.append(x)
        

    def pop(self) -> int: # If stack_b is empty, we need to move items from stack_a
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()

        

    def peek(self) -> int:
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b[-1]
        

    def empty(self) -> bool:
        # Queue is empty only if BOTH stacks are empty
        return not self.stack_a and not self.stack_b
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()




'''
| Command   | Arguments | Meaning      |
| --------- | --------- | ------------ |
| "MyQueue" | []        | create queue |
| "push"    | [1]       | push(1)      |
| "push"    | [2]       | push(2)      |
| "peek"    | []        | peek()       |
| "pop"     | []        | pop()        |
| "empty"   | []        | empty()      |


| Operation | Return Value |
| --------- | ------------ |
| MyQueue() | null         |
| push(1)   | null         |
| push(2)   | null         |
| peek()    | 1            |
| pop()     | 1            |
| empty()   | false        |


'''