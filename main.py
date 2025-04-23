from mothic import Game, flags


game = Game(
    starting_scene="GameScene",
    caption="Gradius",
    screen_size=(854, 480),
    display_flags=flags.SCALED | flags.FULLSCREEN
)

game.start()
