from flask import Flask, render_template

app = Flask(__name__)

@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        title = "Инженерные тренажеры"
        image_url = "flask_wtf/mars3.jpg" 
    else:
        title = "Научные симуляторы"
        image_url = "flask_wtf/mars1.jpg"  

    return render_template('training.html', title=title, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
