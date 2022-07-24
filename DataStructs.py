

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} --> {self.next}'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.left} <-- {self.val} --> {self.right}'

    @staticmethod
    def inOrder(root):
        if root:
            print(root.val)
            root.inOrder(root.left)
            root.inOrder(root.right)


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


def binary_search_for_all_steps(nums, target):
    begin = 0
    end = len(nums) - 1
    while begin <= end:
        mid = begin + (end - begin)//2

        if nums[mid] >= target:
            end = mid - 1
        if nums[mid] < target:
            begin = mid + 1
    if nums[begin] == target:
        return begin
    return -1


def binary_search_for_quick_find(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > target:
            end = mid - 1
        if nums[mid] < target:
            start = mid + 1
    return False
