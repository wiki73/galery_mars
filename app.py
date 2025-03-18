from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def gallery():
    # Список изображений для галереи
    images = [
        'img/mars1.jpg',
        'img/mars2.jpg',
        'img/mars3.jpg'
    ]
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)