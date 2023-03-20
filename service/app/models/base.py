import datetime
from pydantic import BaseModel, validator, Field


class BaseObject(BaseModel):
  id_: int = Field(0, alias="id")
  create_time: datetime.datetime = None
  update_time: datetime.datetime = None
  delete_mark: bool = False

  @validator("create_time", "update_time", pre=True)
  def default_datetime(
      cls,
      value: datetime.datetime,
  ) -> datetime.datetime:
      return value or datetime.datetime.now()