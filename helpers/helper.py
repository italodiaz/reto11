import os
from flask import json, request, jsonify
from dotenv import load_dotenv
from pathlib import Path
from functools import wraps
from jwt import decode

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def handler_response(app, code_error, output, validate=True, payload=None):
    if payload is None:
        payload = {}

    response_object = {
        'response': {
            'system_message': output,
            'api_response': payload,
            'validate': validate,
            'status_code': code_error
        }
    }

    response = app.response_class(
        response=json.dumps(response_object),
        status=code_error,
        mimetype='application/json'
    )

    return response

def jwt_secret():
    return os.getenv('JWT_SECRET')

def token_required(f):
    @wraps(f)
    def decorator(*ars, **kwargs):
        token = request.headers.get('_token')

        if not token:
            return jsonify({
                'response': {
                    'system_message': 'Token no encontrado',
                    'api_response': {},
                    'status_code': 401
                }
            })

        try:
            decode(token, jwt_secret())
        except Exception as e:
            return jsonify({
                'response': {
                    'system_message': 'Token incorrecto',
                    'api_response': {
                        'error': f'{str(e)}'
                    },
                    'status_code': 401
                }
            })

        return f(*ars, **kwargs)

    return decorator