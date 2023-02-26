from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/uuid', methods=['GET'])
def generate_uuid():
    return str(uuid.uuid4())

if __name__ == '__main__':
    app.run()
