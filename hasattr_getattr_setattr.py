class Parent:
    pass


class Child(Parent):
    pass


if hasattr(Parent, 'x'):
    print(getattr(Parent, 'x'))

# setattr设置类属性
setattr(Parent, 'x', 3)
print(getattr(Parent, 'x'))
p = Parent()
print(getattr(p, 'x'))

c = Child()
print(getattr(c, 'x'))

c.x = 4
print(getattr(c, 'x'))
print(getattr(p, 'x'))
