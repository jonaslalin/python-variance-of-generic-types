from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from typing_extensions import TypeAlias

from example1.world import A, B, consume_a, consume_b, produce_a, produce_b

T = TypeVar("T", contravariant=True)


class Sink(Generic[T], ABC):
    @abstractmethod
    def consume(self, value: T) -> None: ...


ASink: TypeAlias = Sink[A]
BSink: TypeAlias = Sink[B]


class ConcreteASink(ASink):
    def consume(self, value: A) -> None:
        consume_a(value)


class ConcreteBSink(BSink):
    def consume(self, value: B) -> None:
        consume_b(value)


def with_a_sink(a_sink: ASink) -> None:
    a_sink.consume(produce_a())
    a_sink.consume(produce_b())


def with_b_sink(b_sink: BSink) -> None:
    b_sink.consume(produce_b())
