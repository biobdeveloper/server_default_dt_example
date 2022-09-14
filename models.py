from sqlalchemy.orm import declarative_base
import sqlalchemy as sa

metadata = sa.MetaData()

Base = declarative_base(metadata=metadata)


class Foo(Base):
    __tablename__ = 'foo'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now())

    def as_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
            if getattr(self, column.name) is not None
        }
