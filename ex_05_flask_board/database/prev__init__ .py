from __main__ import app
from flask_sqlalchemy import SQLAlchemy

__all__ = ['Base', 'session']

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/kimyongseon'
DATABASES = SQLAlchemy(app)

Base = DATABASES.Model

session = DATABASES.session