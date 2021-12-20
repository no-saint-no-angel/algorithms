class Solution:
    def ReverseSentence(self, s):
        # write code here
        s = s.strip() # 删除首尾空格
        strs = s.split(' ') # 分割字符串
        strs.reverse() # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回

# line = list(map(str, input().strip().split()))
# line = input()
line='"  hello,  world...  "'
line1 = line.split('"')[1]
word_reverse = Solution()
print(word_reverse.ReverseSentence(str(line1)))

#youzan  "  hello,  world...  "
#JZ "nowcoder. a am I"
