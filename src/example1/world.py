from typing import Any


class A:
    a: str

    def __init__(self, a: str = "a") -> None:
        self.a = a

    def print_a(self) -> None:
        print(f"print_a in {self.__class__.__name__}")
        print(f"a={self.a}")


class B(A):
    b: str

    def __init__(self, b: str = "b", *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.b = b

    def print_b(self) -> None:
        print(f"print_b in {self.__class__.__name__}")
        print(f"b={self.b}")


class C(B):
    c: str

    def __init__(self, c: str = "c", *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.c = c

    def print_c(self) -> None:
        print(f"print_c in {self.__class__.__name__}")
        print(f"c={self.c}")


class D(A):
    d: str

    def __init__(self, d: str = "d", *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.d = d

    def print_d(self) -> None:
        print(f"print_d in {self.__class__.__name__}")
        print(f"d={self.d}")


def produce_a(*args: Any, **kwargs: Any) -> A:
    a = A(*args, **kwargs)
    return a


def produce_b(*args: Any, **kwargs: Any) -> B:
    b = B(*args, **kwargs)
    return b


def produce_c(*args: Any, **kwargs: Any) -> C:
    c = C(*args, **kwargs)
    return c


def produce_d(*args: Any, **kwargs: Any) -> D:
    d = D(*args, **kwargs)
    return d


def consume_a(a: A) -> None:
    a.print_a()


def consume_b(b: B) -> None:
    b.print_a()
    b.print_b()


def consume_c(c: C) -> None:
    c.print_a()
    c.print_b()
    c.print_c()


def consume_d(d: D) -> None:
    d.print_a()
    d.print_d()


def consume_a_and_produce_a(a: A) -> A:
    consume_a(a)
    new_a = produce_a(a=a.a * 2)
    return new_a


def consume_b_and_produce_b(b: B) -> B:
    consume_b(b)
    new_b = produce_b(a=b.a * 2, b=b.b * 2)
    return new_b


def consume_c_and_produce_c(c: C) -> C:
    consume_c(c)
    new_c = produce_c(a=c.a * 2, b=c.b * 2, c=c.c * 2)
    return new_c


def consume_d_and_produce_d(d: D) -> D:
    consume_d(d)
    new_d = produce_d(a=d.a * 2, d=d.d * 2)
    return new_d
