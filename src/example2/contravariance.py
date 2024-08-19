from typing import Callable, TypeVar

from typing_extensions import TypeAlias

from example1.world import consume_a, consume_b, consume_c, consume_d, produce_a, produce_b, produce_c, produce_d

T_contra = TypeVar("T_contra", contravariant=True)
# T_in = TypeVar("T_in", contravariant=True)

ConsumeFn: TypeAlias = Callable[[T_contra], None]


def with_consume_fn(consume_fn: ConsumeFn[T_contra], something: T_contra) -> None:
    consume_fn(something)


with_consume_fn(consume_a, produce_a())
with_consume_fn(consume_a, produce_b())
with_consume_fn(consume_a, produce_c())
with_consume_fn(consume_a, produce_d())


with_consume_fn(consume_b, produce_a())
with_consume_fn(consume_b, produce_b())
with_consume_fn(consume_b, produce_c())
with_consume_fn(consume_b, produce_d())


with_consume_fn(consume_c, produce_a())
with_consume_fn(consume_c, produce_b())
with_consume_fn(consume_c, produce_c())
with_consume_fn(consume_c, produce_d())


with_consume_fn(consume_d, produce_a())
with_consume_fn(consume_d, produce_b())
with_consume_fn(consume_d, produce_c())
with_consume_fn(consume_d, produce_d())
