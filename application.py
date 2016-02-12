import os
from app import create_app

value = os.getenv('DEPLOY_TYPE', 'default')
app = create_app(value)

if __name__ == '__main__':
    app.run()
