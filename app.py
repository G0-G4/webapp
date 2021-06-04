from logging import INFO
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cnhf[e,bdftnhfpev010730@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# engine = create_engine('mysql+pymysql://root:cnhf[e,bdftnhfpev010730@localhost/test')


db = SQLAlchemy(app)

class Info(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    device_id = db.Column(db.Integer, nullable = False)
    x = db.Column(db.Float, nullable = False)
    y = db.Column(db.Float, nullable = False)
    tempreture = db.Column(db.Float, nullable = False)
    date = db.Column(db.DateTime, nullable = False)

    def __repr__(self):
        #return "<inf %>" % self.id
        return f"<inf {self.id}>"


@app.route("/")
def index():
    infos = Info.query.order_by(Info.date).all()
    return render_template("index.html", infos=infos)

@app.route("/post", methods = ["POST", "GET"])
def pst():
    if request.method == "POST":
        device_id = request.form['device_id']
        x = request.form['x']
        y = request.form['y']
        tempreture = request.form['tempreture']
        date = request.form['date']
        new_info = Info(
            device_id=device_id,
            x=x,
            y=y,
            tempreture=tempreture,
            date=date)
        try:
            db.session.add(new_info)
            db.session.commit()
            return redirect('/')
        except:
            return 'there was an issue adding info'

    else:
        infos = Info.query.order_by(Info.date).all()
        return render_template("pst.html")


@app.route("/device/<int:device_id>")
def devid(device_id):
    data = Info.query.filter_by(device_id = device_id).order_by(Info.date)
    dates = []
    tempretures = []
    x = []
    y = []
    for d in data:
        dates.append(str(d.date))
        tempretures.append(d.tempreture)
        x.append(d.x)
        y.append(d.y)
    return render_template("device.html", device_id=device_id, dates = dates,
    tempretures = tempretures, x=x, y=y)


@app.route('/myview/<int:page>',methods=['GET'])
def view(page=1):
    per_page = 10
    infos = Info.query.order_by(Info.date).paginate(page,per_page,error_out=False)
    return render_template('view.html',infos=infos)


@app.route('/graph')
def graph():
    data = Info.query.filter_by(device_id = 1).order_by(Info.date)
    dates = []
    tempretures = []
    x = []
    y = []
    for d in data:
        dates.append(str(d.date))
        tempretures.append(d.tempreture)
        x.append(d.x)
        y.append(d.y)
    return render_template('graph.html', dates = dates, tempretures = tempretures, x=x, y=y)
    



if __name__ == "__main__":
    app.run(debug=True)
