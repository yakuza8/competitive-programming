import unittest


class StackEntry:

    def __init__(self, element: int, min_value: 'StackEntry'):
        self.element = element
        self.min_value = min_value

    def __repr__(self):
        return repr('StackEntry({0})'.format(self.element))


class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

    Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = StackEntry(float('inf'), None)

    def push(self, x: int) -> None:
        if x <= self.min_value.element:
            entry = StackEntry(x, self.min_value)
            self.stack.append(entry)
            self.min_value = entry
        else:
            self.stack.append(StackEntry(x, None))

    def pop(self) -> None:
        if len(self.stack) > 1:
            last_element = self.stack.pop()
            if last_element.element == self.min_value.element:
                self.min_value = last_element.min_value
        else:
            last_element = self.stack.pop()
            self.min_value = StackEntry(float('inf'), None)

    def top(self) -> int:
        return self.stack[-1].element

    def getMin(self) -> int:
        return int(self.min_value.element)


class MinStackTest(unittest.TestCase):

    def test_case_1(self):
        min_stack = MinStack()
        min_stack.push(1)
        min_stack.push(3)
        min_stack.push(2)
        min_stack.push(-1)
        min_stack.push(6)
        min_stack.push(5)
        min_stack.push(-4)
        min_stack.push(3)
        min_stack.pop()
        min_stack.pop()
        min_stack.pop()
        min_stack.pop()
        min_stack.pop()
        min_stack.pop()
        min_stack.pop()
