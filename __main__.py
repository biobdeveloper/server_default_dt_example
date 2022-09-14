import asyncio

from models import Foo
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa


engine = create_async_engine(
    url='postgresql+asyncpg://postgres:password@0.0.0.0:5432/postgres'
)
session_factory = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def main():
    async with session_factory() as session:
        # Create some record
        foo = Foo(name='Hello, alembic')
        foo.id = (await session.execute(sa.insert(Foo).values(foo.as_dict()).returning(Foo.id))).scalar_one()
        await session.commit()

        # Update it
        await session.execute(sa.update(Foo).values(name='Update, alembic'))
        await session.commit()

        # Check that updated_at is different from created_at
        foo = (await session.execute(sa.select(Foo).where(Foo.id == foo.id))).scalar()
        assert foo.updated_at > foo.created_at
        print(f"{foo.updated_at} > {foo.created_at}")

asyncio.get_event_loop().run_until_complete(main())
