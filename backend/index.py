from fastapi import FastAPI
from routers.user import api as api_u
from routers.time_record import api as api_t
from routers.organization import api as api_o
from routers.login import api as api_l
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:80",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_u)
app.include_router(api_t)
app.include_router(api_o)
app.include_router(api_l)