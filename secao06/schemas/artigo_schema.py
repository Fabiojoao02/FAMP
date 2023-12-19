from typing import Optional


from pydantic import BaseModel as SCBaseModel
from pydantic import HttpUrl, validator


class ArtigoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: str  # HttpUrl
    usuario_id: Optional[int] = None

    @validator("url_fonte", pre=True, always=True)
    def convert_url_to_str(cls, value):
        return str(value)

    class Config:
        # orm_mode = True
        from_attributes = True
        validate_assignment = False
