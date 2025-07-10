#!/usr/bin/env python3
import tcod

#
# Princess Molly's Adventure
#
# Princess Molly lives in a small village at the edge of a dark forest.
# One day, she decides to explore the forest and find out what lies beyond the trees.
# She packs her bag with some food, a map, and a flashlight, and sets off on her adventure.
# After walking for a while, she comes across a small clearing with a pond in the center.
# She sits down by the pond and takes out her map to see where she is when she hears a rustling in the bushes.
# She turns around and sees a small creature peeking out at her. It's a rabbit! but not just any rabbit, it's a magical rabbit that can talk!
# The rabbit introduces himself as Mr. Fluff and tells Molly that he has been waiting for her.
# It was such a shock to Molly she fell backwards into the pond!
# Down she went, into the water, down and down, until she fell into an underwater cave.
# Now Molly must find her way out of the cave and back to the surface... the adventure has just begun!

def main() -> None:
    # Set the screen dimensions.
    screen_width = int(80/2)
    screen_height = int(50/2)

    # Set the initial player position.
    player_x = int(screen_width / 2) # cast to int to ensure it's an integer
    player_y = int(screen_height / 2)

    # the number of columns and rows of tiles in the image
    # https://dwarffortresswiki.org/index.php/Tileset_repository
    tileset = tcod.tileset.load_tilesheet(
        #"rltiles-2d.png", 30, 54, tcod.tileset.CHARMAP_TCOD
        #"dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
        "Cooz_curses_square_16x16.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    # Create a new context with the specified screen dimensions and tileset.
    with  tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Princess Molly's Adventure",
        vsync=True,
    ) as context:
        # This creates our “console” which is what we’ll be drawing to.
        # The `order="F"` argument specifies that the console should be in Fortran-style order [x,y] rather than C-style order [y,x].
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        # The main game loop.
        # This loop will run until the user quits the game.
        while True:
            # Clear the console to black and put the cursor at the top left corner displaying the string "@".
            root_console.print(x=player_x , y=player_y, string="@")

            # Render the console to the context. Will display the console on the screen.
            context.present(root_console)

            # Handle events such as quitting the game.
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()

if __name__ == "__main__":
    main()