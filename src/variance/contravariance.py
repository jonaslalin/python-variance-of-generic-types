from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .models import A, B, C

T_in = TypeVar("T_in", contravariant=True)


class Sink(ABC, Generic[T_in]):
    @abstractmethod
    def consume(self, something: T_in, /) -> None: ...


class ConcreteASink(Sink[A]):
    def consume(self, a: A, /) -> None:
        a.foo()


class ConcreteBSink(Sink[B]):
    def consume(self, b: B, /) -> None:
        b.foo()
        b.bar()


class ConcreteCSink(Sink[C]):
    def consume(self, c: C, /) -> None:
        c.foo()
        c.bar()
        c.baz()


def with_some_a_sink(a_sink: Sink[A]) -> None:
    a_sink.consume(A())  # `a_sink.consume(a)` will call `a.foo()`, which exists on instances of `A`
    a_sink.consume(B())  # `a_sink.consume(b)` will call `b.foo()`, which exists on instances of `B`
    a_sink.consume(C())  # `a_sink.consume(b)` will call `c.foo()`, which exists on instances of `C`


def with_some_b_sink(b_sink: Sink[B]) -> None:
    # b_sink.consume(A())  # `b_sink.consume(a)` will call `a.bar()`, which doesn't exist on instances of `A`
    b_sink.consume(B())  # `b_sink.consume(b)` will call `b.foo(), and `b.bar()`, which exist on instances of `B`
    b_sink.consume(C())  # `b_sink.consume(c)` will call `c.foo(), and `c.bar()`, which exist on instances of `C`


def with_some_c_sink(c_sink: Sink[C]) -> None:
    # c_sink.consume(A())  # `c_sink.consume(a)` will call `a.bar()`, and `a.baz()`, which doesn't exist on instances of `A`  # noqa: E501 # fmt: skip
    # c_sink.consume(B())  # `c_sink.consume(b)` will call `b.baz()`, which doesn't exist on instances of `B`
    c_sink.consume(C())  # `c_sink.consume(c)` will call `c.foo(), `c.bar()`, and `c.baz()`, which exist on instances of `C`  # noqa: E501 # fmt: skip
