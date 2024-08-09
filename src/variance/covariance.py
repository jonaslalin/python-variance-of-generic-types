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
