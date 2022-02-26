from flask import Flask, jsonify, request
from http import HTTPStatus


app=Flask(__name__)

recipes=[
    {
        'id':1,
        'name':'jeden'
    },
    {
        'id':2,
        'name':'dwa'
    }
]


@app.route('/recipes',methods=['GET'])
def get_recipes():
    return jsonify({'data':recipes})


if __name__=='__main__':
    app.run()