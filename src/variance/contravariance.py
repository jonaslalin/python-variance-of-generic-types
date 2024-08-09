from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .models import A, B, C

T_in = TypeVar("T_in", contravariant=True)
# T_contra = TypeVar("T_contra", contravariant=True)


class Sink(ABC, Generic[T_in]):
    @abstractmethod
    def consume(self, value: T_in, /) -> None: ...


class PureASink(Sink[A]):
    def consume(self, a: A, /) -> None:
        print(f"doing consume from {self.__class__.__name__}")
        a.foo()


class PureBSink(Sink[B]):
    def consume(self, b: B, /) -> None:
        print(f"doing consume from {self.__class__.__name__}")
        b.foo()
        b.bar()


class PureCSink(Sink[C]):
    def consume(self, c: C, /) -> None:
        print(f"doing consume from {self.__class__.__name__}")
        c.foo()
        c.bar()
        c.baz()


def with_some_a_sink(a_sink: Sink[A]) -> None:
    a, b, c = A(), B(), C()
    a_sink.consume(a)
    a_sink.consume(b)
    a_sink.consume(c)


def with_some_b_sink(b_sink: Sink[B]) -> None:
    a, b, c = A(), B(), C()  # noqa: F841
    # b_sink.consume(a)
    b_sink.consume(b)
    b_sink.consume(c)


def with_some_c_sink(c_sink: Sink[C]) -> None:
    a, b, c = A(), B(), C()  # noqa: F841
    # c_sink.consume(a)
    # c_sink.consume(b)
    c_sink.consume(c)
