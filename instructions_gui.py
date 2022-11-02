from gui_base import GuiBase

intro_text = ["In this experiment, you will either hand objects to the robot or move them to another location.",
              "The instructions for each trial comes visually with that trial.",
              "Now let\'s start!\n Press Spece Key When You Are Ready"]

if __name__ == "__main__":
    gui = GuiBase(intro_text)
    gui.start()
