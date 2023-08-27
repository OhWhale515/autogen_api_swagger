from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


data = []

@app.route('/api/data', methods=['GET'])
def get_data():
    """
    Get data with optional filtering.
    ---
    parameters:
      - in: query
        name: filter
        type: string
        description: Filter data based on a criterion
    responses:
      200:
        description: Successful response
    """
    filter_value = request.args.get('filter')
    if filter_value:
        filtered_data = [item for item in data if filter_value in item]
        return jsonify(filtered_data)
    else:
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
          properties:
            key1:
              type: string
              example: value1
            key2:
              type: integer
              example: 42
          examples:
            example1:
              value:
                key1: example_value1
                key2: 99
            example2:
              value:
                key1: another_example
                key2: 123
    responses:
      200:
        description: Data added successfully
    """
    new_item = request.json
    data.append(new_item)
    return jsonify({"message": "Data added successfully"})

if __name__ == '__main__':
    app.run(debug=True)
