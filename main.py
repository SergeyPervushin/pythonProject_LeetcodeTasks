from DataStructs import ListNode, MyHashSet


# 2. Add Two Numbers (Medium)
def addTwoNumbers(l1, l2):
    out = ListNode()
    current = out
    add = 0

    while l1 or l2:

        if l1 is None:
            tmp = l2.val + add
        elif l2 is None:
            tmp = l1.val + add
        else:
            tmp = l1.val + l2.val + add
        if tmp > 9:  # сумма превышает 9, тогда в ответ кладем количество единиц, десятки (1) переносим
            current.val = int(str(tmp)[-1])
            add = 1

        else:
            current.val = tmp
            add = 0
        #   проверка на возможность дальнейшего прохождения по связным спискам
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
        #   проверка на возможность создания следующего элемента ответа
        if l2 or l1 is not None:
            current.next = ListNode(add)
            current = current.next

    #   при наличии переходящего "десятка" создаем еще элемент со значением add
    if add > 0:
        current.next = ListNode(add)
        current = current.next
    return out


# 23. Merge k Sorted Lists(Hard)
def mergeKLists(lists):
    if len(lists) == 0 or lists.count(None) == len(lists):
        return None
    result = ListNode()
    current = result
    mega_list = []

    for item in lists:
        while item is not None:
            mega_list.append(item.val)
            item = item.next
    mega_list.sort()
    for i in range(len(mega_list) - 1):
        current.val = mega_list[i]
        current.next = ListNode()
        current = current.next
    current.val = mega_list[-1]
    return result


#   25. Reverse Nodes in k-Group(Hard)
def reverseKGroup(head: ListNode, k):
    # Проверка пограничных значений
    if head is None:
        return None
    if head.next is None or k == 1:
        return head

    for_size = ptr = head
    SIZE = 0
    stack = []
    result = []

    while for_size:
        SIZE += 1
        for_size = for_size.next
    steps = SIZE // k

    while steps > 0:
        counter = 0
        while counter < k:
            head = head.next
            ptr.next = None
            stack.append(ptr)
            counter += 1
            ptr = head

        begin = end = stack.pop()
        while stack:
            end.next = stack.pop()
            end = end.next

        result.append([begin, end])
        steps -= 1
        for i in range(1, len(result)):
            result[i - 1][1].next = result[i][0]
        result[-1][1].next = head
    return result[0][0]


#   206. Reverse Linked List(Easy)
def reverseList(head):
    # реверс связного списка через указатель и стек
    # указатель(p1) = head, head сдвигаем на 1, p1.next --> None(отвязываем от head)
    if head is None:
        return None
    if head.next is None:
        return head

    p1 = head
    stack = []
    while head.next:
        head = head.next
        p1.next = None
        stack.append(p1)
        p1 = head
    out = head
    while stack:
        head.next = stack.pop()
        head = head.next
    return out


def reverseList_in_time(head):
    # реверс односвязного списка за О(n) с использованием трех указателей
    if head is None:
        return None
    if head.next is None:
        return head
    prev = nxt = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    head = prev
    return head


# 19.Remove Nth Node From End of List(Medium)
def removeNthFromEnd(head, n):
    result = head
    current = result
    array = []
    while current.next:
        array.append(current)
        current = current.next
    array.append(current)
    return result


if __name__ == '__main__':

    new_list_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_list_2 = ListNode(1, ListNode(2))

    n = 1
    print(removeNthFromEnd(new_list_1, n))
