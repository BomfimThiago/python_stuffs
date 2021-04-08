
from collections import deque

class TicketQueue():
    def __init__(self):
        self.lst = []
        self.deque = deque()

    def add_person(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person('Jack')
        Jack has been added to the queue
        """

        # first manner to do this
        self.lst.append(name)
        print(f'{name} has been added to the queue')

        #better way to do 
        # deque.append is appending the new value
        # at the right side of the deque by default
        self.deque.append(name)
        print(f'{name} has been added to the queue')

    def service_person(self):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person('Jack')
        Jack has been added to the queue
        >>> queue.service_person()
        Jack has been serviced
        """
        # first manner to do this
        name = self.lst.pop(0)
        print(f'{name} has been serviced')

        #better way to do 
        # popleft is to take out the first value
        # of the deque
        name = self.deque.popleft()
        print(f'{name} has been serviced')

    def bypass_queue(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person('Jack')
        Jack has been added to the queue
        >>> queue.bypass_queue('Jill')
        Jill has bypassed the queue
        """
        # first manner to do this
        self.lst.insert(0, name)
        print(f'{name} has bypassed the queue')

        #better way to do 
        # appendleft is to put first the value
        # in the deque
        self.deque.appendleft(name)
        print(f'{name} has been serviced')
