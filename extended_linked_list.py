# Written by **** for COMP9021

from linked_list_adt import *


class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self, step):
        current_node = new_head = Node()
        nd = new_head.next_node = self.head
        s = step
        while s > 1:
            j = 1
            past = current_node
            t = s-1
            while j <= t:
                past = past.next_node
                if not past:
                    past = nd
                    s -= 1
                j += 1
            tmp = past.next_node
            if not tmp:
                tmp = nd
                nd = nd.next_node
                s -= 1
            elif not tmp.next_node:
                past.next_node = nd
            else:
                past.next_node = tmp.next_node
            current_node.next_node = tmp
            current_node = tmp
        self.head = new_head.next_node