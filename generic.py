from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')


class Interface(ABC, Generic[T]):
    @abstractmethod
    def get(self, id) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    def add(self, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, **kwargs) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id) -> None:
        raise NotImplementedError

# class UserInterface(Interface[User]):
#     # Implement the abstract methods for the User type
#     pass
