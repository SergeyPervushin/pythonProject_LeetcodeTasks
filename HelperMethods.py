import collections


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


def bin_search_for_34_first_index(nums, target):
    start = 0
    end = len(nums) - 1
    index = -1

    while start <= end:
        mid = start + (end - start)//2
        if target == nums[mid]:
            index = mid
        if target <= nums[mid]:
            end = mid - 1
        if target > nums[mid]:
            start = mid + 1
    if nums[index] == target:
        return start
    return -1


def bin_search_for_34_last_index(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start)//2
        if target < nums[mid]:
            end = mid - 1
        if target >= nums[mid]:
            start = mid + 1
    if nums[end] == target:
        return end
    return -1


def pattern_of_string(s: str):  # return dict like this: {number of letters: (index_1, index_2, index_n) }
    count_dict = collections.Counter(s)
    indexes = []
    output_dict = {}
    for item in count_dict.keys():
        tmp = [i for i, ltr in enumerate(s) if ltr == item]
        indexes.append(tmp)
    for i, item in enumerate(count_dict.keys()):
        output_dict[item] = indexes[i]

    return list(output_dict.values())


