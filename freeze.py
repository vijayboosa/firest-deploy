from flask_frozen import Freezer
from myapp import app

freezer = Freezer(app)

#this is my branch

if __name__ == '__main__':
    freezer.freeze()