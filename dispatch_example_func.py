from multipledispatch_module import dispatch
from multipledispatch_module import combMethod
from multipledispatch_module import call_next_before
from multipledispatch_module import call_next_after
from multipledispatch_module import before, after, around
import numpy as np


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


@dispatch(np.ndarray, np.ndarray)
def add(array1, array2):
    '''add two array'''
    if(array1.shape == array2.shape):
        return array1 + array2
    else:
        return 'error'


@dispatch(np.ndarray)
def add(array1):
    '''array2 is filled with zero'''
    return array1


@dispatch(int, np.ndarray)
def add(int1, array1):
    '''add int and array'''
    array2 = np.full(array1.shape, int1)
    return add(array1, array2)


@dispatch(np.ndarray, int)
def add(array1, int1):
    '''add array and int'''
    return add(int1, array1)


@dispatch(float, np.ndarray)
def add(float1, array1):
    '''add float and array'''
    array2 = np.full(array1.shape, float1)
    return add(array1, array2)


@dispatch(np.ndarray, float)
def add(array1, float1):
    '''add array and float'''
    return add(float1, array1)


@dispatch(int, int)
def sub(int1, int2):
    '''sub two int'''
    return int1 - int2


@dispatch(int)
def sub(int1):
    '''int2 is zero'''
    return int1


@dispatch(float, float)
def sub(float1, float2):
    '''sub two float'''
    return float1 - float2


@dispatch(float)
def sub(float1):
    '''float2 is zero'''
    return float1


@dispatch(int, float)
def sub(int1, float1):
    '''int sub float'''
    return int1 - float1


@dispatch(float, int)
def sub(float1, int1):
    '''float sub int'''
    return float1 - int1


@dispatch(np.ndarray, np.ndarray)
def sub(array1, array2):
    '''sub two array'''
    if array1.shape == array2.shape:
        return array1 - array2
    else:
        return 'error'


@dispatch(np.ndarray)
def sub(array1):
    '''array2 is filled with zero'''
    return array1


@dispatch(int, np.ndarray)
def sub(int1, array1):
    '''sub int and array'''
    array2 = np.full(array1.shape, int1)
    return sub(array2, array1)


@dispatch(np.ndarray, int)
def sub(array1, int1):
    '''sub array and int'''
    array2 = np.full(array1.shape, int1)
    return sub(array1, array2)


@dispatch(float, np.ndarray)
def sub(float1, array1):
    '''sub float and array'''
    array2 = np.full(array1.shape, float1)
    return sub(array2, array1)


@dispatch(np.ndarray, float)
def sub(array1, float1):
    '''sub array and float'''
    array2 = np.full(array1.shape, float1)
    return sub(array1, array2)


@dispatch(int, int)
def multiple(int1, int2):
    '''multiple two int'''
    return int1 * int2


@dispatch(int)
def multiple(int1):
    '''int2 is 1'''
    return int1


@dispatch(float, float)
def multiple(float1, float2):
    '''multiple two float'''
    return float1 * float2


@dispatch(float)
def multiple(float1):
    '''float2 is 1'''
    return float1


@dispatch(float, int)
def multiple(float1, int1):
    '''multiple float and int'''
    return float1 * int1


@dispatch(int, float)
def multiple(int1, float1):
    '''multiple int and float'''
    return int1 * float1


@dispatch(np.ndarray, np.ndarray)
def multiple(array1, array2):
    '''multiple two array'''
    if array1.shape == array2.shape:
        return array1 * array2
    else:
        return 'error'


@dispatch(np.ndarray)
def multiple(array1):
    '''array2 is filled with one'''
    return array1


@dispatch(int, np.ndarray)
def multiple(int1, array1):
    '''multiple int and array'''
    array2 = np.full(array1.shape, int1)
    return multiple(array1, array2)


@dispatch(np.ndarray, int)
def multiple(array1, int1):
    '''multiple array and int'''
    return multiple(int1, array1)


@dispatch(float, np.ndarray)
def multiple(float1, array1):
    '''multiple array and float'''
    array2 = np.full(array1.shape, float1)
    return multiple(array1, array2)


@dispatch(np.ndarray, float)
def multiple(array1, float1):
    '''multiple float and array'''
    return multiple(float1, array1)


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
@around(around_func)
@dispatch(A)
def aroundfn(object1):
    return 'aroundA'


@around(around_func)
@dispatch(B)
def aroundfn(object1):
    return 'aroundB'


@around(around_func)
@dispatch(C)
def aroundfn(object1):
    return 'aroundC'


@around(around_func)
@dispatch(D)
def aroundfn(object1):
    return 'aroundD'


@combMethod(before=before_func, after=after_func, around=around_func)
@dispatch(A)
def combfn(object2):
    return 'combA'


@combMethod(before=before_func, after=after_func, around=around_func)
@dispatch(B)
def combfn(object2):
    return 'combB'


@combMethod(before=before_func, after=after_func, around=around_func)
@dispatch(C)
def combfn(object3):
    return 'combC'


@combMethod(before=before_func, after=after_func, around=around_func)
@dispatch(D)
def combfn(object4):
    return 'combD'
