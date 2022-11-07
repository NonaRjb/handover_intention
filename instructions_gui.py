from gui_base import GuiBase

intro_text = ["Hello dear participant! Welcome to our experiment!",
              "In this experiment, you will either hand objects to the robot or move them to another location.",
              "There are four available object places in front of the robot.",
              "Two of these object places (one in the left and one in the right) is occupied by objects.",
              "If the instruction is to move one of the objects, it will look like one of the images below.\n"
              "For example, if the arrow is on the left side, based on the object\'s current location, i.e., A or C, "
              "you should move it to the other location, i.e., C or A.",
              "If the instruction is to hand the object to the robot, it will look like one of the images below.\n"
              "For example, if the arrow is in the left, you pick the object from its current location (A or C), and "
              "hand it to the robot.",
              "The instructions for each trial will be visually provided to you at the beginning of that trial. "
              "Each trial's pipeline looks like this:",
              "Now let\'s start!\n Press Space Key When You Are Ready"]

if __name__ == "__main__":
    trial_sequence = [{"type": "hand", "side": "l"}]
                      # {"type": "move", "side": "l"},
                      # {"type": "hand", "side": "r"},
                      # {"type": "move", "side": "r"}]
    gui = GuiBase(intro_text)
    gui.start(trial_sequence)
