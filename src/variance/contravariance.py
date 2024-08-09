from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .models import A, B, C

T_in = TypeVar("T_in", contravariant=True)
# T_contra = TypeVar("T_contra", contravariant=True)


class Consumer(ABC, Generic[T_in]):
    @abstractmethod
    def consume(self, value: T_in, /) -> None: ...


class PureAConsumer(Consumer[A]):
    def consume(self, a: A, /) -> None:
        print(f"doing consume in {self.__class__.__name__}")
        a.foo()


class PureBConsumer(Consumer[B]):
    def consume(self, b: B, /) -> None:
        print(f"doing consume in {self.__class__.__name__}")
        b.foo()
        b.bar()


class PureCConsumer(Consumer[C]):
    def consume(self, c: C, /) -> None:
        print(f"doing consume in {self.__class__.__name__}")
        c.foo()
        c.bar()
        c.baz()


def with_some_a_consumer(a_consumer: Consumer[A]) -> None:
    a, b, c = A(), B(), C()
    a_consumer.consume(a)
    a_consumer.consume(b)
    a_consumer.consume(c)


def with_some_b_consumer(b_consumer: Consumer[B]) -> None:
    a, b, c = A(), B(), C()  # noqa: F841
    # b_consumer.consume(a)
    b_consumer.consume(b)
    b_consumer.consume(c)


def with_some_c_consumer(c_consumer: Consumer[C]) -> None:
    a, b, c = A(), B(), C()  # noqa: F841
    # c_consumer.consume(a)
    # c_consumer.consume(b)
    c_consumer.consume(c)
