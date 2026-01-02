def check_access(user):
    return user.plan in ["builder", "enterprise"]
