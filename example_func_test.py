import unittest
from hypothesis import given,  strategies as st
from dispatch_example_func import add, multiple, sub, A, B, C, D
from dispatch_example_func import beforefn, afterfn
from dispatch_example_func import aroundfn, combfn
import math
import numpy as np


class Testmultiple(unittest.TestCase):

    @given(st.integers(), st.integers())
    def test_add_int(self, a, b):
        '''test int'''
        # two int
        self.assertEqual(add(a, b), a+b)
        self.assertEqual(add(a, b), add(b, a))

        # optional
        self.assertEqual(add(a), a)

    @given(st.floats(), st.floats())
    def test_add_float(self, a, b):
        '''test floats'''
        # two floats
        if (not (math.isinf(a) or math.isinf(b)) and
                (not (math.isnan(a) or math.isnan(b)))):
            self.assertEqual(add(a, b), a+b)
            self.assertEqual(add(a, b), add(b, a))

        # optional
            self.assertEqual(add(a), a)

    @given(st.integers(), st.floats())
    def test_add_IntAndFloat(self, a, b):
        '''test int and float'''
        # two numbers
        if (not math.isinf(b)) and (not math.isnan(b)):
            self.assertEqual(add(a, b), a+b)
            self.assertEqual(add(a, b), add(b, a))

    @given(st.text(), st.text())
    def test_add_str(self, a, b):
        '''test str'''
        # two strings
        self.assertEqual(add(a, b), a+b)

        # optional
        self.assertEqual(add(a), a)

    def test_add_dict(self):
        '''test dict'''
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        dict3 = {'a': 1, 'b': 2}

        # two dict
        self.assertEqual(add(dict1, dict2), dict3)

    @given(st.lists(st.integers()), st.lists(st.integers()))
    def test_add_list(self, a, b):
        '''test list'''
        # two list
        self.assertEqual(add(a, b), a + b)
        self.assertEqual(sorted(add(a, b)), sorted(add(b, a)))

        # optional
        self.assertEqual(add(a), a)

    def test_add_np(self):
        '''test array'''
        array1 = np.ones(3)
        array2 = np.ones(3)
        array3 = np.ones(4)
        array4 = np.full(3, 1.0)

        # two  same shape array
        res = add(array1, array2)
        self.assertEqual((res == np.full(3, 2)).all(), True)

        # two different shape array
        self.assertEqual(add(array1, array3), "error")

        # optional
        self.assertEqual((add(array1) == array1).all(), True)

        # int and array
        self.assertEqual((add(1, array1) == np.full(3, 2)).all(), True)
        self.assertEqual((add(1, array1) == add(array1, 1)).all(), True)

        # float and array
        self.assertEqual((add(1.0, array4) == np.full(3, 2.0)).all(), True)
        self.assertEqual((add(1.0, array4) == add(array4, 1.0)).all(), True)

    @given(st.integers(), st.integers())
    def test_sub_int(self, a, b):
        '''test sub two int'''
        # two int
        self.assertEqual(sub(a, b), a-b)

        # optional
        self.assertEqual(sub(a), a)

    @given(st.floats(), st.floats())
    def test_sub_float(self, a, b):
        '''test sub two float'''
        if (not (math.isinf(a) or math.isinf(b)) and
                (not (math.isnan(a) or math.isnan(b)))):
            # two float
            self.assertEqual(sub(a, b), a-b)

            # optional
            self.assertEqual(sub(a), a)

    @given(st.integers(), st.floats())
    def test_sub_intAndfloat(self, a, b):
        '''test int sub float'''
        if not math.isinf(b) and not math.isnan(b):
            self.assertEqual(sub(a, b), a-b)

    @given(st.floats(), st.integers())
    def test_sub_floatAndint(self, a, b):
        '''test float sub int'''
        if not math.isinf(a) and not math.isnan(a):
            self.assertEqual(sub(a, b), a-b)

    def test_sub_array(self):
        '''test sub two array'''
        array1 = np.ones(3)
        array2 = np.ones(3)
        array3 = np.ones(4)
        array4 = np.full(3, 1.0)
        # two array
        res = sub(array1, array2)
        self.assertEqual((res == np.zeros(3)).all(), True)
        self.assertEqual(sub(array1, array3), "error")

        # optional
        self.assertEqual((sub(array1) == array1).all(), True)

        # int and array
        self.assertEqual((sub(1, array1) == np.zeros(3)).all(), True)
        self.assertEqual((sub(array1, 1) == np.zeros(3)).all(), True)

        # float and array
        self.assertEqual((sub(array4, 1.0) == np.full(3, 0.0)).all(), True)
        self.assertEqual((sub(1.0, array4) == np.full(3, 0.0)).all(), True)

    @given(st.integers(), st.integers())
    def test_multiple_int(self, a, b):
        '''test multiple int'''
        # two int
        self.assertEqual(multiple(a, b), a*b)
        self.assertEqual(multiple(a, b), multiple(b, a))

        # optional
        self.assertEqual(multiple(a), a)

    @given(st.floats(), st.floats())
    def test_multiple_float(self, a, b):
        '''test multiple float'''
        if (not (math.isinf(a) or math.isinf(b)) and
                (not (math.isnan(a) or math.isnan(b)))):
            # two float
            self.assertEqual(multiple(a, b), a*b)
            self.assertEqual(multiple(a, b), multiple(b, a))

            # optional
            self.assertEqual(multiple(a), a)

    @given(st.integers(), st.floats())
    def test_multiple_intAndfloat(self, a, b):
        '''test int and float'''
        if not math.isinf(b) and not math.isnan(b):
            self.assertEqual(multiple(a, b), a*b)

    @given(st.floats(), st.integers())
    def test_multiple_floatAndint(self, a, b):
        '''test float and int'''
        if not math.isinf(a) and not math.isnan(a):
            self.assertEqual(multiple(a, b), a*b)

    def test_multiple_array(self):
        '''test array'''
        array1 = np.ones(3)
        array2 = np.ones(3)
        array3 = np.ones(4)
        array4 = np.full(3, 2.0)

        # two array
        res = multiple(array1, array2)
        self.assertEqual((res == np.full(3, 1)).all(), True)
        self.assertEqual(multiple(array1, array3), "error")

        # optional
        self.assertEqual((multiple(array1) == array1).all(), True)

        # int and array
        self.assertEqual((multiple(1, array1) == 1*array1).all(), True)
        res = (multiple(1, array1) == multiple(array1, 1)).all()
        self.assertEqual(res, True)

        # float and array
        self.assertEqual((multiple(1.0, array4) == 1.0*array4).all(), True)
        res = (multiple(array4, 1.0) == multiple(1.0, array4)).all()
        self.assertEqual(res, True)

    def test_inheritance(self):
        '''test inheritance and multiple inheritance with
        before, after, around method'''
        a = A()
        b = B()
        c = C()
        d = D()

        # before method
        self.assertEqual(beforefn(a), 'beforeA')
        self.assertEqual(a.before, 1)
        self.assertEqual(beforefn(b), 'beforeB')
        self.assertEqual(b.before, 2)
        self.assertEqual(beforefn(c), 'beforeC')
        self.assertEqual(c.before, 2)
        self.assertEqual(beforefn(d), 'beforeD')
        self.assertEqual(d.before, 4)

        # after method
        self.assertEqual(afterfn(a), 'afterA')
        self.assertEqual(a.after, 1)
        self.assertEqual(afterfn(b), 'afterB')
        self.assertEqual(b.after, 2)
        self.assertEqual(afterfn(c), 'afterC')
        self.assertEqual(c.after, 2)
        self.assertEqual(afterfn(d), 'afterD')
        self.assertEqual(d.after, 4)

        # around method
        self.assertEqual(aroundfn(a), 'aroundA')
        self.assertEqual(aroundfn(b), 'aroundB')
        self.assertEqual(aroundfn(c), 'aroundC')
        self.assertEqual(aroundfn(d), 'aroundD')

        # comb methond
        self.assertEqual(combfn(a), 'combA')
        self.assertEqual(combfn(b), 'combB')
        self.assertEqual(combfn(c), 'combC')
        self.assertEqual(combfn(d), 'combD')


if __name__ == '__main__':
    # The function around which the other functions should run
    unittest.main()
