
'''
from app import app


if __name__=='__main__':
    app.run()
'''

from demo import app

app.debug=True
if __name__=='__main__':
    app.run()