from core import create_app
from env import APP_HOST, APP_PORT, APP_DEBUG

app = create_app()

if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG)