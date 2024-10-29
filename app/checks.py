def check_data_create_cake(data: dict = None) -> str:
    if not data:
        return "Data is None"

    if data.get("name", None):
        if not isinstance(data["name"], str):
            return "Name field must be a string type"
        if len(data["name"]) > 100:
            return "Name length must be <= 100 symbols"
    else:
        return "Name is None"

    if data.get("flavor", None):
        if not isinstance(data["flavor"], str):
            return "Flavor field must be a string type"
        if len(data["flavor"]) > 100:
            return "Flavor length must be <= 100 symbols"
    else:
        return "Flavor is None"

    if data.get("price"):
        if not isinstance(data["price"], (int, float)):
            return "Price field must be numeric type"
    else:
        return "Price is None"

    if data.get("available", None) is not None:
        if not isinstance(data["available"], bool):
            return "Available must be boolean type"
    else:
        return "Available is None"

    return "OK"


def check_data_update_cake(data: dict = None) -> str:
    if not data:
        return "Data is None"

    if data.get("name", None):
        if not isinstance(data["name"], str):
            return "Name field must be string"

    if data.get("flavor", None):
        if not isinstance(data["flavor"], str):
            return "Flavor field must be string"

    if data.get("price", None):
        if not isinstance(data["price"], (int, float)):
            return "Price field must be numeric"

    if data.get("available", None) is not None:
        if not isinstance(data["available"], bool):
            return "Available field must be boolean"

    return "OK"


def check_data_create_bakery(data: dict = None) -> str:
    if not data:
        return "Data is None"

    if data.get("name", None):
        if not isinstance(data["name"], str):
            return f"Name field must be string"
        if len(data["name"]) > 100:
            return "Name field must be <= 100 characters"
    else:
        return "Name field is None"

    if data.get("location", None):
        if not isinstance(data["location"], str):
            return "Location field must be string"
        if len(data["location"]) > 100:
            return "Location must be <= 100 characters"
    else:
        return "Location is None"

    if data.get("rating", None) is not None:
        if not isinstance(data["rating"], (int, float)):
            return "Rating must be numeric type"
    else:
        return "Rating is None"

    return "OK"


def check_data_update_bakery(data: dict) -> str:
    if not data:
        return "Data is None"

    if data.get("name", None):
        if not isinstance(data["name"], str):
            return "Name must be string"
        if len(data["name"]) > 100:
            return "Name must be <= 100 characters"

    if data.get("location", None):
        if not isinstance(data["location"], str):
            return "Location must be string"
        if len(data["location"]) > 100:
            return "Location must be <= 100 characters"

    if data.get("rating", None):
        if not isinstance(data["rating"], (int, float)):
            return "Rating must be numeric type"

    return "OK"