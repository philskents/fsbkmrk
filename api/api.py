from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Bookmarks

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://mongo/fsbkmrk'
}

initialize_db(app)

@app.route('/bookmarks')
def get_bookmarks():
    bookmarks = Bookmarks.objects().to_json()
    return Response(bookmarks, mimetype="application/json", status=200)

@app.route('/bookmarks', methods=['POST'])
def add_bookmark():
    body = request.get_json()
    bookmark = Bookmarks(**body).save()
    id = bookmark.id
    return {'id': str(id)}, 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
