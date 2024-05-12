from pydantic import BaseModel


class StationData(BaseModel):
    id: str
    pressure: int


class StationInfo(BaseModel):
    id: str
    location: str
