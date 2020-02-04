from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __repr__(self):
        return '<User %r>' % self.id


class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    user = db.relationship('User', backref='users.id')
    thumbnail_link = db.Column(db.String(100))
    photo_link = db.Column(db.String(100))
    processed_link = db.Column(db.String(100))

    def __repr__(self):
        return '<Photo %r>' % self.id