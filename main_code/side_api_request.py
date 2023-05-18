import requests
from .models import Record
from . import db
from datetime import datetime


def make_request(url:str, count: str):
    response = requests.get(url, params={'count': count})
    data_list = response.json()
    new_records = []
    for item in data_list:
        query = Record.query.filter_by(id=item['id']).first()
        if query:
            make_request(url, count='1')
        else:
            new_record = Record(id=item['id'],
                                request=item['question'],
                                response=item['answer'],
                                date_added_to_api=datetime.strptime(item['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
                                )
            db.session.add(new_record)
            db.session.commit()
        new_records.append(new_record)
        return new_record


def handle_post_request(sender, **kwargs):
    count = kwargs['count']
    url = 'https://jservice.io/api/random'
    return make_request(url, count)
