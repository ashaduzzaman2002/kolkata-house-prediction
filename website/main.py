from flask import Flask, render_template, request, redirect
from utils.helper import getLocationList, yesNoParameters

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'Location_list': getLocationList(),
        'yesNoParameters': yesNoParameters()
    }
    return render_template('index.html', data= data)

@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    if request.method == 'POST':

        key_list = yesNoParameters()
        area = request.form.get('24X7Security')
        data = {
            'Location': request.form.get('location'),
            'bhk': int(request.form.get('bhk')),
            'bathrooms': int(request.form.get('bathrooms')),
            'Area': int(request.form.get('area')),
        }
        
        for key in key_list:
            if key == '24X7Security':
                data['Security'] = int(request.form.get(key))
            else:
                data[key] = int(request.form.get(key))
        return render_template('prediction.html')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=5000)