"""

    思路：
    运用栈先进后出的思想，比较当前括号和栈顶的括号是否是一对括号，是的话，将栈顶元素弹出，否则将当前括号压入栈内。
    遍历完之后，判断栈是否为空，空返回True。
    通过哈希表来建立左右括号对应关系：key为右括号，value为左括号，这样查询 2 个括号是否对应只需 O(1) 时间复杂度；
    建立栈 stack，遍历字符串 s 并按照算法流程一一判断。
    流程：
    循环遍历，判断当前括号是否是右括号，是右括号的话，判断是否和栈顶元素匹配，匹配的话，弹出栈顶元素，否则返回false。
    不是右括号的话，把当前元素压入栈
    优化：
    1、判断第一个括号是否是右括号，最后一个元素是否是左括号，成立的话，返回false。
    2、判断传入的括号数量是否是奇数，是的话，返回false。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        dict_map = {')':'(', '}':'{', ']':'['}
        # list_str = list(str)
        # while list_str:
        queue_str = list()
        if s[0] in dict_map.keys() or s[-1] in dict_map.values():
            return False

        for i in range(len(s)):
            if s[i] in dict_map.keys() and len(queue_str)>0:
                if queue_str[-1] == dict_map[s[i]]:
                    queue_str.pop()
                else:  # 若当前括号和栈顶不匹配，直接返回False
                    return False
            else:
                queue_str.append(s[i])
        return len(queue_str) == 0


if __name__ == '__main__':
    a = "({[["
    # a = "({[[]]})"
    s = Solution()
    print(s.isValid(a))