from fastapi import APIRouter

from api.routes import login, station, users, utils, climate

router = APIRouter()

router.include_router(login.router, tags=["login"])
router.include_router(station.router, prefix="/station", tags=["station"])
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(utils.router, prefix="/utils", tags=["utils"])
router.include_router(climate.router, prefix="/climate", tags=["climate"])
