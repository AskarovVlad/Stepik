import sys


class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        end = ListObject(obj)
        head = self
        self.next_obj = obj
        while head.next_obj:
            head = head.next_obj
        head.next_obj = end

lst_in = list(map(str.strip, sys.stdin.readlines()))


