from psychopy import visual, core, event, monitors


class GuiBase:
    def __init__(self, intro_text):
        self.win = None
        self.clock = None
        self.intro_text = intro_text

    def initial_settings(self):
        my_monitor = monitors.Monitor(name='BMI_Lab')
        # probably some monitor specs
        my_monitor.saveMon()

        self.win = visual.Window(
            units="pix",
            monitor=my_monitor,
            color="black",
            fullscr=False,
            allowGUI=True
        )

        self.clock = core.Clock()

    def intro(self):
        intro_text = visual.TextStim(
            win=self.win,
            units="norm"
        )
        intro_text.text = self.intro_text
        intro_text.color = "white"
        intro_text.size = (0.2, 0.2)
