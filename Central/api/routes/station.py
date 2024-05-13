from fastapi import APIRouter, HTTPException

from typing import Any

from sqlmodel import func, select

from api.deps import CurrentUser, SessionDep
from models import (
    Measure,
    MeasureCreate,
    StationMeasurePublic,
    StationMeasuresPublic,
    Station,
    StationBase,
)

router = APIRouter()


@router.post(
    "/get_station_data",
    name="Receber Dados da Estação X",
    response_model=StationMeasuresPublic,
)
def receive_station_data(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    station_id: int,
    skip: int = 0,
    limit: int = 100
):
    if current_user.is_superuser:
        count_statement = (
            select(func.count())
            .select_from(Measure)
            .where(Measure.station_id == station_id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Measure)
            .offset(skip)
            .limit(limit)
            .where(Measure.station_id == station_id)
        )
        items = session.exec(statement).all()
    else:
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return StationMeasuresPublic(data=items, count=count)


@router.post("/send_data", name="Enviar Dados", response_model=StationMeasurePublic)
def send_data(
    *, session: SessionDep, current_user: CurrentUser, item_in: MeasureCreate
) -> Any:
    """
    Create new item.
    """
    measure = Measure.model_validate(item_in, update={"station_id": current_user.id})
    session.add(measure)
    session.commit()
    session.refresh(measure)
    return measure


@router.put("/register", name="Registrar Estação")
async def register_station(
    *, session: SessionDep, current_user: CurrentUser, item_in: StationBase
) -> Any:
    """
    Create new item.
    """
    station = Station.model_validate(item_in, update={"id": current_user.id})
    session.add(station)
    session.commit()
    session.refresh(station)
    return station


@router.get("/central_status", name="Status da Central")
async def get_status() -> str:
    return "Online"
