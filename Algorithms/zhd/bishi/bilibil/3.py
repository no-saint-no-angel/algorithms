
class UnionFind(object):
    def __init__(self, n):
        self.uf = [-1 for i in range(n + 1)]
        self.sets_count = n

    def find(self, p):
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        elif self.uf[proot] > self.uf[qroot]:

            self.uf[qroot] += self.uf[proot]
            self.uf[proot] = qroot
        else:
            self.uf[proot] += self.uf[qroot]
            self.uf[qroot] = proot
        self.sets_count -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution():
    def user_pool(self, n, connections):
        user_union = UnionFind(n)
        for connection in connections:
            user_union.union(connection[0], connection[1])
        return user_union.sets_count


if __name__ == '__main__':
    c = int(input().strip())
    aa = Solution()
    for _ in range(c):
        connections = []
        line = input().strip().split()
        n, m = int(line[0]), int(line[1])
        for __ in range(m):
            line = input().strip().split()
            connections.append([int(line[0]), int(line[1])])
        print(aa.user_pool(n, connections))