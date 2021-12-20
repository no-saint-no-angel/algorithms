# coding:utf-8

class Solution():

    def find(self, nums):
        heapnum = len(nums) // 2
        heap = nums[:heapnum + 1]
        for i in range(len(heap) // 2 - 1, -1, -1):  # 前n/2个元素建堆
            self.heap_adjust(i, heap)
        for j in range(heapnum + 1, len(nums)):
            if nums[j] > heap[0]:
                heap[0] = nums[j]
                self.heap_adjust(0, heap)
        # 奇数时是最中间的数，偶数时是最中间两数的均值
        return heap[0] if len(nums) % 2 == 1 else float(heap[0] + min(heap[1], heap[2])) / 2

    def heap_adjust(self, parent, heap):  # 更新结点后进行调整
        child = 2 * parent + 1
        while len(heap) > child:
            if child + 1 < len(heap):
                if heap[child + 1] < heap[child]:
                    child += 1
            if heap[parent] <= heap[child]:
                break
            heap[parent], heap[child] = heap[child], heap[parent]
            parent, child = child, child * 2 + 1


if __name__ == "__main__":
    sol = Solution()
    lists = [2, 5, 4, 9, 3, 6, 8, 7, 1]
    # lists = [1, 2]

    out_put = sol.find(lists)
    # out_put = find(lists)
    print("中位数 = %s" % out_put)