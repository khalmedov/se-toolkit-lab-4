import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from app.models.item import ItemRecord
from app.models.learner import Learner
from app.models.interaction import InteractionLog

async def init_db():
    database_url = "postgresql+asyncpg://postgres:postgres@localhost:5432/lab-4"
    engine = create_async_engine(database_url, echo=True)
    
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    
    await engine.dispose()
    print("✅ Таблицы успешно созданы!")

if __name__ == "__main__":
    asyncio.run(init_db())
