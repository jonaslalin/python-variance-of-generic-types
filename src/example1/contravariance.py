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

ConsumeAFn: TypeAlias = Callable[[A], None]
ConsumeBFn: TypeAlias = Callable[[B], None]
ConsumeCFn: TypeAlias = Callable[[C], None]
ConsumeDFn: TypeAlias = Callable[[D], None]


def with_consume_a_fn(consume_a_fn: ConsumeAFn, a: A) -> None:
    consume_a_fn(a)


def with_consume_b_fn(consume_b_fn: ConsumeBFn, b: B) -> None:
    consume_b_fn(b)


def with_consume_c_fn(consume_c_fn: ConsumeCFn, c: C) -> None:
    consume_c_fn(c)


def with_consume_d_fn(consume_d_fn: ConsumeDFn, d: D) -> None:
    consume_d_fn(d)


with_consume_a_fn(consume_a, produce_a())
with_consume_a_fn(consume_a, produce_b())
with_consume_a_fn(consume_a, produce_c())
with_consume_a_fn(consume_a, produce_d())

with_consume_b_fn(consume_a, produce_a())
with_consume_b_fn(consume_a, produce_b())
with_consume_b_fn(consume_a, produce_c())
with_consume_b_fn(consume_a, produce_d())

with_consume_c_fn(consume_a, produce_a())
with_consume_c_fn(consume_a, produce_b())
with_consume_c_fn(consume_a, produce_c())
with_consume_c_fn(consume_a, produce_d())

with_consume_d_fn(consume_a, produce_a())
with_consume_d_fn(consume_a, produce_b())
with_consume_d_fn(consume_a, produce_c())
with_consume_d_fn(consume_a, produce_d())


with_consume_a_fn(consume_b, produce_a())
with_consume_a_fn(consume_b, produce_b())
with_consume_a_fn(consume_b, produce_c())
with_consume_a_fn(consume_b, produce_d())

with_consume_b_fn(consume_b, produce_a())
with_consume_b_fn(consume_b, produce_b())
with_consume_b_fn(consume_b, produce_c())
with_consume_b_fn(consume_b, produce_d())

with_consume_c_fn(consume_b, produce_a())
with_consume_c_fn(consume_b, produce_b())
with_consume_c_fn(consume_b, produce_c())
with_consume_c_fn(consume_b, produce_d())

with_consume_d_fn(consume_b, produce_a())
with_consume_d_fn(consume_b, produce_b())
with_consume_d_fn(consume_b, produce_c())
with_consume_d_fn(consume_b, produce_d())


with_consume_a_fn(consume_c, produce_a())
with_consume_a_fn(consume_c, produce_b())
with_consume_a_fn(consume_c, produce_c())
with_consume_a_fn(consume_c, produce_d())

with_consume_b_fn(consume_c, produce_a())
with_consume_b_fn(consume_c, produce_b())
with_consume_b_fn(consume_c, produce_c())
with_consume_b_fn(consume_c, produce_d())

with_consume_c_fn(consume_c, produce_a())
with_consume_c_fn(consume_c, produce_b())
with_consume_c_fn(consume_c, produce_c())
with_consume_c_fn(consume_c, produce_d())

with_consume_d_fn(consume_c, produce_a())
with_consume_d_fn(consume_c, produce_b())
with_consume_d_fn(consume_c, produce_c())
with_consume_d_fn(consume_c, produce_d())


with_consume_a_fn(consume_d, produce_a())
with_consume_a_fn(consume_d, produce_b())
with_consume_a_fn(consume_d, produce_c())
with_consume_a_fn(consume_d, produce_d())

with_consume_b_fn(consume_d, produce_a())
with_consume_b_fn(consume_d, produce_b())
with_consume_b_fn(consume_d, produce_c())
with_consume_b_fn(consume_d, produce_d())

with_consume_c_fn(consume_d, produce_a())
with_consume_c_fn(consume_d, produce_b())
with_consume_c_fn(consume_d, produce_c())
with_consume_c_fn(consume_d, produce_d())

with_consume_d_fn(consume_d, produce_a())
with_consume_d_fn(consume_d, produce_b())
with_consume_d_fn(consume_d, produce_c())
with_consume_d_fn(consume_d, produce_d())
