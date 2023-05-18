from . import db
import datetime


class Record(db.Model):
    __tablename__ = "records"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    request = db.Column(db.String(100), unique=True, nullable=False)
    response = db.Column(db.String(100), unique=True, nullable=False)
    date_added_to_api = db.Column(db.DateTime, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def to_json(self):
        json_data = {
            'id': self.id,
            'request': self.request,
            'response': self.response,
            'datetime': self.date_added_to_api.strftime('%Y-%m-%d %H:%M:%S')
        }

        return json_data





