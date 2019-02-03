
class first:
    def test(self):
        data = [[0, 0, True], [0, 1, True], [1, 0, False], [1, 1, True]]

        w0 = 1
        w1 = -1.2
        w2 = 0.5

        for d in data:
            print(w0 + d[0]*w1 + d[1]*w2 >= 0)
            assert d[2] ==  (w0 + d[0]*w1 + d[1]*w2 >= 0)


class second:
    def first_sub(self, x1, x2):
        w0 = -8
        w1 = 2
        w2 = 6
        return w0+w1*x1+w2*x2 >= 0

    def second_sub(self, x1, x2):
        w0 = -10
        w1 = 12
        w2 = 14
        return w0+w1*x1+w2*x2 >= 0

    def final(self, x1, x2):
        w0 = -10
        w1 = -4
        w2 = 12
        return w0+w1*x1+w2*x2 >= 0

    def test(self):
        data = [[0, 0, False], [0, 1, True], [1, 0, True], [1, 1, False]]
        for d in data:
            print(self.final(self.first_sub(d[0], d[1]), self.second_sub(d[0], d[1])))
            assert d[2] == self.final(self.first_sub(d[0], d[1]), self.second_sub(d[0], d[1]))

s = second()
s.test()