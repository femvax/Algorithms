class UnionFind:

    def __init__(self, n):
        self.id = list(range(n))
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
            self.id[p] = q_id

    def connected(self, p, q):
        return(self.find(p) == self.find(q))