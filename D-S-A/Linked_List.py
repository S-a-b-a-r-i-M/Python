class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next: Node = next


class MyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._length = 0  # _var -> PRIVATE VARIABLE NAMING CONVENTIONAL
        print(__name__)

    # ADDING DATA TO LINKED LIST
    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        if self.head == None:
            self.tail = new_node

        self.head = new_node
        self._length += 1  # TRACKING CURRENT LIST OBJ _length

    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_beginning(data)

        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self._length += 1

    def insert(self, pos, data) -> bool:
        if self.head == None:
            return False
        if pos == 0:
            self.insert_at_beginning(data)
            return True

        pointer = self.head
        for i in range(1, pos):
            if pointer == None:
                return False
            pointer = pointer.next

        if pointer == None:
            return False
        new_node = Node(data, pointer.next)
        pointer.next = new_node
        self._length += 1
        return True

    def insert_values(self, data: list):
        if len(data) == 0:
            return

        for i in data:
            self.insert_at_end(i)

    def show(self):
        my_head: Node = self.head
        print('[ ', end='')
        while my_head is not None:
            print(my_head.data, end=' ')
            if my_head.next != None:
                print(',', end='')
            my_head = my_head.next
        print(']')

    def remove_at(self, pos: int):
        if 0 > pos >= self.length:
            return 'Index Out Of Range***'
        if pos == 0:
            data = self.head.data
            self.head = self.head.next
            return data

        pre: Node = None
        cur: Node = self.head
        for i in range(0, pos):
            pre = cur
            cur = cur.next

        pre.next = cur.next
        self._length -= 1
        return cur.data

    @property  # IS DENOTE IM GOING TO WRITE A 'GETTER METHOD'
    def length(self):
        return self._length

    # SETTER
    @length.setter  # IS DENOTE IM GOING TO WRITE A 'SETTER METHOD' . THERE IS DEPENDENCY BETWEEN GETTER TO SETTER
    def length(self, val):
        if val > 0:
            self._length = val
