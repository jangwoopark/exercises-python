import unittest

class TheIndianJob:
    memoize = {}

    def __init__(self, g, A):
        self._g = g
        self._A = A

    def calculate(self):
        """One line doc string"""
        self._A.sort(reverse=True)
        return self.recursive_formulation(self._g, self._g, self._A[:])

    def recursive_formulation(self, l1, l2, A):
        """Recursive formulation of the given problem
        
        Keyword arguments:
            11 -- length of the first lane
            l2 -- length of the second lane
            A -- Array of time each thief wants to be in 
        """
        # minor optimization
        if l1 < l2:
            l1, l2 = l2, l1
        # base cases
        if l1 < 0 or l2 < 0:
            return False
        if sum(A) > l1 + l2:
            return False
        if len(A) == 0:
            return True
        if len(A) == 1:
            if A[0] <= l1 or A[0] <= l2:
                return True
            else:
                return False

        if sum(A) == l1 or sum(A) == l2:
            return True

        # memoize
        key = "{}_{}_{}".format(l1, l1, "_".join(["{}".format(x) for x in A]))
        if key in self.memoize:
            return self.memoize.get(key)

        # check permutations
        first_el = A[0]
        remaining_array = A[1:]  # we are very sure that A contains atleast 2 elements
        # check possibility in l1 or l2
        possibility = self.recursive_formulation(l1 - first_el,
                                                 l2, remaining_array) or self.recursive_formulation(l1,
                                                                                                    l2 - first_el,
                                                                                                    remaining_array)
        self.memoize[key] = possibility
        return possibility


class TestTheIndianJob(unittest.TestCase):
    def test1(self):
        tij = TheIndianJob(4, [2, 4, 2])
        self.assertEqual(tij.calculate(), True)

    def test2(self):
        tij = TheIndianJob(2, [2, 4, 2])
        self.assertEqual(tij.calculate(), False)

    def test3(self):
        tij = TheIndianJob(4, [5, 1, 2])
        self.assertEqual(tij.calculate(), False)

    def test4(self):
        tij = TheIndianJob(9, [4, 4, 3, 3, 3])
        self.assertEqual(tij.calculate(), True)

    def test5(self):
        tij = TheIndianJob(9, [4, 4, 4, 3, 3])
        self.assertEqual(tij.calculate(), False)

    def test6(self):
        tij = TheIndianJob(11, [10])
        self.assertEqual(tij.calculate(), True)


if __name__ == "__main__":
    n = int(input().strip())
    for i in range(n):
        r_count, g = map(int, input().strip().split())
        A = [int(el) for el in input().strip().split()]
        tij = TheIndianJob(g, A)
        if tij.calculate():
            print("YES")
        else:
            print("NO")
