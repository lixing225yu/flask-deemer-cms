from pydantic.main import BaseModel
from pydantic.fields import Field


class PagedModel(BaseModel):
    page: int = Field(default=1, description="页码", gt=0)
    page_size: int = Field(default=20, description="每页数量", gt=0, le=50)

