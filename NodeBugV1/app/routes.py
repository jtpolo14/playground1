from app import app
from .utils import runDiagn

@app.route('/stats')
def stats():
    res = runDiagn()
    return res

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"