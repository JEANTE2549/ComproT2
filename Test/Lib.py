# %% [markdown]
# # Data Structure:
# - Array
# - Array 2D
# - Linked List (Singly, Doubly)
# 
# # ADT
# - Stack
# - Queue
# - Circular Queue
# - Double Ended Queue
# - Matrix

# %% [markdown]
# ## Array
# | properties/methods    | description    |
# | --- | --- |  
# | __Array(size)__ : | Creates a one-dimensional array consisting of size elements with each element initially set to None. Size must be greater than zero |  
# | __`__`len( )`__`__: | Returns the length of number of elements in the array |   
# | __`__`getitem`__`(index)__: | Returns the value stored in the array at element position index. The index argument must be with in the valid range. Accessed using the subscript operator |  
# | __`__`setitem`__`(index, value)__: | Modifies the contents of the array element at position index to contain value. The index must be within the valid range. Accessed using the subscript operator |    
# | __clear(value)__: | Clears the array by setting every element to value  |  
# | __`__`iter( )`__`__: | Creates and returns an iterator that can be used to traverse the elements of the array |
# | __`__`next( )`__`__: |Return the next item for next iteration |
# | __`__`repr( )`__`__: |Return all value in stored in the array as a string to represent this object |

# %%
import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, "Array must be > 0"
        self._size = size
        pyArrayType  = ctypes.py_object * size
        self._element = pyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self,index):
        return self._element[index]

    def __setitem__(self,index,value):
        self._element[index] = value  

    def clear(self,value):
        for i in range (self._size):
            self._element[i] = value

    def __repr__(self):
        s = "[ "
        for i in (self._element):
            s = s + str(i) + ", "
        s = s[:-2] + " ]"
        return s

    def __iter__(self):
        self._curIndex = 0
        return self
        
    def __next__(self):
        if self._curIndex < len(self._element):
            entry = self._element[self._curIndex]
            self._curIndex += 1
            return entry
        else:
            raise StopIteration

# %% [markdown]
# ## Array 2D
# | properties/methods  | description  |
# |---|---|
# | __Array2D(nrows,ncols)__: | Creates a two-dimensional array organized into rows and columns. The nrows and ncols arguments indicate the size of the table. The individual elements of the table are initialized to None|
# |__numRows()__: | Returns the number of rows in the 2-D array|
# | __numCols()__:| Returns the number of columns in the 2-D array|
# | __clear(value)__: | Clears the array by setting each element to the given value|
# | __`__`getitem`__`(i1,i2)__: | Returns the value stored in the 2-D array element at the position indicated by the 2-tuple (i1; i2), both of which must be within the valid range. Accessed using the subscript operator: y = x[1,2]|
# |__`__`setitem`__`(i1,i2,value)__: | Modifies the contents of the 2-D array element indicated by the 2-tuple (i1; i2) with the new value. Both indices must be within the valid range. Accessed using the subscript operator: x[0,3] = y|
# | __`__`repr( )`__`__: |Return all value in stored in the 2-D array as a string to represent this object |

# %%
class Array2D:
    def __init__(self, nRows, nCols):
        self.nRows = nRows
        self.nCols = nCols
        self._theRows = Array(nRows)
        for i in range(nRows):
            self._theRows[i] = Array(nCols)
        self.clear(None)

    def numRows(self):
        return self.nRows

    def numCols(self):
        return self.nCols

    def __getitem__(self, indexTuple): #indexTuple รับค่ามา 2 ตัว เป็น tuple
        row = indexTuple[0]
        col = indexTuple[1]
        return self._theRows[row][col]

    def __setitem__(self, indexTuple, value):
        row = indexTuple[0]
        col = indexTuple[1]
        self._theRows[row][col] = value

    def clear(self, value):
        for i in range(self.nRows):
            for j in range(self.nCols):
                self._theRows[i][j] = value
                
    def __repr__(self):
        s = ""
        for i in self._theRows:
            s += str(i) + "\n"
        return s[:-1]

# %% [markdown]
# ## Singly Linked List
# | properties/methods    | description    |
# | --- | --- | 
# | **Single_Linked_list()** | create a new single linked list without any node |
# | **prepend(item)** | add a new node to the head of linked list |
# | **append(item)** | add a new node to the tail of linked list |
# | **traverse()** | print all contained data in linked list |
# | **search(target)** | return True if target item was found in linked list, return False if target item was not in linked list | 
# | **remove(target)** | remove the first found target from linked list |
# | **isEmpty()** | return True if the linked list has no node and return False if not
# | **length()** | return the number of node contained in Linked list

# %%
class SLinkNode:
    def __init__(self, item):
        self._item = item
        self._next = None
    
class SLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def prepend(self, item):
        newNode = SLinkNode(item)
        if self.isEmpty():
            self._tail = newNode # ให้ pointer
        else:
            newNode._next = self._head # ใช้บอกว่า newNode._next ของกุเนี่ยตอนนี้เป็น self._head
        self._head = newNode # ให้ pointer head มาชี้ภายหลัง
        self._size += 1

    def append(self, item):
        newNode = SLinkNode(item)
        if self.isEmpty():
            self._head = newNode # ให้ pointer
        else:
            self._tail._next = newNode # ให้ช่องด้านหลังเป็น new node
        self._tail = newNode # ให้ pointer
        self._size += 1
    
    def __repr__(self):
        curNode = self._head
        s = "[ "
        while curNode is not None:
            s = s + str(curNode._item) + "->"
            curNode = curNode._next
        s = s[:-2] + " ]"
        return s
    
    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and (curNode._item != target):
            curNode = curNode._next
        return curNode is not None
    
    def isEmpty(self):
        return self._size == 0
    
    def remove(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode._item != item: # ใช้ search
            predNode = curNode # -> pointer 1 ไล่ ตาม curnode เก่า
            curNode = curNode._next # -> pointer 2 ไล่ไปตาม list node
        assert curNode is not None, "The item is not linked list"
        self._size -= 1
        if curNode is self._head:
            self._head = curNode._next
        elif curNode is self._tail:
            self._tail = predNode
            self._tail._next = None
        predNode._next = curNode._next # ให้ prednode next เชื่อม curnode next ได้
        return curNode._item
    
    def __iter__(self):
        self._curNode = self._head
        return self
    
    def __next__(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode._item
            self._curNode = self._curNode._next
            return item

    #--------------------------------------------------------------------------------------------------new

    def insertAt(self, index, item):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(item)
            return
        elif index == self._size:
            self.append(item)
            return
        newNode = SLinkNode(item)
        curNode = self._head
        for _ in range(index - 1):
            curNode = curNode._next
        newNode._next = curNode._next
        curNode._next = newNode
        self._size += 1

    def insertAfter(self, key, item):
        curNode = self._head
        while curNode is not None:
            if curNode._item == key:
                newNode = SLinkNode(item)
                newNode._next = curNode._next
                curNode._next = newNode
                if curNode is self._tail:
                    self._tail = newNode
                self._size += 1
                return
            curNode = curNode._next
        return None
    
    def delete(self, key):
        predNode = None
        curNode = self._hea
        while curNode is not None and curNode._item != key:
            predNode = curNode
            curNode = curNode._next
        if curNode is None:
            return None
        if curNode is self._head:
            self._head = curNode._next
        else:
            predNode._next = curNode._next
        if curNode is self._tail:
            self._tail = predNode
        self._size -= 1
        return curNode._item

    def swap(self, key1, key2):
        if key1 == key2:
            return
        prev1 = None
        prev2 = None
        node1 = self._head
        node2 = self._head
        while node1 is not None and node1._item != key1:
            prev1 = node1
            node1 = node1._next
        while node2 is not None and node2._item != key2:
            prev2 = node2
            node2 = node2._next
        if node1 is None or node2 is None:
            return
        if prev1 is not None:
            prev1._next = node2
        else:
            self._head = node2
        if prev2 is not None:
            prev2._next = node1
        else:
            self._head = node1
        node1._next, node2._next = node2._next, node1._next
        if node1 is self._tail:
            self._tail = node2
        elif node2 is self._tail:
            self._tail = node1

    def reverse(self):
        prevNode = None
        curNode = self._head
        self._tail = self._head
        while curNode is not None:
            nextNode = curNode._next
            curNode._next = prevNode
            prevNode = curNode
            curNode = nextNode
        self._head = prevNode


# %% [markdown]
# ## Doubly Linked List

# %%
class DLinkNode:
    def __init__(self, item, prev, next):
        self._item = item
        self._prev = prev
        self._next = next

class DLinkedList:
    def __init__(self):
        self._header = DLinkNode(None,None,None)
        self._trailer = DLinkNode(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def insert_between(self, item, predencessor, successor):
        newNode = DLinkNode(item, predencessor, successor)
        predencessor._next = newNode
        successor._prev = newNode
        self._size += 1

    def delete_node(self, node):
        assert not self.isEmpty(), "Doubly Linked list is empty"
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        item = node._item
        node._prev = node._next = node._item = None
        return item
    
    def isEmpty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        curNode = self._header
        s = "[ "
        while curNode is not None:
            s = s + str(curNode._item) + " <-> "
            curNode = curNode._next
        s = s[:-4] + " ]"
        return s

# %% [markdown]
# ## Matrix
# | properties/methods  | description  |
# |---|---|
# | __Matrix(rows,ncols)__: | Creates a new matrix containing nrows and ncols with each element initialized to 0 |
# | __numRows()__: | Returns the number of rows in the matrix |
# | __numCols()__: | Returns the number of columns in the matrix |
# | __clear(value)__: | Clears the matrix by setting each element to the given value|
# | __`__`getitem(row,col)`__`__: | Returns the value stored in the given matrix element. Both row and col must be within the valid range |
# | __`__`setitem(row,col,scalar)`__`__: | Sets the matrix element at the given row and col to scalar. The element indices must be within the valid range |
# | __`__`repr( )`__`__: |Return all value in stored in the matrix as a string to represent this object |
# | __scaleBy(scalar)__: | Multiplies each element of the matrix by the given scalar value. The matrix is modified by this operation |
# | __transpose()__: | Returns a new matrix that is the transpose of this matrix |
# | __add(rhsMatrix)__: | Creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix. The size of the two matrices must be the same |
# | __subtract(rhsMatrix)__: | The same as the add() operation but subtracts the two matrices |
# | __multiply(rhsMatrix)__: | Creates and returns a new matrix that is the result of multiplying this matrix to the given rhsMatrix. The two matrices must be of appropriate sizes as defined for matrix multiplication |

# %%
class Matrix(Array2D):
    def __init__(self, nRows, nCols):
        super().__init__(nRows, nCols)
        self.clear(0)

    def scaleBy(self, scalar):
        newMatrix = Matrix(self.nRows, self.nCols)
        for i in range(self.nRows):
            for j in range(self.nCols):
                newMatrix[i, j] = self._theRows[i][j] * scalar
        return newMatrix

    def transpose(self):
        newMatrix = Matrix(self.nCols, self.nRows)
        for i in range(self.nRows):
            for j in range(self.nCols):
                element = self._theRows[i][j]
                newMatrix[j, i] = element
        return newMatrix
    
    def __add__(self, rhsMatrix):
        NewMatrix = Matrix(self.nRows, self.nCols)
        for i in range(self.nRows):
            for j in range(self.nCols):
                NewMatrix[i, j] = self[i, j] + rhsMatrix[i, j]
        return NewMatrix
    
    def __sub__(self, rhsMatrix):
        NewMatrix = Matrix(self.nRows, self.nCols)
        for i in range(self.nRows):
            for j in range(self.nCols):
                NewMatrix[i, j] = self[i, j] - rhsMatrix[i, j]
        return NewMatrix
    
    def __mul__(self, rhsMatrix):
        assert self.numCols() == rhsMatrix.numRows(), \
            f"Incompatible sizes: A has {self.numCols()} cols, but B has {rhsMatrix.numRows()} rows."
        NewMatrix = Matrix(self.numRows(), rhsMatrix.numCols())
        for i in range(self.numRows()):
            for j in range(rhsMatrix.numCols()):
                total = 0
                for k in range(self.numCols()):
                    total += self[i, k] * rhsMatrix[k, j]
                NewMatrix[i, j] = total
        return NewMatrix

    #---------------------------------------------------------------------------------------------------------------------new

    def trace(self):
        if self.nRows != self.nCols:
            raise ValueError("Trace only for square matrix")
        total = 0
        for i in range(self.nRows):
            total += self[i, i]
        return total
    
    def det(self):
        if self.nRows != self.nCols:
            raise ValueError("Determinant only for square matrix")
        if self.nRows == 2:
            a = self[0,0]
            b = self[0,1]
            c = self[1,0]
            d = self[1,1]
            return a*d - b*c
        elif self.nRows == 3:
            a,b,c = self[0,0], self[0,1], self[0,2]
            d,e,f = self[1,0], self[1,1], self[1,2]
            g,h,i = self[2,0], self[2,1], self[2,2]
            return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
        else:
            raise ValueError("Only 2x2 or 3x3 supported")

    def inverse(self):
        if self.nRows != 2 or self.nCols != 2:
            raise ValueError("Inverse only for 2x2")
        determinant = self.det()
        if determinant == 0:
            raise ValueError("Matrix not invertible")
        a = self[0,0]
        b = self[0,1]
        c = self[1,0]
        d = self[1,1]
        result = Matrix(2,2)
        result[0,0] =  d / determinant
        result[0,1] = -b / determinant
        result[1,0] = -c / determinant
        result[1,1] =  a / determinant
        return result

# %% [markdown]
# ## Stack
# | properties/methods    | description    |
# | --- | --- |  
# | __Stack()__: | Creates a new empty stack.|
# | __isEmpty()__: |Returns a Boolean value indicating if the stack is empty.|
# | __length()__: |Returns the number of items in the stack.|
# | __pop()__: |Removes and returns the top item of the stack, if the stack is not empty. Items cannot be popped from an empty stack. The next item on the stack becomes the new top item.|
# | __peek()__: |Returns a reference to the item on top of a non-empty stack without removing it. Peeking, which cannot be done on an empty stack, does not modify the stack contents.|
# | __push(item)__: | Adds the given item to the top of the stack.|
# | __\_\_repr()\_\___:| Represent the values of elements keep in stack |

# %%
# implement with array
class Stack:
    def __init__(self):
        self._theItems = list()

    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._theItems)

    def peek(self):
        assert not self.isEmpty(), "Can't peek empty stack"
        return self._theItems[-1]
    
    def pop(self):
        assert not self.isEmpty(), "can't pop empty pop"
        return self._theItems.pop()
    
    def push(self, item):
        self._theItems.append(item)

    def __repr__(self):
        s = '<--'
        s = s.join([str(x) for x in self._theItems])
        return s

# %%
# implement with singly linked list
class LLStack(SLinkedList):
    def push(self, item):
        self.prepend(item) # เพราะจะ pop ด้านหน้า เลยใช้ prepend แทน append
    
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        curNode = self._head
        item = curNode._item
        self._head = curNode._next
        self._size -= 1
        return item
    
    def peek(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._head._item
    
    def __repr__(self):
        curNode = self._head
        s = "_____\n"
        while curNode is not None:
            s = s + str(curNode._item) + " \n"
            curNode = curNode._next
        s = s + "_____"
        return s

# %% [markdown]
# ## Queue
# | properties/methods    | description    |
# | --- | --- | 
# | __Queue()__: | Creates a new empty queue, which is a queue containing no items.
# | __isEmpty()__: | Returns a Boolean value indicating whether the queue is empty.
# | __length()__: | Returns the number of items currently in the queue.
# | __enqueue(item)__: | Adds the given item to the back of the queue.
# | __dequeue()__: | Removes and returns the front item from the queue. An item cannot be dequeued from an empty queue.
# | __\_\_repr()\_\___:| Represent the values of elements keep in queue |

# %%
# implement with array
class Queue:
    def __init__(self):
        self._qList = list()

    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._qList)
    
    def enqueue(self, item):
        self._qList.append(item)
        
    def dequeue(self):
        assert not self.isEmpty(), "Can't dequeue from empty queue"
        return self._qList.pop(0)

# %%
# implement with linked list
class LLqueue(SLinkedList):
    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty stack"
        curNode = self._head
        item = curNode._item
        self._head = self._head._next
        self._size -= 1
        return item

# %% [markdown]
# ## Circular Queue
# | properties/methods    | description    |
# | --- | --- | 
# | __CQueue()__: | Creates a new empty circular queue, which a circular array is used to contain the items.
# | __isEmpty()__: | Returns a Boolean value indicating whether the circular queue is empty.
# | __isFull()__: | Returns a Boolean value indicating whether the circular queue is full.
# | __length()__: | Returns the number of items currently collected in the circular queue.
# | __enqueue(item)__: | Adds the given item to the back-index position of the circular queue.
# | __dequeue()__: | Removes and returns the front item from the circular queue. An item cannot be dequeued from an empty circular queue.
# | __\_\_repr()\_\___:| Represent the values of elements keep in circular queue |

# %%
class CQueue:
    def __init__(self,  maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1 # เพราะเป็น index
        self._qArray = Array(maxSize)

    def enqueue(self, item):
        assert not self.isFull(), "Can't enqueue cause full queue"
        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize #ตัวชี้วงกลมที่ใช้ math หา #มันจะเลื่อน pointer back ไปในทุกๆการหารเศษ
        self._qArray[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Can't enqueue cause full queue"
        item = self._qArray[self._front]
        maxSize = len(self._qArray)
        self._qArray[self._front] = None # ใส่ค่า None เข้าไป 
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item

    def __len__(self):
        return self._count
    
    def isFull(self):
        maxSize = len(self._qArray)
        return self._count == maxSize
    
    def isEmpty(self):
        return self._count == 0
    
    def __repr__(self):
        s = '<--'
        s = s.join([str(x) for x in self._qArray])
        return s

# %% [markdown]
# ## Double Ended Queue (Deque)
# | properties/methods    | description    |
# | --- | --- |
# | __Deque()__: | Create a new empty deque, which no item with in.|
# | __AddFirst(item)__: | Add an item to the front of deque.|
# | __AddRear(item)__: | Add an item to the back of deque.|
# | __DeleteFirst()__: | Remove and return the first item from deque; an error occurs if the deque is empty.|
# | __DeleteRear()__: | Remove and return the last item from deque; an error occurs if the deque is empty.|
# | __First()__: | Return (but do not remove) the first item of deque; an error occurs if the deque is empty.|
# | __Rear()__: | Return (but do not remove) the last item of deque; an error occurs if the deque is empty.|
# | __isEmpty()__: | Return True if deque does not contain any items.|
# | __length()__: | Return the number of items in deque.|
# | __\_\_repr\_\_()__ : | represent the item contained in stack |

# %%
# Implement with array
class Deque(CQueue):
    def __init__(self, maxSize):
        super().__init__(maxSize)

    def addLast(self, item):
        self.enqueue(item)

    def addFront(self, item):
        assert not self.isFull(), "Can't addFront cause full deque"
        maxSize = len(self._qArray)
        self._front = (self._front - 1 + maxSize) % maxSize
        self._qArray[self._front] = item
        self._count += 1
        
    def removeFirst(self):
        return self.dequeue() # <-- use of pointer, so its O(1)

    def removeLast(self):
        assert not self.isEmpty(), "Can't removeLast cause empty deque"
        item = self._qArray[self._back]
        maxSize = len(self._qArray)
        self._qArray[self._back] = None
        self._back = (self._back - 1 + maxSize) % maxSize
        self._count -= 1
        return item

# %%
# implement with linked list
class LLDeque(DLinkedList):
    def addFirst(self, item):
        self.insert_between(item, self._header, self._header._next)
    
    def addRear(self, item):
        self.insert_between(item, self._trailer._prev, self._trailer)
    
    def deleteFirst(self):
        assert not self.isEmpty(), "Empty shi!!! wat can u delete dumb"
        return self.delete_node(self._header._next)
    
    def deleteRear(self):
        assert not self.isEmpty(), "Empty shi!!! wat can u delete dumb"
        self.delete_node(self._trailer._prev)
    
    def first(self):
        assert not self.isEmpty(), "wat do u mean by that"
        return self._header._next._item
    
    def rear(self):
        assert not self.isEmpty(), "wat do u mean by that"
        return self._trailer._prev._item

# %% [markdown]
# ## Priority Queue

# %%
class PQEntry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __repr__(self):
        return f"({self.item},{self.priority})"

class PriorityQueue:
    def __init__(self):
        self._data = []

    def isEmpty(self):
        return len(self._data) == 0

    def length(self):
        return len(self._data)

    def enqueue(self, item, priority):
        entry = PQEntry(item, priority)
        self._data.append(entry)
        i = len(self._data) - 1
        while i > 0 and self._data[i].priority < self._data[i-1].priority:
            self._data[i], self._data[i-1] = self._data[i-1], self._data[i]
            i -= 1

    def dequeue(self):
        if self.isEmpty():
            return None
        return self._data.pop(0).item

    def remove(self, key):
        for i in range(len(self._data)):
            if self._data[i].item == key:
                return self._data.pop(i).item
        return None



