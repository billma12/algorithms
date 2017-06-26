class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.cur = self.head
        self.count = 0
        print('Linked List Created')

    def insert(self, val):
        self.cur.next = ListNode(val)
        self.cur = self.cur.next
        self.count += 1
        print('Inserting', val)

    def delete(self, val):
        pass

    def reverse(self):
        pass

    def sort(self):
        pass

    def search(self, val):
        pass

    def size(self):
        return self.count

    def print(self):
        self.dummy = self.head.next
        print('[', end='')
        while(self.dummy):
            print(self.dummy.val, '-> ', end='')
            self.dummy = self.dummy.next
        print('None]')

# test below

ll = LinkedList()

ll.print()
ll.insert(5)
ll.insert(2)
ll.print()
print(ll.size())
