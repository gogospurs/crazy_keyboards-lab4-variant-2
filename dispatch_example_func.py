from multipledispatch_module import registry
from multipledispatch_module import Dispatch
from multipledispatch_module import dispatch
from multipledispatch_module import combMethod
from multipledispatch_module import call_next_before
from multipledispatch_module import call_next_after
from multipledispatch_module import before, after, around


@dispatch(int, int)
def add(int1, int2):
    '''add two int variable'''
    return int1 + int2


@dispatch(int)
def add(int1):
    '''int2 is optional, and its default value is 0'''
    return int1


@dispatch(float, float)
def add(float1, float2):
    '''add two float variable'''
    return float1 + float2


@dispatch(float)
def add(float1):
    '''float2 is optional and its default value is 0.0'''
    return float1


@dispatch(int, float)
def add(int1, float1):
    '''add two different type numeric variable'''
    return int1 + float1


@dispatch(float, int)
def add(float1, int1):
    '''add two different type numeric variable'''
    return add(int1, float1)


@dispatch(str, str)
def add(str1, str2):
    '''add two str variable'''
    return str1 + str2


@dispatch(str)
def add(str1):
    '''str2 is optional and its default value is "" '''
    return str1


@dispatch(dict, dict)
def add(dict1, dict2):
    '''add two dict variable'''
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3


@dispatch(dict)
def add(dict1):
    '''dict2 is optional and is empty dict {}'''
    return dict1


@dispatch(list, list)
def add(list1, list2):
    '''add two list variable, put the list2 after the list1'''
    return list1 + list2


@dispatch(list)
def add(list1):
    '''list2 is optional and is empty list []'''
    return list1


class A(object):
    '''super class'''
    def __init__(self):
        self.before = 0
        self.after = 0
        self.around = 0


class B(A):
    '''class inhertied from A'''
    def __init__(self):
        super().__init__()


class C(A):
    '''class inhertied from B'''
    def __init__(self):
        super().__init__()


class D(B, C):
    '''class multiinhertied from B and C'''
    def __init__(self):
        super().__init__()


# The actual functions to run before, after, around
def before_func(object1=None):
    class_list = call_next_before(object1)
    if class_list:
        for classtype in class_list:
            print(classtype)
            object1.before = object1.before + 1


def after_func(object1=None):
    class_list = call_next_after(object1)
    if class_list:
        for classtype in class_list:
            print(classtype)
            object1.after = object1.after + 1


def around_func(object1=None):
    print("around")


# before method
@before(before_func)
@dispatch(A)
def beforefn(object1):
    return 'beforeA'


@before(before_func)
@dispatch(B)
def beforefn(object1):
    return 'beforeB'


@before(before_func)
@dispatch(C)
def beforefn(object1):
    return 'beforeC'


@before(before_func)
@dispatch(D)
def beforefn(object1):
    return "beforeD"


# after
@after(after_func)
@dispatch(A)
def afterfn(object1):
    return 'afterA'


@after(after_func)
@dispatch(B)
def afterfn(object1):
    return 'afterB'


@after(after_func)
@dispatch(C)
def afterfn(object1):
    return 'afterC'


@after(after_func)
@dispatch(D)
def afterfn(object1):
    return 'afterD'


# around
@combMethod(before=before_func, after=after_func, around=around_func)
@dispatch(A)
def aroundfn(object2):
    return 'aroundA'


@combMethod(before=before_func, after=after_func, around=around_func)
@dispatch(B)
def aroundfn(object2):
    return 'aroundB'


@combMethod(before=before_func, after=after_func, around=around_func)
@dispatch(C)
def aroundfn(object3):
    return 'aroundC'


@combMethod(before=before_func, after=after_func, around=around_func)
@dispatch(D)
def aroundfn(object4):
    return 'aroundD'
