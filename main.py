from mothic import Game, flags


game = Game(
    starting_scene="GameScene",
    caption="Gradius",
    screen_size=(1920, 1080),
    display_flags=flags.SCALED | flags.FULLSCREEN
)

game.start()
