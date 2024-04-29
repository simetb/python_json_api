from fastapi import FastAPI
from fake_champion_data import FAKE_CHAMPION_DATA

app = FastAPI()

# Base API route
@app.get("/")
async def root():
    return{"Your json api works fine :D"}

# Get all info
@app.get("/champions")
async def get_all_champions():
    return FAKE_CHAMPION_DATA

# Get all the champions name 
@app.get("/champions/names")
async def get_all_champions_names():
    return FAKE_CHAMPION_DATA["Names"]

# Get all the champion info
@app.get("/champions/{champion_name}")
async def get_champion_info(champion_name: str):
    return FAKE_CHAMPION_DATA[champion_name]

# Get all the champion aabilities
@app.get("/champions/{champion_name}/abilities")
async def get_champion_abilities(champion_name: str):
    return FAKE_CHAMPION_DATA[champion_name]["Abilities"]

# Get a specific champion ability
@app.get("/champions/{champion_name}/abilities/{ability_label}")
async def get_champion_ability(champion_name: str, ability_label: str):
    return FAKE_CHAMPION_DATA[champion_name]["Abilities"][ability_label]

# Get the champion passive
@app.get("/champions/{champion_name}/passive")
async def get_champion_passive(champion_name: str):
    return FAKE_CHAMPION_DATA[champion_name]["Passive"]

# Get the champion lane
@app.get("/champions/{champion_name}/lane")
async def get_champion_lane(champion_name: str):
    return FAKE_CHAMPION_DATA[champion_name]["Lane"]

# Get the champion ubication
@app.get("/champions/{champion_name}/ubication")
async def get_champion_ubication(champion_name: str):
    return FAKE_CHAMPION_DATA[champion_name]["Ubication"]