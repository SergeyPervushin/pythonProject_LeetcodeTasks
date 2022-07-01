

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} --> {self.next}'


# 705. DesignHashSet (Easy)
class MyHashSet:
    # Реализация через односвязный список
    def __init__(self, key=None, next_elem=None):
        self.key = key
        self.next = next_elem

    def add(self, key: int) -> None:
        if self.key is None:
            self.key = key
            self.next = None
        current = self
        new_key = MyHashSet(key)
        while current.next:
            if current.key == key:
                return
            current = current.next
        if current.key != key:
            current.next = new_key

    def remove(self, key: int) -> None:
        prev = current = self
        current = current.next
        while current:

            if prev.key == key:
                prev.key = current.key
                prev.next = current.next
                return
            else:
                current = current.next
                prev = prev.next
        if prev.key == key:
            prev.key = None

    def contains(self, key: int) -> bool:
        flag = False
        current = self
        while current:
            if current.key == key:
                flag = True
            current = current.next
        return flag

    def __repr__(self):
        return f'{self.key} --> {self.next}'

