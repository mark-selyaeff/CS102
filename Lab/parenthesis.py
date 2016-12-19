class Tree():
    def __init__(self, string):
        self.string = string
        self.t = [0] * len(string) * 4
        self.__build(0, 0, len(self.string) - 1)

    def __build(self, v, vl, vr):
        if vl == vr:
            self.t[v] = Cell(self.string[vl])
        else:
            vm = vl + (vr - vl) // 2
            self.__build(2*v+1, vl, vm)
            self.__build(2*v+2, vm+1, vr)
            self.t[v] = self.t[v*2+1] + self.t[v*2+2]

    def query(self, v, vl, vr, l, r):
        if (r < vl) or (vr < l):
            return 0
        if (l <= vl) and (vr <= r):
            return self.t[v].count_p + min(self.t[v].leftp, self.t[v].rightp)
        vm = vl + (vr - vl) // 2
        ql = self.query(2*v+1, vl, vm, l, r)
        qr = self.query(2*v+2, vm+1, vr, l, r)
        return ql + qr





class Cell():
    def __init__(self, string):
        self.string = string
        self.leftp = self._leftp()
        self.rightp = self._rightp()
        self.count_p = self._count_p() if len(self.string) > 1 else 0

    def _leftp(self):
        return self.string.count('(') - self._count_p()

    def _rightp(self):
        return self.string.count(')') - self._count_p()

    def _count_p(self):
        opened = 0
        answer = 0
        for i in self.string:
            if i == '(':
                opened += 1
            elif  i == ')' and opened > 0:
                opened -= 1
                answer += 1
        return answer

    def __add__(self, other):
        return Cell(self.string + other.string)

    def __repr__(self):
        return self.string


