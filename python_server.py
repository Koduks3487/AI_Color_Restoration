from urllib import request
from flask import Flask, request

from flask_restx import Resource, Api
from werkzeug.utils import secure_filename

app = Flask(__name__)
api = Api(app)

@api.route('/upload')
class uploadging(Resource):
    def post(self):
        f = request.files['image']
        f.save(secure_filename(str(f.filename)))
        return {"isUploadSuccess" : "success"}

if __name__ == "__main__":
    app.run(debug=True, host='165.229.229.173', port=5000)