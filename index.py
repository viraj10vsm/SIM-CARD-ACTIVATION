from fastapi import FastAPI
from routes.sim_card import sim_card

app = FastAPI()

app.include_router(sim_card)