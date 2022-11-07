from psychopy import visual, core, event, monitors
from psychopy.hardware import keyboard
import os
from configs import CONFIG


class GuiBase:
    def __init__(self, intro_text):
        self.win = None
        self.clock = None
        self.marker = None
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

        rx = 0.04
        rpix = rx * width_pix
        ry = rpix / height_pix

        self.marker = visual.Circle(
            win=self.win,
            units="norm",
            radius=(rx, ry),
            pos=(-0.96, -0.94),
            fillColor='white',
            lineColor='white'
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
        hand_1 = os.path.join(CONFIG.PATHS.IMGS, "hand_l.png")
        hand_2 = os.path.join(CONFIG.PATHS.IMGS, "hand_r.png")
        move_1 = os.path.join(CONFIG.PATHS.IMGS, "move_l.png")
        move_2 = os.path.join(CONFIG.PATHS.IMGS, "move_r.png")
        pipeline = os.path.join(CONFIG.PATHS.IMGS, "pipeline.png")

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
        intro_text.size = (0.2, 0.1)
        intro_text.wrapWidth = 1.5
        intro_text.pos = (0, 0.3)

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
        intro_text.pos = (0, 0.4)

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
        intro_text.pos = (0, 0.4)

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
        intro_text.size = (0.2, 0.1)
        intro_text.pos = (0, 0.3)

        experiment_env.image = pipeline
        experiment_env.size = (1.3, 0.8)
        experiment_env.pos = (-0.02, -0.55)

        intro_text.draw()
        experiment_env.draw()
        press_text.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        # eighth page
        intro_text.text = self.intro_text[7]
        intro_text.size = (0.2, 0.1)

        intro_text.draw()
        press_text.draw()
        self.win.flip()
        key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
        if "space" in key:
            event.clearEvents()

        return

    def trial_manager(self, trial_sequence):
        instruction_images = [os.path.join(CONFIG.PATHS.IMGS, "hand_l.png"),
                              os.path.join(CONFIG.PATHS.IMGS, "hand_r.png"),
                              os.path.join(CONFIG.PATHS.IMGS, "move_l.png"),
                              os.path.join(CONFIG.PATHS.IMGS, "move_r.png")]
        for trial in trial_sequence:
            if trial["type"] == "hand" and trial["side"] == "l":
                self.trial(instruction_images[0])
            if trial["type"] == "hand" and trial["side"] == "r":
                self.trial(instruction_images[1])
            if trial["type"] == "move" and trial["side"] == "l":
                self.trial(instruction_images[2])
            if trial["type"] == "move" and trial["side"] == "r":
                self.trial(instruction_images[3])

    def trial(self, env_img):

        w_cross = os.path.join(CONFIG.PATHS.IMGS, "white_cross.png")
        r_cross = os.path.join(CONFIG.PATHS.IMGS, "red_cross.png")
        g_cross = os.path.join(CONFIG.PATHS.IMGS, "green_cross.png")
        font_file = [os.path.join(CONFIG.PATHS.STYLES, "OpenSans-Light.ttf")]

        press_text = visual.TextStim(
            font="Open Sans",
            fontFiles=font_file,
            alignText="center",
            pos=(0, -0.3),
            color="white",
            win=self.win,
            units="norm"
        )

        press_text.text = "(Press Space key to continue)"
        press_text.size = (0.1, 0.06)
        press_text.wrapWidth = 1.5

        count_down = visual.TextStim(
            font="Open Sans",
            fontFiles=font_file,
            alignText="center",
            pos=(0, -0.1),
            bold=True,
            color="yellow",
            win=self.win,
            units="norm"
        )
        count_down.size = (0.5, 0.3)
        count_down.wrapWidth = 2
        cnt_down = 3

        # Instruction
        instruction_img = visual.ImageStim(
            image=env_img,
            units="norm",
            size=(0.5, 0.9),
            pos=(0, 0.1),
            win=self.win
        )

        instruction_img.draw()
        self.marker.draw()
        self.win.flip()
        core.wait(CONFIG.CONSTANTS.INS_DUR-cnt_down)
        event.clearEvents()
        while cnt_down > 0:
            count_down.text = str(cnt_down)
            instruction_img.draw()
            count_down.draw()
            self.marker.draw()
            self.win.flip()
            core.wait(1)
            event.clearEvents()
            cnt_down -= 1

        event.clearEvents()
        self.win.flip()

        # Preparation
        instruction_img.image = w_cross
        instruction_img.size = (0.2, 0.36)
        instruction_img.draw()
        self.marker.draw()
        self.win.flip()
        core.wait(CONFIG.CONSTANTS.PREP_DUR)
        event.clearEvents()

        event.clearEvents()
        self.win.flip()

        # Execution
        instruction_img.image = r_cross
        instruction_img.size = (0.2, 0.36)
        instruction_img.draw()
        self.marker.draw()
        self.win.flip()
        core.wait(CONFIG.CONSTANTS.EXEC_DUR)
        event.clearEvents()

        event.clearEvents()
        self.win.flip()

        # Rest
        instruction_img.image = g_cross
        instruction_img.size = (0.2, 0.36)
        instruction_img.draw()
        self.marker.draw()
        if CONFIG.CONSTANTS.REST_DUR == "inf":
            press_text.draw()
            self.win.flip()
            key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
            if "space" in key:
                event.clearEvents()
        else:
            self.win.flip()
            core.wait(CONFIG.CONSTANTS.PREP_DUR)
            event.clearEvents()

    def start(self, trial_sequence):
        self.initial_settings()
        self.intro()
        self.trial_manager(trial_sequence)
        return
