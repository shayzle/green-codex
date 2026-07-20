# just for testing

def build_feed(posts, users):
    result = []
    for post in posts:   # outer loop
        for user in users:   # inner loop -> NESTED_LOOP
            if post.author_id == user.id:
                result.append((post, user))
    return result

def load_comments(post_ids, db):
    comments = []
    for pid in post_ids:
        comments.append(db.query(pid))   # query in loop -> QUERY_IN_LOOP
    return comments