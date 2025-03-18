from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'galery_mars/static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def gallery():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('gallery'))

    standard_images = [
        'mars1.jpg',
        'mars2.jpg',
        'mars3.jpg'
    ]
    
    uploaded_images = os.listdir(app.config['UPLOAD_FOLDER'])
    
    images = standard_images + uploaded_images
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)