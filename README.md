# LeetCode-
## 腾讯面试50题刷题计划
### Task1：
* 思路：设置一个栈，根据栈的后进先出的特性，将匹配成功的连续开闭括号从栈中删除，如果开闭括号不匹配，则错误，若最后栈不空，也错误。
* 代码：
```python
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    1. 左括号必须用相同类型的右括号闭合。
    2. 左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in mapping:
                TopElement = stack.pop() if stack else "#"
                if mapping[char] != TopElement:
                    return False
            else:
                stack.append(char)
        return not stack
```
### Task2：
* 思路：设置一个小型堆，保证堆的大小为k, 然后取堆顶元素为返回结果，时间复杂度为O(nlog(k))。
* 代码：
```python
"""
在未排序的数组中找到第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
"""
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap =[]
        for num in nums[:k]:
            heapq.heappush(heap,num)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
        return heap[0]
```
### Task3：
* 思路：采用分治算法，对每个节点进行比较，时间复杂度为O(Nlog2(K))。
* 代码：
```python
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        amount = len(lists)
        if amount == 0:
            return None
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next
```
