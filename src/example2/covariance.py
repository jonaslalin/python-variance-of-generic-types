from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .models import A, B, C

T_out = TypeVar("T_out", covariant=True)
# T_co = TypeVar("T_co", covariant=True)


class Producer(ABC, Generic[T_out]):
    @abstractmethod
    def produce(self) -> T_out: ...


class PureAProducer(Producer[A]):
    def produce(self) -> A:
        print(f"doing produce in {self.__class__.__name__}")
        a = A()
        return a


class PureBProducer(Producer[B]):
    def produce(self) -> B:
        print(f"doing produce in {self.__class__.__name__}")
        b = B()
        return b


class PureCProducer(Producer[C]):
    def produce(self) -> C:
        print(f"doing produce in {self.__class__.__name__}")
        c = C()
        return c


def with_some_a_producer(a_producer: Producer[A]) -> None:
    a = a_producer.produce()
    a.foo()
    # a.bar()
    # a.baz()


def with_some_b_producer(b_producer: Producer[B]) -> None:
    b = b_producer.produce()
    b.foo()
    b.bar()
    # b.baz()


def with_some_c_producer(c_producer: Producer[C]) -> None:
    c = c_producer.produce()
    c.foo()
    c.bar()
    c.baz()
