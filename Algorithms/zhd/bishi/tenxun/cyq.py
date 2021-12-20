class Solution:

    def FillArray(self,arr,k):

        total_zero = 0
        zero_position = []
        for i in range(len(arr)):
            if arr[i]==0:
                total_zero+=1
                zero_position.append(i)

        global total_plan
        total_plan = 0
        def dfs(a,p):
            if p>=total_zero:
                global total_plan
                total_plan+=1
            else:
                if zero_position[p]==0:
                    tmp_position_pre = 1
                else:
                    tmp_position_pre = a[zero_position[p]-1]
                if zero_position[p]==len(a)-1:
                    tmp_position_next = k
                else:
                    tmp_position_next = a[zero_position[p] +1]
                if tmp_position_next==0: tmp_position_next=k
                for i in range(tmp_position_pre,tmp_position_next+1):
                    a[zero_position[p]]=i
                    dfs(a[:],p+1)
                    a[zero_position[p]]=0

        dfs(arr,0)

        return total_plan % (10**9+7)

a = [0, 4,0,  5]
k = 6
f = Solution()
print(f.FillArray(a, k))