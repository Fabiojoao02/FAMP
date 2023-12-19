from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path
from sqlalchemy.orm.decl_api import DeclarativeMeta

from typing import ClassVar


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:delta@localhost:5432/faculdade"
    # DB_URL: str = "postgresql+asyncpg://fbi:delta@localhost:5432/faculdade"
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
    TEMPLATES: ClassVar[Jinja2Templates] = Jinja2Templates(
        directory='templates')
    MEDIA: ClassVar[Path] = Path('media')
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings: Settings = Settings()
