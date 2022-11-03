from typing import List

from sdv.domain.entities.abstract_actor_entity import AbstractActorEntity
from sdv.domain.ports.resources_repository import ResourcesRepository


class ActorSQLRepository(ResourcesRepository):

    def find_all(self) -> List[AbstractActorEntity]:
        pass

    def find_by_id(self, ids: List[int]) -> List[AbstractActorEntity]:
        pass
