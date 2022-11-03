from sqlalchemy.orm import declarative_base

from sdv.infrastructure.sql.entities.actor_sql import ActorSQL

Base = declarative_base()

ActorSQL(Base)