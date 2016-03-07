from run_app import db
from datetime import datetime


class Rooms(db.Model):
    __tablename__ = 'users_chat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    room_id = db.Column(db.String(80))
    time = db.Column(db.DateTime, default=datetime.now())
    messages_1_ = db.Column(db.Text)
    messages_2_ = db.Column(db.Text)
    checked = db.Column(db.Boolean, default=False)

    def __init__(self, room_id, time=None, user1_mes=None, user2_mes=None):
        self.room_id = room_id
        if time is not None:
            self.time = time

        self.user1_mes = user1_mes
        self.user2_mes = user2_mes


db.create_all()
