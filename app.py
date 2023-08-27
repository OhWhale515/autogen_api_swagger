from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Sample data to store information
data = []

@app.route('/api/data', methods=['GET'])
def get_data():
    """
    Get all data.
    ---
    responses:
      200:
        description: Successful response
    """
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
    """
    Add new data.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Successful response
    """
    new_item = request.json
    data.append(new_item)
    return jsonify({"message": "Data added successfully"})

if __name__ == '__main__':
    app.run(debug=True)
