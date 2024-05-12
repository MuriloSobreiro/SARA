from fastapi import APIRouter

from api.routes.station import router as station_data

router = APIRouter()

router.include_router(station_data, prefix="/station")
