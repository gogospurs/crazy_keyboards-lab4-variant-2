registry = {}


class Dispatch(object):
    def __init__(self, name):
        '''initial function'''
        self.name = name
        self.typemapdict = {}

    def __call__(self, *args):
        '''make the function callable'''
        types = tuple(arg.__class__ for arg in args)
        func = self.typemapdict.get(types)
        if func is None:
            raise TypeError("no match")
        return func(*args)

    def register(self, types, func):
        '''add new function to typemap'''
        if types in self.typemapdict:
            raise TypeError("duplicate registration")
        self.typemapdict[types] = func


def dispatch(*types):
    '''decorator'''
    def register(func):
        '''add'''
        func = getattr(func, "__lastreg__", func)
        name = func.__name__
        md = registry.get(name)
        if md is None:
            md = registry[name] = Dispatch(name)
        md.register(types, func)
        md.__lastreg__ = func
        return md
    return register


def combMethod(before=None, after=None, around=None):
    """A decorator that implements function method to be run before, after or
    around another function, sort of like in the CLOS."""
    # Make sure all of our method are callable
    before = before if callable(before) else None
    after = after if callable(after) else None
    around = around if callable(around) else None

    # The actual decorator function.  The "real" function to be called will be
    # pased to this as `func`
    def decorator(func):
        # The decorated function.  This is where the work is done.  The before
        # and around functions are called, then the "real" function is called
        # and its results are stored, then the around and after functions are
        # called.
        def decorate_order(*args, **kwargs):
            if callable(around):
                around(*args, **kwargs)
            if callable(before):
                before(*args, **kwargs)
            result = func(*args, **kwargs)
            if callable(after):
                after(*args, **kwargs)
            if callable(around):
                around(*args, **kwargs)
            return result

        return decorate_order

    return decorator


def call_next_before(object1):
    '''return list of call next method for before method'''
    list1 = []
    if object1 is not None:
        if type(object1).__mro__:
            list1 = list(type(object1).__mro__).copy()
            if list1:
                list1.pop(-1)
    return list1


def call_next_after(object1):
    '''return list of call next method for after method'''
    list1 = []
    if object1 is not None:
        if type(object1).mro():
            list1 = list(type(object1).__mro__)[::-1]
            if list1:
                list1.pop(0)
    return list1


# Shortcuts for defining just one kind of hint
def before(method):
    return combMethod(before=method)


def after(method):
    return combMethod(after=method)


def around(method):
    return combMethod(around=method)
