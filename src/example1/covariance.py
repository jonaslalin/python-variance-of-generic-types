from typing import Callable

from typing_extensions import TypeAlias

from example1.world import (
    A,
    B,
    C,
    D,
    consume_a,
    consume_b,
    consume_c,
    consume_d,
    produce_a,
    produce_b,
    produce_c,
    produce_d,
)

ProduceAFn: TypeAlias = Callable[[], A]
ProduceBFn: TypeAlias = Callable[[], B]
ProduceCFn: TypeAlias = Callable[[], C]
ProduceDFn: TypeAlias = Callable[[], D]


def with_produce_a_fn(produce_a_fn: ProduceAFn) -> A:
    a = produce_a_fn()
    return a


def with_produce_b_fn(produce_b_fn: ProduceBFn) -> B:
    b = produce_b_fn()
    return b


def with_produce_c_fn(produce_c_fn: ProduceCFn) -> C:
    c = produce_c_fn()
    return c


def with_produce_d_fn(produce_d_fn: ProduceDFn) -> D:
    d = produce_d_fn()
    return d


consume_a(with_produce_a_fn(produce_a))
consume_b(with_produce_a_fn(produce_a))
consume_c(with_produce_a_fn(produce_a))
consume_d(with_produce_a_fn(produce_a))

consume_a(with_produce_b_fn(produce_a))
consume_b(with_produce_b_fn(produce_a))
consume_c(with_produce_b_fn(produce_a))
consume_d(with_produce_b_fn(produce_a))

consume_a(with_produce_c_fn(produce_a))
consume_b(with_produce_c_fn(produce_a))
consume_c(with_produce_c_fn(produce_a))
consume_d(with_produce_c_fn(produce_a))

consume_a(with_produce_d_fn(produce_a))
consume_b(with_produce_d_fn(produce_a))
consume_c(with_produce_d_fn(produce_a))
consume_d(with_produce_d_fn(produce_a))


consume_a(with_produce_a_fn(produce_b))
consume_b(with_produce_a_fn(produce_b))
consume_c(with_produce_a_fn(produce_b))
consume_d(with_produce_a_fn(produce_b))

consume_a(with_produce_b_fn(produce_b))
consume_b(with_produce_b_fn(produce_b))
consume_c(with_produce_b_fn(produce_b))
consume_d(with_produce_b_fn(produce_b))

consume_a(with_produce_c_fn(produce_b))
consume_b(with_produce_c_fn(produce_b))
consume_c(with_produce_c_fn(produce_b))
consume_d(with_produce_c_fn(produce_b))

consume_a(with_produce_d_fn(produce_b))
consume_b(with_produce_d_fn(produce_b))
consume_c(with_produce_d_fn(produce_b))
consume_d(with_produce_d_fn(produce_b))


consume_a(with_produce_a_fn(produce_c))
consume_b(with_produce_a_fn(produce_c))
consume_c(with_produce_a_fn(produce_c))
consume_d(with_produce_a_fn(produce_c))

consume_a(with_produce_b_fn(produce_c))
consume_b(with_produce_b_fn(produce_c))
consume_c(with_produce_b_fn(produce_c))
consume_d(with_produce_b_fn(produce_c))

consume_a(with_produce_c_fn(produce_c))
consume_b(with_produce_c_fn(produce_c))
consume_c(with_produce_c_fn(produce_c))
consume_d(with_produce_c_fn(produce_c))

consume_a(with_produce_d_fn(produce_c))
consume_b(with_produce_d_fn(produce_c))
consume_c(with_produce_d_fn(produce_c))
consume_d(with_produce_d_fn(produce_c))


consume_a(with_produce_a_fn(produce_d))
consume_b(with_produce_a_fn(produce_d))
consume_c(with_produce_a_fn(produce_d))
consume_d(with_produce_a_fn(produce_d))

consume_a(with_produce_b_fn(produce_d))
consume_b(with_produce_b_fn(produce_d))
consume_c(with_produce_b_fn(produce_d))
consume_d(with_produce_b_fn(produce_d))

consume_a(with_produce_c_fn(produce_d))
consume_b(with_produce_c_fn(produce_d))
consume_c(with_produce_c_fn(produce_d))
consume_d(with_produce_c_fn(produce_d))

consume_a(with_produce_d_fn(produce_d))
consume_b(with_produce_d_fn(produce_d))
consume_c(with_produce_d_fn(produce_d))
consume_d(with_produce_d_fn(produce_d))
