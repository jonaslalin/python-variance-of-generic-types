from typing import Callable, TypeVar

from typing_extensions import TypeAlias

from example1.world import (
    consume_a,
    consume_and_produce_a,
    consume_and_produce_b,
    consume_and_produce_c,
    consume_and_produce_d,
    consume_b,
    consume_c,
    consume_d,
    produce_a,
    produce_b,
    produce_c,
    produce_d,
)

T = TypeVar("T")
# T = TypeVar("T", covariant=False, contravariant=False)


ConsumeAndProduceFn: TypeAlias = Callable[[T], T]


def with_consume_and_produce_fn(consume_and_produce_fn: ConsumeAndProduceFn[T], something: T) -> T:
    new_something = consume_and_produce_fn(something)
    return new_something


consume_a(with_consume_and_produce_fn(consume_and_produce_a, produce_a()))
consume_a(with_consume_and_produce_fn(consume_and_produce_a, produce_b()))
consume_a(with_consume_and_produce_fn(consume_and_produce_a, produce_c()))
consume_a(with_consume_and_produce_fn(consume_and_produce_a, produce_d()))

consume_b(with_consume_and_produce_fn(consume_and_produce_a, produce_a()))
consume_b(with_consume_and_produce_fn(consume_and_produce_a, produce_b()))
consume_b(with_consume_and_produce_fn(consume_and_produce_a, produce_c()))
consume_b(with_consume_and_produce_fn(consume_and_produce_a, produce_d()))

consume_c(with_consume_and_produce_fn(consume_and_produce_a, produce_a()))
consume_c(with_consume_and_produce_fn(consume_and_produce_a, produce_b()))
consume_c(with_consume_and_produce_fn(consume_and_produce_a, produce_c()))
consume_c(with_consume_and_produce_fn(consume_and_produce_a, produce_d()))

consume_d(with_consume_and_produce_fn(consume_and_produce_a, produce_a()))
consume_d(with_consume_and_produce_fn(consume_and_produce_a, produce_b()))
consume_d(with_consume_and_produce_fn(consume_and_produce_a, produce_c()))
consume_d(with_consume_and_produce_fn(consume_and_produce_a, produce_d()))


consume_a(with_consume_and_produce_fn(consume_and_produce_b, produce_a()))
consume_a(with_consume_and_produce_fn(consume_and_produce_b, produce_b()))
consume_a(with_consume_and_produce_fn(consume_and_produce_b, produce_c()))
consume_a(with_consume_and_produce_fn(consume_and_produce_b, produce_d()))

consume_b(with_consume_and_produce_fn(consume_and_produce_b, produce_a()))
consume_b(with_consume_and_produce_fn(consume_and_produce_b, produce_b()))
consume_b(with_consume_and_produce_fn(consume_and_produce_b, produce_c()))
consume_b(with_consume_and_produce_fn(consume_and_produce_b, produce_d()))

consume_c(with_consume_and_produce_fn(consume_and_produce_b, produce_a()))
consume_c(with_consume_and_produce_fn(consume_and_produce_b, produce_b()))
consume_c(with_consume_and_produce_fn(consume_and_produce_b, produce_c()))
consume_c(with_consume_and_produce_fn(consume_and_produce_b, produce_d()))

consume_d(with_consume_and_produce_fn(consume_and_produce_b, produce_a()))
consume_d(with_consume_and_produce_fn(consume_and_produce_b, produce_b()))
consume_d(with_consume_and_produce_fn(consume_and_produce_b, produce_c()))
consume_d(with_consume_and_produce_fn(consume_and_produce_b, produce_d()))


consume_a(with_consume_and_produce_fn(consume_and_produce_c, produce_a()))
consume_a(with_consume_and_produce_fn(consume_and_produce_c, produce_b()))
consume_a(with_consume_and_produce_fn(consume_and_produce_c, produce_c()))
consume_a(with_consume_and_produce_fn(consume_and_produce_c, produce_d()))

consume_b(with_consume_and_produce_fn(consume_and_produce_c, produce_a()))
consume_b(with_consume_and_produce_fn(consume_and_produce_c, produce_b()))
consume_b(with_consume_and_produce_fn(consume_and_produce_c, produce_c()))
consume_b(with_consume_and_produce_fn(consume_and_produce_c, produce_d()))

consume_c(with_consume_and_produce_fn(consume_and_produce_c, produce_a()))
consume_c(with_consume_and_produce_fn(consume_and_produce_c, produce_b()))
consume_c(with_consume_and_produce_fn(consume_and_produce_c, produce_c()))
consume_c(with_consume_and_produce_fn(consume_and_produce_c, produce_d()))

consume_d(with_consume_and_produce_fn(consume_and_produce_c, produce_a()))
consume_d(with_consume_and_produce_fn(consume_and_produce_c, produce_b()))
consume_d(with_consume_and_produce_fn(consume_and_produce_c, produce_c()))
consume_d(with_consume_and_produce_fn(consume_and_produce_c, produce_d()))


consume_a(with_consume_and_produce_fn(consume_and_produce_d, produce_a()))
consume_a(with_consume_and_produce_fn(consume_and_produce_d, produce_b()))
consume_a(with_consume_and_produce_fn(consume_and_produce_d, produce_c()))
consume_a(with_consume_and_produce_fn(consume_and_produce_d, produce_d()))

consume_b(with_consume_and_produce_fn(consume_and_produce_d, produce_a()))
consume_b(with_consume_and_produce_fn(consume_and_produce_d, produce_b()))
consume_b(with_consume_and_produce_fn(consume_and_produce_d, produce_c()))
consume_b(with_consume_and_produce_fn(consume_and_produce_d, produce_d()))

consume_c(with_consume_and_produce_fn(consume_and_produce_d, produce_a()))
consume_c(with_consume_and_produce_fn(consume_and_produce_d, produce_b()))
consume_c(with_consume_and_produce_fn(consume_and_produce_d, produce_c()))
consume_c(with_consume_and_produce_fn(consume_and_produce_d, produce_d()))

consume_d(with_consume_and_produce_fn(consume_and_produce_d, produce_a()))
consume_d(with_consume_and_produce_fn(consume_and_produce_d, produce_b()))
consume_d(with_consume_and_produce_fn(consume_and_produce_d, produce_c()))
consume_d(with_consume_and_produce_fn(consume_and_produce_d, produce_d()))
