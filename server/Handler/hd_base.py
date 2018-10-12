from flask import jsonify, request, abort, make_response
from server import app
from functools import wraps

def require(*required_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            for arg in required_args:
                if arg not in request.json:
                    return abort(400)
            return func(*args, **kw)
        return wrapper
    return decorator

@app.errorhandler(400)
def not_found(error):
     return make_response(jsonify({'error': '参数不正确'}), 400)
