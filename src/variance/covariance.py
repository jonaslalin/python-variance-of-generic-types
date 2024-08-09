from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .models import A, B, C

T_out = TypeVar("T_out", covariant=True)


class Source(ABC, Generic[T_out]):
    @abstractmethod
    def produce(self) -> T_out: ...


class ConcreteASource(Source[A]):
    def produce(self) -> A:
        return A()


class ConcreteBSource(Source[B]):
    def produce(self) -> B:
        return B()


class ConcreteCSource(Source[C]):
    def produce(self) -> C:
        return C()


def with_some_a_source(a_source: Source[A]) -> None:
    a = a_source.produce()
    a.foo()


def with_some_b_source(b_source: Source[B]) -> None:
    b = b_source.produce()
    b.foo()
    b.bar()


def with_some_c_source(c_source: Source[C]) -> None:
    c = c_source.produce()
    c.foo()
    c.bar()
    c.baz()
