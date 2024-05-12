from fastapi import APIRouter, status

from schemas.stationData import StationData

router = APIRouter()


@router.post(
    "/send_data",
    name="Enviar Dados",
)
async def send_data(data: StationData) -> str:
    return "Ok"


@router.get("/central_status", name="Status da Central")
async def get_status() -> str:
    return "Online"
