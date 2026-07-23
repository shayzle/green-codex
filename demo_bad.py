def build_feed(posts, users):
    result = []
    for post in posts:
        for user in users:
            result.append((post, user))
    return result

def load_comments(ids, db):
    out = []
    for i in ids:
        out.append(db.query(i))
    return out