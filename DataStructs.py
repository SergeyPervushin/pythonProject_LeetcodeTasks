# Вспомогательный класс Node для решения задач Leetcode на связные списки
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    # делаем из списка питон связный список из его элементов по порядку
    def Linked_List_by_input_list(input_list):
        if len(input_list) <= 1:
            head = ListNode(input_list[0])
            return head
        input_list.reverse()
        end = ListNode(input_list[0])
        for i in range(1, len(input_list)):
            head = ListNode(input_list[i])
            head.next = end
            end = head
        return head

    @staticmethod
    def out_linked_list(head):
        out = []
        while head is not None:
            out.append(head.val)
            head = head.next
        print(out)
