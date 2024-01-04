from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'{self.name} - {self.country} - {self.position}'

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/players')
def get_players():
    players = Player.query.all()
    output = []
    for player in players:
        player_data = {'name': player.name, 'country': player.country, 'position': player.position}
        output.append(player_data)
    return {'players': output}

@app.route('/players/<id>')
def get_player(id):
    player = Player.query.get_or_404(id)
    return {'name': player.name, 'country': player.country, 'position': player.position}
   