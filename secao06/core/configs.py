from typing import List

# from pydantic import BaseSettings
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm.decl_api import DeclarativeMeta
from fastapi.templating import Jinja2Templates
from pathlib import Path

from typing import ClassVar


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:delta@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
    TEMPLATES: ClassVar[Jinja2Templates] = Jinja2Templates(
        directory='templates')
    MEDIA: ClassVar[Path] = Path('media')
    DBBaseModel = declarative_base()

    JWT_SECRET: str = '9jeRfqk2JW2ShzR6MzAQFA-g0f1dO0ZYKCJf8YNegEY'
    """
    python <enter> digitar no terminal
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
