import uuid
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='Tic Tac Toe API',
          description='Tic Tac Toe Game API')

# Namespaces
game_ns = Namespace('game', description='game operations')

api.add_namespace(game_ns)

# In-memory data storage
active_games = []


'''
Game Namespace
'''

@game_ns.route('/')
class Games(Resource):
    @game_ns.doc('games')
    def get(self):
        """List all active games"""
        return active_games
    
@game_ns.route('/newGame')
class NewGame(Resource):
    @game_ns.doc('newGame')
    def post(self):
        """Create a new game"""
        last_idx = active_games[-1]['id'] if len(active_games) > 0 else -1
        new_game = {'id': last_idx + 1, 'board': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]}

        active_games.append(new_game)
        return new_game



if __name__ == '__main__':
    app.run(debug=True)
