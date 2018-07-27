import os
import sys

path = '/app/bungkerdream'
if path not in sys.path:
    sys.path.append(path)

os.environ['FLASK_CONFIG'] = 'production'
os.environ['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql://dt_admin:dt2016@localhost/dreamteam_db'

from run import app as application
