from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SimCard(BaseModel):
    sim_number: int          # SIM number (unique identifier)
    phone_number: int        # Phone number
    status: bool             # Status of the SIM (active/inactive)
    activation_date: Optional[datetime]  # Activation date (nullable for inactive SIMs)
    
    # class Config:
    #     orm_mode = True  # Enable ORM mode for compatibility with databases