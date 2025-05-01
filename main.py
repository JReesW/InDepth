from mothic import Game, flags


game = Game(
    starting_scene="IntroScene",
    caption="InDepth",
    screen_size=(1920, 1080),
    display_flags=flags.SCALED | flags.FULLSCREEN
)


game.start()
