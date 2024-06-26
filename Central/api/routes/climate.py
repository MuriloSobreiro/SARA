from fastapi import APIRouter, HTTPException

from typing import Any

from api.deps import CurrentUser

from utils import get_api_climate

router = APIRouter()


@router.post(
    "/get_climate_data",
    name="Receber dados de clima",
)
def receive_station_data(
    *,
    current_user: CurrentUser,
    cidade: str,
    lat: str = "",
    lon: str = ""
):
    if current_user.is_superuser:
        r = get_api_climate(cidade, lat, lon)
    else:
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return r
