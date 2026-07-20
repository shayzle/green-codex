# this version has no energy problems

def build_feed(posts, users):
    user_map = {user.id: user for user in users}
    result = []
    for post in posts:
        matched = user_map.get(post.author_id)
        if matched:
            result.append((post, matched))
    return result