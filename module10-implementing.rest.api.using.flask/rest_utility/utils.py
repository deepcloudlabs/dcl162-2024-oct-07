def extract_body(request, fields):
    employee = {}
    for field in fields:
        if field in request.json:
            employee[field] = request.json[field]
        if "identity" in employee:
            employee["_id"] = request.json["identity"]
    return employee