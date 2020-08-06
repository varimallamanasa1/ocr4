import numpy as np
from flask import Flask, request, jsonify, render_template
import os
import cv2
import pytesseract
import base64
from pytesseract import Output

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")

def start_page():
    print("Start")
    return render_template('index.html')

@app.route('/upload', methods=['POST'])

def upload_file():
    file = request.files['image']
    option = request.form['budget']
    Save file
    filename = 'static/' + file.filename
    file.save(filename)
    #Read image
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    result = read_img(image)
    
    if(len(result) == 0): 
        textDetected = False
        print ("Empty String") 
        result = "String Have nothing"
        to_send = ''
    else : 
        textDetected = True
        print ("String Have something")
        
        d = pytesseract.image_to_data(image, output_type=Output.DICT)
        image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        n_boxes = len(d['text'])
        for i in range(n_boxes):
            if int(d['conf'][i]) > 60:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        image_content = cv2.imencode('.jpg', image)[1].tostring()
        encoded_image = base64.encodestring(image_content)
        to_send = 'data:image/jpg;base64, ' + str(encoded_image, 'utf-8')
    return render_template('index.html', textDetected=textDetected, prediction_text=result,image_to_show=to_send, init=True)

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)
     
def read_img(img):
    text = pytesseract.image_to_string(img)
    return(text)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
