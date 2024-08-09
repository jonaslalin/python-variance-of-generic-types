class A:
    def foo(self) -> None:
        print("foo")


class B(A):
    def bar(self) -> None:
        print("bar")


class C(B):
    def baz(self) -> None:
        print("baz")
