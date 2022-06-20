import unittest
from hypothesis import given,  strategies as st
from dispatch_example_func import *
import math


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
        if (not (math.isinf(a) or math.isinf(b))
        and (not (math.isnan(a) or math.isnan(b)))):
            self.assertEqual((add(a, b)-(a+b)) < 1e-3, True)
            self.assertEqual(add(a, b)-add(b, a) < 1e-3, True)

        # optional
            self.assertEqual(abs(add(a)-a) < 1e-3, True)

    @given(st.integers(), st.floats())
    def test_add_IntAndFloat(self, a, b):
        '''test int and float'''
        # two numbers
        if (not math.isinf(b)) and (not math.isnan(b)):
            self.assertEqual(abs(add(a, b)-(a+b)) < 1e-5, True)
            self.assertEqual(abs(add(a, b)-add(b, a)) < 1e-5, True)

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

if __name__ == '__main__':
    # The function around which the other functions should run
    unittest.main()