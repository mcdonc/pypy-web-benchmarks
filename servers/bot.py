import sys
from bottle import run
import bottle
import redis

app = bottle.Bottle()

redisdb = redis.ConnectionPool(host='localhost')

if len(sys.argv) < 2:
    server = 'tornado'
else:
    server = sys.argv[1]


@app.route('/')
def stream():
    db = redis.Redis(connection_pool=redisdb)
    x = db.incr('counter')
    p = db.get('page')
    yield 'hello world! %s\n' % x
    yield p

run(app, host='0.0.0.0', port=8000, server=server, quiet=True)


