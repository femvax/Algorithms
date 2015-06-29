class UnionFind:
    def __init__(self, N):
        self.id = list(range(N))
        self.sz = [1] * N

    def find(self, p):
        if self.id[p] == p:
            return p
        else:
            self.id[p] = self.id[self.id[p]]
            return self.find(self.id[p])

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id != q_id:
            if self.sz[p_id] <= self.sz[q_id]:
                self.id[p_id] = q_id
                self.sz[q_id] += self.sz[p_id]
            else:
                self.id[q_id] = p_id
                self.sz[p_id] += self.sz[q_id]

    def connected(self, p, q):
        return(self.find(p) == self.find(q))