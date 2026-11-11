#This schemas file is responsible for serving as the communication between the APIS and the database models
from pydantic import BaseModel, ConfigDict


class SpectatorSourceBase(BaseModel):
    name: str
    email: str

class SpectatorSourceCreate(SpectatorSourceBase):
    pass


class SpectatorSource(SpectatorSourceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
