"""

由于 xx 平方根的整数部分 ans 是满足 k^2 < x,因此我们可以对 k 进行二分查找，从而得到答案。

二分查找的下界为 0，上界可以粗略地设定为 x。
在二分查找的每一步中，我们只需要比较中间元素 mid 的平方与 x 的大小关系，并通过比较的结果调整上下界的范围.
由于我们所有的运算都是整数运算，不会存在误差，因此在得到最终的答案 ans 后，也就不需要再去尝试ans+1 了。

"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                # ans = mid
                l = mid + 1
            else:

                r = mid - 1
                ans = mid
        return ans

"""
    时间复杂度: O(log(n))
    空间复杂度：0（1）
"""
if __name__ == '__main__':
    num = 6
    s = Solution()
    print(s.mySqrt(num))