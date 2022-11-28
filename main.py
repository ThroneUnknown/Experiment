import tcod

from gui import Gui
from window import Window
from engine import Engine


# Toggle between windowed and fullscreen mode
def toggle_fullscreen(context):
    if not context.sdl_window_p:
        return
    fullscreen = tcod.lib.SDL_GetWindowFlags(context.sdl_window_p) & (
        tcod.lib.SDL_WINDOW_FULLSCREEN | tcod.lib.SDL_WINDOW_FULLSCREEN_DESKTOP
    )
    tcod.lib.SDL_SetWindowFullscreen(
        context.sdl_window_p,
        0 if fullscreen else tcod.lib.SDL_WINDOW_FULLSCREEN_DESKTOP,
    )


# Main function that runs the game
def main():
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "rose.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )
    
    with tcod.context.new(
       x=0, y=25,
       tileset=tileset
    ) as context:
        
        toggle_fullscreen(context)
        console = context.new_console(magnification=0.785, order="F")

        gui = Gui(console, context)
        engine = Engine(console, context, gui)

        engine.game_loop()

if __name__ == "__main__":

    main()

