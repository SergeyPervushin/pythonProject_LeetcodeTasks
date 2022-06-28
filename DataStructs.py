# Вспомогательный класс Node для решения задач Leetcode на связные списки
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} --> {self.next}'

