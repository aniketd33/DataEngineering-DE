def transform_data(data):

    transformed = {
        "current_user_url": data.get("current_user_url"),
        "repository_url": data.get("repository_url"),
        "organization_url": data.get("organization_url")
    }

    return transformed