import abc
from typing import List

from abc import ABCMeta


from sdv.domain.entities.abstract_actor_entity import AbstractActorEntity


class ResourcesRepository(metaclass=ABCMeta):
    @abc.abstractmethod
    def find_all(self) -> List[AbstractActorEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_id(self, ids:List[int]) -> List[AbstractActorEntity]:
        raise NotImplementedError
