#!/usr/bin/env python3

class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None


class DLinked_List(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def get_length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur !=None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        node = Node(item)
        cur = self._head
        if self.is_empty():
            self._head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
        return False

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.get_length():
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < (pos-1):
                count = count + 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                if cur.next == None:
                    self._head = None
                else:
                    self._head = cur.next
                    cur.next.prev = None
                    cur.next = None
                return
            while cur != None:
                if cur.item == item:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                    break
                cur = cur.next






