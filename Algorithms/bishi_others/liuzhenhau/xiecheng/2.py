

class Solution:
    def combination_k(self, s, k):
        '''
        字符串 s 中选取 k(0 <= k <= len(s)) 个元素，进行组合，以列表的形式返回所有可能的组合
        s --> 输入的字符串
        k --> 选取的元素的个数

        测试结果如下：
        combination_k('abc', 2) >>> ['ab', 'ac', 'bc']

        combination_k('c', 2)   >>> []
            combination_k('c', 2) 的递归内部解释如下：
                --> combination_k('c', 2)
                    --> for i in combination_k('', 1):
                            c + i
                        # 由于 combination_k('', 1) 的返回结果是一个空列表，这 for 循环遍历不会被执行，所以返回初始设定的值 []
        '''
        # recursive basis
        if k == 0: return ['']
        # recursive chain
        subletters = []
        # 此处涉及到一个 python 遍历循环的特点：当遍历的对象为空（列表，字符串...）时，循环不会被执行，range(0) 也是一样
        for i in range(len(s)):
            for letter in self.combination_k(s[i + 1:], k - 1):
                print(letter)
                # subletters.append([s[i], letter])
                subletters += [s[i] + letter]
        return subletters


if __name__ == '__main__':
    s = Solution()
    # list_a = [1,2,4,7]
    list_a = 'abbbcd'
    print(s.combination_k(list_a, 3))