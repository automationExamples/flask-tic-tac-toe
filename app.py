import uuid
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='Tic Tac Toe API',
          description='Tic Tac Toe Game API')

# Namespaces
game_ns = Namespace('game', description='game operations')
player_ns = Namespace('player', description='player operations')

api.add_namespace(game_ns)
api.add_namespace(player_ns)

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
    
@game_ns.route('/new_game')
class NewGame(Resource):
    @game_ns.doc('new_game')
    def post(self):
        """Create a new game"""
        last_idx = active_games[-1]['id'] if len(active_games) > 0 else -1
        new_game = get_new_board(last_idx + 1)

        active_games.append(new_game)
        return new_game
    
@game_ns.route('/remove_game/<int:game_id>')
@game_ns.response(404, 'Game not found')
@game_ns.param('game_id', 'Game id to delete')
class NewGame(Resource):
    @game_ns.doc('removeGame')
    def delete(self, game_id):
        """Remove a game"""
        for index, game in enumerate(active_games):
            if game['id'] == game_id:
                active_games.pop(index)
                return {"message": f"Game with id {game_id} deleted"}
        api.abort(404, f"Game with ID {game_id} not found")



def get_new_board(id):
    return {'id': id, 'board': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]}

if __name__ == '__main__':
    app.run(debug=True)
