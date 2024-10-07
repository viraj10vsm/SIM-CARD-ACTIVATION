# Normal way
def simCardEntity(item) -> dict:
    return {
        "sim_number": str(item["sim_number"]),
        "phone_number": str(item["phone_number"]),
        "status": "active" if item["status"] else "inactive",
        "activation_date": str(item["activation_date"]) if item["activation_date"] else None
    }

def simCardsEntity(entity) -> list:
    return [simCardEntity(item) for item in entity]


# Best way
def serializeDict(a) -> dict:
    # Convert '_id' (or other IDs) to string, serialize the rest as-is
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}

def serializeList(entity) -> list:
    # Apply serialization to each item in the list
    return [serializeDict(a) for a in entity]