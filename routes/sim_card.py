from fastapi import APIRouter, HTTPException
from config.db import conn
from models.sim_card import SimCard
from schemas.sim_card import serializeDict
from bson import ObjectId
from datetime import datetime

sim_card = APIRouter()

# Activate SIM Card
@sim_card.post("/activate")
async def activate_sim(sim: SimCard):
    sim_record = conn.SIM_DETAILS.sim_cards.find_one({"sim_number": sim.sim_number})
    
    if sim_record:
        if sim_record["status"] == True:
            raise HTTPException(status_code=400, detail="SIM card is already active.")
        else:
            activation_date = datetime.now()
            conn.SIM_DETAILS.sim_cards.update_one(
                {"sim_number": sim.sim_number},
                {"$set": {"status": True, "activation_date": activation_date}}
            )
            return {"message": f"SIM {sim.sim_number} activated successfully."}
    else:
        # SIM does not exist, create a new entry and activate
        conn.SIM_DETAILS.sim_cards.insert_one({
            "sim_number": sim.sim_number,
            "phone_number": sim.phone_number,
            "status": True,
            "activation_date": datetime.now()
        })
        return {"message": f"SIM {sim.sim_number} created and activated."}

# Deactivate SIM Card
@sim_card.post("/deactivate")
async def deactivate_sim(sim: SimCard):
    sim_record = conn.SIM_DETAILS.sim_cards.find_one({"sim_number": sim.sim_number})

    if sim_record:
        if sim_record["status"] == False:
            raise HTTPException(status_code=400, detail="SIM card is already inactive.")
        else:
            conn.SIM_DETAILS.sim_cards.update_one(
                {"sim_number": sim.sim_number},
                {"$set": {"status": False, "activation_date": None}}
            )
            return {"message": f"SIM {sim.sim_number} deactivated successfully."}
    else:
        raise HTTPException(status_code=404, detail="SIM card not found.")

# Get SIM Details
@sim_card.get("/sim-details/{sim_number}")
async def get_sim_details(sim_number: str):
    sim_record = conn.SIM_DETAILS.sim_cards.find_one({"sim_number": sim_number})
    
    if sim_record:
        return serializeDict(sim_record)
    else:
        raise HTTPException(status_code=404, detail="SIM card not found.")
