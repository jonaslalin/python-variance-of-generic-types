class A:
    def foo(self) -> None:
        print(f"doing foo from {self.__class__.__name__}")


class B(A):
    def bar(self) -> None:
        print(f"doing bar from {self.__class__.__name__}")


class C(B):
    def baz(self) -> None:
        print(f"doing baz from {self.__class__.__name__}")
