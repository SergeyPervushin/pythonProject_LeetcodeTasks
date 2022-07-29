import collections

from DataStructs import ListNode, TreeNode
from HelperMethods import binary_search_for_all_steps, binary_search_for_quick_find
from HelperMethods import bin_search_for_34_first_index, bin_search_for_34_last_index
from HelperMethods import pattern_of_string


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
    if head.next is None:
        return None
    result = head
    current = result
    array = []
    while current.next:
        array.append(current)
        current = current.next
    array.append(current)
    # если нужно удалить по факту первый элемент списка, то просто result --> остальная часть минус первый эл-т
    if len(array) == n:
        result = array[-n].next
    else:
        i = len(array) - 1 - n
        array[i].next = array[i + 1].next
    return result


#   101. Symmetric Tree(Easy)
def isSymmetric(self, root) -> bool:
    if root is None:
        return True
    return isMetric(root.left, root.right)


# функция для рекурсивного вызова, вспомогательная для задачи 101
def isMetric(left, right):
    if left is None or right is None:
        return left == right
    if left.val != right.val:
        return False
    return isMetric(left.left, right.right) and isMetric(left.right, right.left)


# нужно реализовать "переключатель", так как при нахождении подстроки в строке требует проверить
# эту же строку на следующем шаге итерации
def isInterleave(s1: str, s2: str, s3: str):
    total_string = s1 + s2
    # test cases
    trigger = True
    i = 0
    j = min(len(s1), len(s2))

    for item in s3:
        if item == total_string[i]:
            i += 1
            continue
        if item == total_string[j]:
            j += 1
            continue
        else:
            trigger = False
    return trigger


# 1302. Deepest Leaves Sum(Easy)
def deepestLeavesSum(root):
    if not root:
        return
    if not root.left and not root.right:
        if root:
            [].append(root.val)
    return sum(deepestLeavesSum(root.left), deepestLeavesSum(root.right))


# 315. Count of Smaller Numbers After Self(Hard)
def countSmaller(nums):
    result = []
    sorted_nums = sorted(nums)
    for item in nums:
        tmp = binary_search_for_all_steps(sorted_nums, item)
        result.append(tmp)
        sorted_nums.pop(tmp)
    return result


# 240. Search a 2D Matrix II(medium)
def searchMatrix(matrix, target) -> bool:
    flag = False
    for item in matrix:
        flag = binary_search_for_quick_find(item, target)
        if flag is True:
            return flag
    return flag


# 167. Two Sum II - Input Array Is Sorted
def twoSum(numbers, target):
    for i in range(len(numbers) - 1):
        start = i + 1
        end = len(numbers) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if numbers[i] + numbers[mid] == target:
                return [i + 1, mid + 1]

            if numbers[i] + numbers[mid] > target:
                end = mid - 1
            if numbers[i] + numbers[mid] < target:
                start = mid + 1


# 34. Find First and Last Position of Element in Sorted Array
def searchRange(nums, target):
    if len(nums) < 1:
        return [-1, -1]
    first = bin_search_for_34_first_index(nums, target)
    last = bin_search_for_34_last_index(nums, target)
    return [first, last]


# 344. Reverse String(Easy)
def reverseString(s) -> None:
    ptr_1 = 0
    ptr_2 = len(s) - 1
    while ptr_1 <= len(s) // 2 <= ptr_2:
        s[ptr_1], s[ptr_2] = s[ptr_2], s[ptr_1]
        ptr_1 += 1
        ptr_2 -= 1
    return s


# 557. Reverse Words in a String III(Easy)
def reverseWords(s: str) -> str:
    result = []
    s_list = s.split(' ')
    for item in s_list:
        tmp = [x for x in item]
        tmp.reverse()
        result.append(''.join(tmp))
    s_result = ' '.join(result)
    return s_result


# 236. Lowest Common Ancestor of a Binary Tree
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right


def checkInclusion(s1: str, s2: str) -> bool:
    s1_counter = collections.Counter(s1)
    s1_len = len(s1)

    for i in range(len(s2) - s1_len + 1):
        if collections.Counter(s2[i: i + s1_len]) == s1_counter:
            return True
    return False


# 733. Flood Fill(Easy)
def floodFill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image
    old_color = image[sr][sc]
    stack = [(sr, sc)]
    while stack:
        i, j = stack.pop()
        if image[i][j] == old_color:
            image[i][j] = color
            if i + 1 < len(image):
                stack.append((i + 1, j))
            if i - 1 >= 0:
                stack.append((i - 1, j))
            if j + 1 < len(image[0]):
                stack.append((i, j + 1))
            if j - 1 >= 0:
                stack.append((i, j - 1))
    return image


# 695. Max Area of Island(Medium)
def maxAreaOfIsland(grid):
    def dfs(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        return 0

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                ans = max(ans, dfs(i, j))
    return ans


# 890. Find and Replace Pattern
def findAndReplacePattern(words, pattern):
    result = []
    check_ptrn = pattern_of_string(pattern)
    for item in words:
        tmp = pattern_of_string(item)
        if tmp == check_ptrn:
            result.append(item)
    return result


if __name__ == '__main__':
    words = ["badc", "abab", "dddd", "dede", "yyxx"]
    pattern = "baba"

    print(findAndReplacePattern(words, pattern))

