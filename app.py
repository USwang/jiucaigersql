from flask import Flask
from exts import db
import config
from flask_migrate import Migrate
from models import Stockdata
from apps.front import front_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)


# 注册蓝图
app.register_blueprint(front_bp)

@app.route('/')
def index():  # put application's code here
    return '/getdata/'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
