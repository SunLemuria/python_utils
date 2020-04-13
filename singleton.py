"""
在 Python 中，我们可以用多种方法来实现单例模式:
1. 使用模块; 2.使用__new__; 3.使用装饰器; 4. 使用元类(metaclass)。
1)使用模块:其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成.pyc 文件， 当第二次导入时，就会直接加载.pyc 文件，而不会再次执行模块代码。因此我们只需把相关的函数和数 据定义在一个模块中，就可以获得一个单例对象了。
"""


# mysingle.py
class MySingle:
    def foo(self):
        pass


# singleton = MySingle()

# 将以上代码保存在mysingle.py文件中,使用:
# from mysingle import singleton
# singleton.foo()


"""
2)使用__new__:为了使类只能出现一个实例，我们可以使用__new__来控制实例的创建过程，
"""


class Singleton(object):
    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个 instance 对象 if not hasattr(cls, 'instance'):
        cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


obj1 = Singleton()
obj2 = Singleton()
assert obj1 is obj2

"""
3)使用装饰器:装饰器可以动态的修改一个类或函数的功能。这里，我们也可以使用装饰器来装饰某
个类，使其只能生成一个实例
"""


def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MyClass:
    a = 1


c1 = MyClass()
c2 = MyClass()
assert c1 is c2

"""
4)使用 metaclass(元类):元类可以控制类的创建过程，它主要做三件事:
- 拦截类的创建
- 修改类的定义
- 返回修改后的类
"""


class Singleton2(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super(Singleton2, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls.__instance


class Foo(object):
    __metaclass__ = Singleton2  # 在代码执行到这里的时候，元类中的__new__方法和__init__方法其实已经被执行了，而不是在 Foo 实例化的时候执行。且仅会执行一次。 14.


foo1 = Foo()
foo2 = Foo()
assert foo1 is foo2
print(Foo.__dict__)
# _Singleton__instance': <__main__.Foo object at 0x100c52f10> 存在一个私有属性来保存属性，而不会污染 Foo 类(其实还是会污染，只是无法直接通过__instance 属性访问)
