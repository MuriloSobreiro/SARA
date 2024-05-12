from pydantic import BaseModel


class StationData(BaseModel):
    id: str
    pressure: int
