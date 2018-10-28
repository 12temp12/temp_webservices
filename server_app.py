# -*- coding: utf-8 -*-

from flask import Flask, request
from flask import jsonify, abort, make_response

app = Flask(__name__)

data =[
        {"id":1,
         "name":"jaydeep",
         "designation":"CEO"},
        {"id":2,
         "name":"jhon",
         "designation":"CFO"},
        ]

@app.route('/company-data/api/v1.0/data',methods=["GET"])
def get_data():
    return jsonify({'data':data})

@app.route('/company-data/api/v1.0/data/<int:mem_id>', methods=["GET"])
def get_specific(mem_id):
    info = [info for info in data if info["id"]==mem_id]
    if len(info)==0:
        abort(404)
    return jsonify({"data":info})


@app.route('/company-data/api/v1.0/data', methods=["POST"])
def create_data():
    
    if not request.json or not 'name' in request.json:
        abort(400)
    info = {'id':data[-1]["id"]+1,
            "name":request.json['name'],
            "designation":request.json.get('designation',""),
            }
    data.append(info)
    
    return jsonify({"data":data}),201



@app.route('/company-data/api/v1.0/data/update/<int:mem_id>', methods=["PUT"])
def update_data(mem_id):
    info = [info for info in data if info['id'] == mem_id]
    if len(info) == 0:
        abort(404)
    if not request.json:
        abort(400)
    data.remove(info[0])
    info[0]['name'] = request.json.get('name', info[0]['name'])
    info[0]['designation'] = request.json.get('designation', info[0]['designation'])
    
    data.append(info[0])
    return jsonify({'data': data}), 201

@app.route('/company-data/api/v1.0/data/<int:mem_id>', methods=['DELETE'])
def delete_task(mem_id):
    info = [info for info in data if info['id'] == mem_id]
    if len(info) == 0:
        abort(404)
    data.remove(info[0])
    return jsonify({'result': True})






@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'resource not found'}), 404)
if __name__ == "__main__":
    app.run(debug=True)
