def register_user(db, username, password):
    db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, password)
            )
    db.commit()

def get_user_by_name(db, username):
    return db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()