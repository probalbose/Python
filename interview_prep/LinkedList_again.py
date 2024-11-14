class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        h = self.head
        llstr = ''

        while h:
            llstr += str(h.data) + '-->'
            h = h.next
    
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        h = self.head
        while h.next:
            h = h.next
        
        h.next = Node(data, None)

    
    def insert_value(self, data_lst):
        self.head = None
        for data in data_lst:
            self.insert_at_end(data)

    def get_len(self):
        count = 0
        l = self.head
        while l:
            count += 1
            l = l.next
        return count

    def remove_val_at(self, index):
        if index < 0 or index >= self.get_len():
            raise Exception('Invalid index')
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_val_at(self, index, data):
        if index < 0 or index >= self.get_len():
            raise Exception('Invalid index')

        if index==0:
            self.insert_at_front(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_value(['my','name','is','Probal'])
    ll.print()
    ll.remove_val_at(2)
    ll.print()
    ll.insert_val_at(2, 'is')
    ll.print()
"""     ll.insert_at_front(3)
    ll.insert_at_front(7)
    ll.insert_at_end(9)
    ll.insert_at_end(2) """


