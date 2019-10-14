from flask import Flask
from flask import request
from flask import *
from image_creator import create_image

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def generate_image():
    if request.method == 'POST':

        result = request.form['string']

        path = create_image(result)

        return render_template('result.html', result=result, image_path=path)
    else:
        return render_template('initial.html')

if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)