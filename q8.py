# Team Name: Codepy

def sanitize_email(raw_input: str) -> str:
    cleaned = raw_input.strip().lower()

    if cleaned == "":
        return "Invalid Email"

    if cleaned.count("@") != 1:
        return "Invalid Email"

    local, domain = cleaned.split("@")

    if local == "" or domain == "":
        return "Invalid Email"

    return cleaned
