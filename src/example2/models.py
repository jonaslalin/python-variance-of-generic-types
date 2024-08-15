class A:
    def foo(self) -> None:
        print(f"doing foo in {self.__class__.__name__}")


class B(A):
    def bar(self) -> None:
        print(f"doing bar in {self.__class__.__name__}")


class C(B):
    def baz(self) -> None:
        print(f"doing baz in {self.__class__.__name__}")
