

class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        # list_x_reverse = list(str(x))
        #
        # # list_x_reverse = list(str(x))[::-1]
        # list_x_reversed = list(reversed(list_x))
        return list_x == list(reversed(list_x))


if __name__ == '__main__':
    a = 121

    # s_a = list(str(a))
    # s_b = [int(x) for x in str(a)]
    # s_d = list(reversed(s_b))
    # print(s_d==s_b)

    s = Solution()
    print(s.isPalindrome(a))