from pymfdata.rdb.mapper import mapper_registry

from src.persistence.author.entity import AuthorBookEntity, AuthorEntity, relationship

from .dto import AuthorDTO


def start_mapper():
    t = AuthorEntity.__table__

    mapper_registry.map_imperatively(
        AuthorDTO,
        t,
        properties={"books": relationship(AuthorBookEntity, viewonly=True, lazy="joined")},
    )
