# 3.6 Animal Shelter
# ==============================================================================================
# An animal shelter, which holds only dogs and cats, operates on a strickly "first in, first out"
# basis. People must adopt either the "oldest" (based on arrival time) of all animals at the
# shelter, or they can select whether they would prefer a dog or a cat (and will receive the
# oldest animal of that type. They cannot select which specific animal they would like. Create the
# data structures to maintain this system and implement operations such as enqueue, dequeueAny,
# dequeueDog and dequequeCat. You may use the build-in LinkeList data structure.
# ==============================================================================================

class QueueNode(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, item):
        node = QueueNode(item)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_node = node
            self.tail = node
        
    def remove(self):
        if self.is_empty():
            raise Exception("Cannot remove - queue is empty!")
        res = self.head.data
        self.head = self.head.next_node
        return res
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        return self.head.data
            
    def is_empty(self):
        return not self.head
    
    def print_queue(self):
        print "QUEUE ====="
        node = self.head
        while node:
            print node.data
            node = node.next_node
        print "==========="

queue = Queue()
queue.add(2)
queue.add(5)
queue.add(9)
print queue.remove()
queue.print_queue()

class Animal(object):
    def __init__(self, kind):
        self.kind = kind
    
    def set_order(self, order):
        self.order = order
        
class Dog(Animal):
    def __init__(self):
        
        
class AnimalQueue(object):
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.order = 0 # timestamp
        
    def enqueue(self, animal):
        self.order += 1
        animal.set_order(self.order)
        if type(animal) is Cat:
            self.cats.enqueue(animal)
        elif type(animal) is Dog:
            self.dogs.equeue(animal)
        
    def dequeue_any(self):
        if self.cats.is_empty() and not self.dogs.is_empty():
            return self.dogs.pop()
        if self.dogs.is_empty() and not self.cats.is_empty():
            return self.cats.pop()
        if self.cats.peek().order < self.dogs.peek().order:
            return self.cats.pop()
        else:
            return self.dogs.pop()
        
    def dequeue_dog(self):
        if self.dogs.is_empty():
            raise Exception("Dog queue empty!")
        return self.dogs.remove()
        
    def dequeue_cat(self):
        if self.cats.is_empty():
            raise Exception("Dog queue empty!")
        return self.cats.remove()
    