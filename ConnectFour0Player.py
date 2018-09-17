import ConnectFourRandomAI
import ConnectFourMinimaxAI
import AlphaBetaAI
import ConnectFourEngine

if __name__ == '__main__':
    # Initialise the game engine
    for i in range(4):
        app = ConnectFourEngine.ConnectFour(
                ai_delay = 0,
                red_player = AlphaBetaAI.AIcheck,
                blue_player = AlphaBetaAI.AIcheck,
                )
        # start the game engines
        app.game_loop()