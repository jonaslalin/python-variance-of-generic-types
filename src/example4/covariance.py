from abc import ABC, abstractmethod
from typing import Generic, TypeVar


class CatFood:
    pass


class Cat:
    def feed(self, cat_food: CatFood) -> None:
        pass


class Ragdoll(Cat):
    def cuddle(self) -> None:
        pass


class CuddleError(Exception):
    pass


class Tiger(Cat):
    def cuddle(self) -> None:
        raise CuddleError("Too dangerous to cuddle with a Tiger")


T = TypeVar("T", covariant=True)


class AnimalShelter(Generic[T], ABC):
    @abstractmethod
    def adopt(self) -> T: ...


class CatShelter(AnimalShelter[Cat]):
    def adopt(self) -> Cat:
        return Tiger()  # Danger!!!


class RagdollShelter(AnimalShelter[Ragdoll]):
    def adopt(self) -> Ragdoll:
        return Ragdoll()


class TigerShelter(AnimalShelter[Tiger]):
    def adopt(self) -> Tiger:
        return Tiger()


def with_ragdoll_shelter(ragdoll_shelter: AnimalShelter[Ragdoll]) -> None:
    ragdoll = ragdoll_shelter.adopt()
    ragdoll.cuddle()


with_ragdoll_shelter(CatShelter())
with_ragdoll_shelter(RagdollShelter())
with_ragdoll_shelter(TigerShelter())


def with_cat_shelter(cat_shelter: AnimalShelter[Cat]) -> None:
    cat = cat_shelter.adopt()
    cat.feed(CatFood())
    if isinstance(ragdoll := cat, Ragdoll):
        ragdoll.cuddle()


with_cat_shelter(CatShelter())
with_cat_shelter(RagdollShelter())
with_cat_shelter(TigerShelter())
