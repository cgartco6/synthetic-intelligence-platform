def has_access(user):
    return user["plan"] in ["builder", "enterprise"]
