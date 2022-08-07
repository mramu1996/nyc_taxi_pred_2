import pickle

from flask import Flask, render_template, request, jsonify

# model = pickle.load(open('model.pkl', 'rb'))
point_list = pickle.load(open('pickled_point_list.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    print(point_list)
    # nl=point_list.split('\n')

    return render_template("index.html",hell=point_list[99999])


if __name__ == '__main__':
    app.run()

# @app.route('/predict', methods=['POST'])
# def predict():
#     test_array = list(request.form.values())
#     print("values received are - ", test_array)
#     last = test_array[len(test_array) - 1]
#     if last == 'Submit': test_array.pop()
#     # TODO

@app.route('/android_predict', methods=['GET'])
def android_predict():
    # req_json = request.json
    # print("Values that were posted :\n", req_json)
    return jsonify({"Prediction": str(point_list)})

def get(key): return request.form.get(key, 0)
