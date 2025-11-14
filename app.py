from flask import Flask,request,jsonify
app=Flask(__name__)
data=[{'id':100,'name':'joe'
},
{
    'id':200,
    'name':'mic'
}]
@app.route("/")
def get():
    return jsonify(data),200


if __name__=='__main__':
    app.run()