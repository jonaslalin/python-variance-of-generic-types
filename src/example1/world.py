class A:
    def do_a(self) -> None:
        print(f"doing a in {self.__class__.__name__}")


class B(A):
    def do_b(self) -> None:
        print(f"doing b in {self.__class__.__name__}")


class C(B):
    def do_c(self) -> None:
        print(f"doing c in {self.__class__.__name__}")


class D(A):
    def do_d(self) -> None:
        print(f"doing d in {self.__class__.__name__}")


def produce_a() -> A:
    a = A()
    return a


def produce_b() -> B:
    b = B()
    return b


def produce_c() -> C:
    c = C()
    return c


def produce_d() -> D:
    d = D()
    return d


def consume_a(a: A) -> None:
    a.do_a()


def consume_b(b: B) -> None:
    b.do_a()
    b.do_b()


def consume_c(c: C) -> None:
    c.do_a()
    c.do_b()
    c.do_c()


def consume_d(d: D) -> None:
    d.do_a()
    d.do_d()


def consume_and_produce_a(a: A) -> A:
    consume_a(a)
    new_a = produce_a()
    return new_a


def consume_and_produce_b(b: B) -> B:
    consume_b(b)
    new_b = produce_b()
    return new_b


def consume_and_produce_c(c: C) -> C:
    consume_c(c)
    new_c = produce_c()
    return new_c


def consume_and_produce_d(d: D) -> D:
    consume_d(d)
    new_d = produce_d()
    return new_d
