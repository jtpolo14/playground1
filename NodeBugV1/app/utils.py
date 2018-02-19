import json
from datetime import datetime as dt
from pymongo import MongoClient
import psutil
import socket
from uuid import uuid4

uid = uuid4().hex

def getIP():
    return [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

def runDiagn():
    rc = 0
    results = {"tstamp":dt.utcnow().isoformat()}

    results["uid"] = getIP() + uid
    results["cpu_percent"] = psutil.cpu_percent()
    results["virtual_memory"] = psutil.virtual_memory()

    return json.dumps({
        "rc" : rc,
        "results": results,
        })
