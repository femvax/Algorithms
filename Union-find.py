class UF:
    def __init__(self, N):
        self.id = list(range(N))
        self.sz = [1 for x in range(N)]

    def find(self, p):
        if self.id[p] == p:
            return p
        else:
            return self.find(self.id[p])

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)
        if pID == qID:
            return
        else:
            if self.sz[pID] < self.sz[qID]:
                self.id[pID] = qID
                self.sz[qID] += self.sz[pID]
            else:
                self.id[qID] = pID
                self.sz[pID] += self.sz[qID]

    def connected(self, p, q):
        return(self.find(p) == self.find(q))
