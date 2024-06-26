from sqlmodel import Field, Relationship, SQLModel
import datetime


# Shared properties
# TODO replace email str with EmailStr when sqlmodel supports it
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# TODO replace email str with EmailStr when sqlmodel supports it
class UserRegister(SQLModel):
    email: str
    password: str
    full_name: str | None = None


# Properties to receive via API on update, all are optional
# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdate(UserBase):
    email: str | None = None  # type: ignore
    password: str | None = None


# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdateMe(SQLModel):
    full_name: str | None = None
    email: str | None = None


class UpdatePassword(SQLModel):
    current_password: str
    new_password: str


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: int


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int


# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: int | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str


class StationBase(SQLModel):
    location: int
    description: str


# Database model, database table inferred from class name
class Station(StationBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime.datetime | None = Field(
        default_factory=datetime.datetime.now,
    )
    location: int
    description: str


class MeasureBase(SQLModel):
    station_id: int
    value: int


class MeasureCreate(SQLModel):
    value: int


# Database model, database table inferred from class name
class Measure(MeasureBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    station_id: int
    created_at: datetime.datetime | None = Field(
        default_factory=datetime.datetime.now,
    )
    value: int


class StationMeasurePublic(MeasureBase):
    created_at: datetime.datetime


class StationMeasuresPublic(SQLModel):
    data: list[StationMeasurePublic]
    count: int
