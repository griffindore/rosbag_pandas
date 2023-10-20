def topics_from_keys(keys):
    """
    Extracts the desired topics from specified keys
    :param Keys: List of desired keys
    :return: List of topics
    """
    topics = set()
    for key in keys:
        if not key.startswith("/"):
            key = "/" + key
        chunks = key.split("/")
        for i in range(2, len(chunks)):
            topics.add("/".join(chunks[0:i]))
    return list(topics)
