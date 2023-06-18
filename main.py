import secrets

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='One time secret')

fake_secrets = []


class Secret(BaseModel):
    secret: str
    code_phrase: str


@app.get('/')
def index():
    return {'Greeting message': 'Hello, user!'}


@app.post('/generate')
def generate_secret(secret_data: Secret):
    secret_key = secrets.token_urlsafe(16)
    data = {}
    data['secret_key'] = secret_key
    data['secret'] = secret_data.secret
    data['code_phrase'] = secret_data.code_phrase
    fake_secrets.append(data)
    return {'status': 200, 'data': fake_secrets}


@app.post('/secrets/{secret_key}')
def get_secret(secret_key: str, code_phrase: str):
    for index, item in enumerate(fake_secrets):
        if (item['secret_key'] == secret_key
                and item['code_phrase'] == code_phrase):
            secret = item['secret']
            del fake_secrets[index]
            return {'secret': secret}
    return {'error': 'Invalid secret key or code phrase'}
