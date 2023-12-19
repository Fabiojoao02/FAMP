from core.configs import settings
# from sqlalchemy.orm import Mapped

from sqlalchemy import Column, Integer, String


class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'
    # __allow_unmapped__ = True

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    # id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)
