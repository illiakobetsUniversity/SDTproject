from .singleton import as_singleton


@as_singleton
class A:
    pass


class B:
    pass

a1, a2 = A(), A()

b1, b2 = B(), B()

print("Singleton A, a1 is a2: {}".format(a1 is a2))
print("Not singleton B, b1 is b2: {}".format(b1 is b2))
