import pickle
import numpy as np

from flask import Flask, render_template, request, jsonify

point_list = pickle.load(open('pickled_point_list.pkl', 'rb'))
color_list = pickle.load(open('color_list_pickle.pkl', 'rb'))
n=10000
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
        return render_template("index.html",hell=color_list[2])


if __name__ == '__main__':
    app.run()

@app.route('/android_predict', methods=['GET'])
def android_predict():
    # req_json = request.json
    # print("Values that were posted :\n", req_json)
    points=np.array(point_list)
    colors=np.array(color_list)
    return jsonify(
        {
            "location":points.tolist()[0:n],
            "colors":colors.tolist()[0:n]
        })

def get(key): return request.form.get(key, 0)
