from .auth import router as auth_router
from .teams import router as teams_router
from .projects import router as projects_router
from .tasks import router as tasks_router

all_routers = [
    auth_router,
    teams_router,
    projects_router,
    tasks_router,
]
