from psychopy import visual, core, event, monitors
from psychopy.hardware import keyboard
import os
from configs import CONFIG


class GuiBase:
    def __init__(self, intro_text):
        self.win = None
        self.clock = None
        self.kb = keyboard.Keyboard()
        self.intro_text = intro_text

    def initial_settings(self):

        # probably some monitor specs
        width_pix = 2560
        height_pix = 1440
        width_cm = 59.674
        view_dist = 50
        my_monitor = monitors.Monitor(name='ASUS_VG27AQ', width=width_cm, distance=view_dist)
        my_monitor.setSizePix((width_pix, height_pix))
        my_monitor.saveMon()

        self.win = visual.Window(
            units="pix",
            monitor=my_monitor,
            color="black",
            fullscr=True,
            allowGUI=True
        )

        self.clock = core.Clock()
        self.kb.clock.reset()

    def intro(self):

        font_file = [os.path.join(CONFIG.PATHS.STYLES, "OpenSans-Light.ttf")]
        env_img = os.path.join(CONFIG.PATHS.IMGS, "experiment_env.png")

        intro_text = visual.TextStim(
            font="Open Sans",
            fontFiles=font_file,
            alignText="center",
            win=self.win,
            units="norm"
        )

        experiment_env = visual.ImageStim(
            image=env_img,
            units="norm",
            pos=(0, -0.5),
            size=(0.4, 0.7),
            win=self.win
        )

        intro_text.color = "white"
        intro_text.size = (0.5, 0.15)
        intro_text.wrapWidth = 1.5

        # first page
        intro_text.text = self.intro_text[0]
        intro_text.draw()
        self.win.flip()
        core.wait(5)
        event.clearEvents()

        # second page
        intro_text.text = self.intro_text[1]
        intro_text.draw()
        self.win.flip()
        core.wait(4)
        event.clearEvents()

        # third page
        intro_text.text = self.intro_text[2]
        intro_text.pos = (0, 0.2)
        intro_text.draw()
        experiment_env.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        return

    def experiment_setup(self):
        pass

    def start(self):
        self.initial_settings()
        self.intro()

        return
