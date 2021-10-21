import uuid


def get_uid():
    """Randomise suffix for profile unique slug."""
    uid = str(uuid.uuid4())[:6].replace("-", "").lower()
    return uid
