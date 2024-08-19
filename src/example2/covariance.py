from typing import Callable, TypeVar

from typing_extensions import TypeAlias

from example1.world import consume_a, consume_b, consume_c, consume_d, produce_a, produce_b, produce_c, produce_d

T_co = TypeVar("T_co", covariant=True)
# T_out = TypeVar("T_out", covariant=True)

ProduceFn: TypeAlias = Callable[[], T_co]


def with_produce_fn(produce_fn: ProduceFn[T_co]) -> T_co:
    something = produce_fn()
    return something


consume_a(with_produce_fn(produce_a))
consume_b(with_produce_fn(produce_a))
consume_c(with_produce_fn(produce_a))
consume_d(with_produce_fn(produce_a))


consume_a(with_produce_fn(produce_b))
consume_b(with_produce_fn(produce_b))
consume_c(with_produce_fn(produce_b))
consume_d(with_produce_fn(produce_b))


consume_a(with_produce_fn(produce_c))
consume_b(with_produce_fn(produce_c))
consume_c(with_produce_fn(produce_c))
consume_d(with_produce_fn(produce_c))


consume_a(with_produce_fn(produce_d))
consume_b(with_produce_fn(produce_d))
consume_c(with_produce_fn(produce_d))
consume_d(with_produce_fn(produce_d))
