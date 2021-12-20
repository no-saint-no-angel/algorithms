
class Solution:
    def reverseWords(self, s):
        s_list = s.split(' ')
        tmp = list()
        for i, word_ in enumerate(s_list):
            tmp_s = list(reversed(list(word_)))
            tmp.append(''.join(tmp_s))
        return ' '.join(tmp)

if __name__ == '__main__':
    str_ = "Let's take LeetCode contest"
    s = Solution()
    print(s.reverseWords(str_))