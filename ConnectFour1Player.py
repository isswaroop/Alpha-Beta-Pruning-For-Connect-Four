import ConnectFourRandomAI
import ConnectFourMinimaxAI
import AlphaBetaAI

import ConnectFourEngine

if __name__ == '__main__':
    # Initialise the game engine
    # Modify these parameters to tweak the game
    app = ConnectFourEngine.ConnectFour(
            ai_delay = 20,
            #red_player = ConnectFourMinimaxAI.AIcheck, #None,
            blue_player = AlphaBetaAI.AIcheck #ConnectFourMinimaxAI.AIcheck , 

            )
    # start the game engine
    app.game_loop()
