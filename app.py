from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

def track_visits(page):
    redis.incr(f'{page}_visits')

@app.route('/')
def index():
    track_visits('index')
    visits = redis.get('index_visits').decode('utf-8')
    return f"This webpage has been visited {visits} times."

@app.route('/products')
def products():
    track_visits('products')
    visits = redis.get('products_visits').decode('utf-8')
    return f"This is the products page. It has been visited {visits} times."

@app.route('/users')
def users():
    track_visits('users')
    visits = redis.get('users_visits').decode('utf-8')
    return f"This is the users page. It has been visited {visits} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

