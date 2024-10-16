from game.game_engine import GameEngine
from game.models.player import Player
from game.models.game_models import GamePhase, PlayerRole
from game.gui.debug_gui import DebugGUI

game = GameEngine()

impostor = Player("Warcin", agent="human")
impostor.set_role(PlayerRole.IMPOSTOR)

players = [Player("Wateusz", agent="ai", model_name="gpt-4o-mini"), 
            Player("Waciej", agent="ai", model_name="gpt-4o-mini"), 
            Player("Warek", agent="ai", model_name="gpt-4o-mini"), 
            Player("Wikolaj", agent="ai", model_name="gpt-4o-mini"), 
            impostor]
game.load_players(players, choose_impostor=False)
game.init_game()

game.DEBUG = True
gui = DebugGUI(game)
game.gui = gui
game.main_game_loop()
gui.run()
