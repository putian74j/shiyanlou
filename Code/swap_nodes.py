#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def is_empty(self):
        return not self.head

    def insert(self, position, new_element):
        if position < 0 or position > self.get_length():
            raise IndexError("insert key more than range")
        temp = self.head
        if position == 0:
            new_element.next = temp
            self.head = new_element
            return
        i = 0
        while i < position:
            pre = temp
            temp = temp.next
            i += 1
        pre.next = new_element
        new_element.next = temp

    def remove(self, position):
        if position < 0 or position >self.get_length():
            raise IndexError("remove key more than range")
        temp = self.head
        i = 0
        while temp != None:
            if position == 0:
                self.head = temp.next
                temp.next = None
                return True
            pre, temp = temp, temp.next

            i += 1
            if i == position:
                pre.next, temp.next = temp.next, None
                return

    def get_length(self):
        temp = self.head
        length = 0
        while temp != None:
            length += 1
            temp = temp.next
        return length

    def print_list(self):
        print("linked_list:")
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def initlist(self,data_list):
        self.head = Node(data_list[0])
        temp = self.head

        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def swapNodes(self, d1, d2):
        D1 = Node(d1)
        D2 = Node(d2)
        prevD1 = None
        prevD2 = None
        p1, p2 = 0, 0
        if D1 == D2:
            return
        else:

