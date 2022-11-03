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
        env_1 = os.path.join(CONFIG.PATHS.IMGS, "env1.png")
        env_2 = os.path.join(CONFIG.PATHS.IMGS, "env2.png")
        env_3 = os.path.join(CONFIG.PATHS.IMGS, "env3.png")
        env_4 = os.path.join(CONFIG.PATHS.IMGS, "env4.png")
        hand_1 = os.path.join(CONFIG.PATHS.IMGS, "hand1.png")
        hand_2 = os.path.join(CONFIG.PATHS.IMGS, "hand2.png")
        move_1 = os.path.join(CONFIG.PATHS.IMGS, "move1.png")
        move_2 = os.path.join(CONFIG.PATHS.IMGS, "move2.png")

        intro_text = visual.TextStim(
            font="Open Sans",
            fontFiles=font_file,
            alignText="center",
            win=self.win,
            units="norm"
        )

        press_text = visual.TextStim(
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

        img1 = visual.ImageStim(
            units="norm",
            size=(0.4, 0.7),
            win=self.win
        )

        img2 = visual.ImageStim(
            units="norm",
            size=(0.4, 0.7),
            win=self.win
        )

        img3 = visual.ImageStim(
            units="norm",
            size=(0.4, 0.7),
            win=self.win
        )

        img4 = visual.ImageStim(
            units="norm",
            size=(0.4, 0.7),
            win=self.win
        )

        intro_text.color = "white"
        intro_text.size = (0.5, 0.15)
        intro_text.wrapWidth = 1.5
        intro_text.pos = (0, 0.4)

        press_text.text = "(Press Space key to continue)"
        press_text.color = "white"
        press_text.size = (0.1, 0.06)
        press_text.wrapWidth = 1.5
        press_text.pos = (0, -0.05)

        # first page
        intro_text.text = self.intro_text[0]

        intro_text.draw()
        press_text.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        # second page
        intro_text.text = self.intro_text[1]

        intro_text.draw()
        press_text.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        # third page
        intro_text.text = self.intro_text[2]

        intro_text.draw()
        press_text.draw()
        experiment_env.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        # fourth page
        img1.image = env_1
        img2.image = env_2
        img3.image = env_3
        img4.image = env_4

        img1.pos = (-0.7, -0.5)
        img2.pos = (-0.25, -0.5)
        img3.pos = (0.25, -0.5)
        img4.pos = (0.7, -0.5)

        intro_text.text = self.intro_text[3]

        intro_text.draw()
        img1.draw()
        img2.draw()
        img3.draw()
        img4.draw()
        press_text.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        # fifth page
        img2.image = move_1
        img3.image = move_2

        intro_text.text = self.intro_text[4]
        intro_text.size = (0.2, 0.1)

        intro_text.draw()
        press_text.draw()
        img2.draw()
        img3.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        # sixth page
        img2.image = hand_1
        img3.image = hand_2

        intro_text.text = self.intro_text[5]
        intro_text.size = (0.2, 0.1)

        intro_text.draw()
        press_text.draw()
        img2.draw()
        img3.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        # seventh page
        intro_text.text = self.intro_text[6]
        intro_text.size = (0.5, 0.15)

        intro_text.draw()
        press_text.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        # eighth page
        intro_text.text = self.intro_text[7]

        intro_text.draw()
        press_text.draw()
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
