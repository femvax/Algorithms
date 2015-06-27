class UnionFind:

    def __init__(self, n):
        self.id = list(range(n))
        self.sz = [1 for x in range(n)]
        self.n = n

    def find(self, p):
        if p == self.id[p]:
            return p
        else:
            return self.find(self.id[p])

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        else:
            if self.sz[p_id] < self.sz[q_id]:
                self.id[p] = q_id
                self.sz[q] += 1
            else:
                self.id[q] = p_id
                self.sz[p] += 1

    def connected(self, p, q):
        return(self.find(p) == self.find(q))