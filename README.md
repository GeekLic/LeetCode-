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
### Task4：
* 错误思路：转化为图结构求解，时间复杂度为O(n^2)，空间复杂度上升。
* 代码：
```python
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
class Graph(object):
    def __init__(self,lists):
        self._val = lists
        n = len(lists)
        self._next = [[0]*n for i in range(n)]
        for j in range(1, n):
            for i in range(j):
                if lists[j] > lists[i]:
                    minus = lists[j] - lists[i]
                    self._next[j][i] = minus

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        G = Graph(prices)
        n = len(G._val)
        if n <= 1:
            return 0
        distance = [0] * n
        for i in range(1, n):
            cur = G._next[i]
            for j in range(i):
                cur[j] += distance[j]
            distance[i] = max(cur)
        return max(distance)
```
* 正确思路：遍历数组，只记录涨幅则为最优解。
* 代码：
```python
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit
```
### Task4_dp：
* 思路：穷举所有的状态，使用动态规划解决股票问题。
* 代码：
```python
"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        K = 2
        if n <= 1:
            return 0
        dp = [[[0] * 2 for j in range(K+1)] for i in range(n)]
        for i in range(n):
            """处理base case"""
            if i - 1 == -1:
                for k in range(K+1):
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                continue
            for k in range(1,K+1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n-1][K][0]
```
### Task13：
* 思路：通过递归找出结点的是同时在左或者同时在右，如果一左一右则父节点已经找到。
* 代码：
```python
"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        
```