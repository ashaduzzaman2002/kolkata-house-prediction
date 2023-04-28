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
            'No. of Bedrooms': int(request.form.get('bhk')),
            'BED': int(request.form.get('bed')),
            'Area': float(request.form.get('area')),
        }
        
        for key in key_list:
            data[key] = int(request.form.get(key))
        return data
        # return render_template('prediction.html')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=5000)