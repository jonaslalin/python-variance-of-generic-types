# python-variance-of-generic-types

> ## Variance rules of thumb
>
> Finally, here are a few rules of thumb to reason about when thinking through variance:
>
> * If a formal type parameter defines a type for data that comes out of the object, it can be covariant.
> * If a formal type parameter defines a type for data that goes into the object after its initial construction, it can be contravariant.
> * If a formal type parameter defines a type for data that comes out of the object and the same parameter defines a type for data that goes into the object, it must be invariant.
> * To err on the safe side, make formal type parameters invariant.
>
> This suggests that a good naming convention for covariant and contravariant type variables in Python would be:
>
> ```python
> T_out = TypeVar('T_out', covariant=True)
> T_in = TypeVar('T_in', contravariant=True)
> ```
>
> Is it too late to change the naming convention established in [PEP 484](https://peps.python.org/pep-0484/)?
>
> Source: [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/), by Luciano Ramalho.
