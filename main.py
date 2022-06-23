from DataStructs import *


# 2. Add Two Numbers (Medium)
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    current = ListNode()
    out = ListNode()
    out.next = current

    while l1 and l2:

        tmp_sum = l1.val + l2.val + current.val

        if tmp_sum > 9:
            current.val = int(str(tmp_sum)[0])
            current.next = ListNode(1)
        else:
            current.val = tmp_sum
            current.next = ListNode()

        l1 = l1.next
        l2 = l2.next
        current = current.next
    ListNode.out_linked_list(out.next)
    return out.next.val


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    linked_list_1 = ListNode.Linked_List_by_input_list(l1)
    linked_list_2 = ListNode.Linked_List_by_input_list(l2)

    ListNode.out_linked_list(linked_list_1)
    ListNode.out_linked_list(linked_list_2)

    print(addTwoNumbers(linked_list_1, linked_list_2))