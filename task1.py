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