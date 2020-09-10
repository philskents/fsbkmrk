from flask import Flask, jsonify
app = Flask(__name__)

bookmarks = [
    {
        "title":"My Blog",
        "url":"https://strangeadventures.in",
        "tags":["blog"]
    },
    {
        "title":"Splunk",
        "url":"https://splunk.com",
        "tags":["vendor"]
    }
]

@app.route('/bookmarks')
def get_bookmarks():
    return jsonify(bookmarks)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
