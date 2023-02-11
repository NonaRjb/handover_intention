from psychopy import visual, core, event, monitors
from psychopy.hardware import keyboard
import os
from configs import CONFIG
from sys import exit


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

        return

    def trial_manager(self, trial_sequence):
        instruction_images = [os.path.join(CONFIG.PATHS.IMGS, "handover.png"),
                              os.path.join(CONFIG.PATHS.IMGS, "joint.png"),
                              os.path.join(CONFIG.PATHS.IMGS, "solo.png")]

        cnt = 1
        for trial in trial_sequence:
            if trial["type"] == "hand":
                self.trial(instruction_images[0], cnt)
            if trial["type"] == "joint":
                self.trial(instruction_images[1], cnt)
            if trial["type"] == "solo":
                self.trial(instruction_images[2], cnt)
            if cnt == CONFIG.CONSTANTS.BREAK:
                cnt = 1
            else:
                cnt += 1
        exit(0)

    def trial(self, env_img, cnt, press_text=None):

        r_cross = os.path.join(CONFIG.PATHS.IMGS, "red_cross.png")
        g_cross = os.path.join(CONFIG.PATHS.IMGS, "green_cross.png")
        font_file = [os.path.join(CONFIG.PATHS.STYLES, "OpenSans-Light.ttf")]

        break_text = visual.TextStim(
            font="Open Sans",
            fontFiles=font_file,
            alignText="center",
            pos=(0, -0.5),
            color="white",
            win=self.win,
            units="norm"
        )

        break_text.text = "Good Job! You Can Now Have a Longer Break (~5 mins)!"
        break_text.size = (0.1, 0.06)
        break_text.wrapWidth = 1.5

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
            pos=(0.005, 0.33),
            bold=True,
            color="Black",
            win=self.win,
            units="norm"
        )
        count_down.size = (0.28, 0.18)
        count_down.wrapWidth = 2
        cnt_down = CONFIG.CONSTANTS.INS_DUR

        trial_count = visual.TextStim(
            font="Open Sans",
            fontFiles=font_file,
            alignText="center",
            pos=(0.0, -0.55),
            bold=True,
            color="white",
            win=self.win,
            units="norm"
        )
        trial_count.size = (0.15, 0.1)
        trial_count.wrapWidth = 1
        trial_count.text = f"{cnt}/{CONFIG.CONSTANTS.BREAK}"

        event.clearEvents()
        core.wait(CONFIG.CONSTANTS.MARKER_DUR)
        self.win.flip()

        # Instruction
        instruction_img = visual.ImageStim(
            image=env_img,
            units="norm",
            size=(0.37, 0.95),
            pos=(0.0, 0.03),
            win=self.win
        )

        # instruction_img.draw()
        self.marker.draw()
        # self.win.flip()
        # core.wait(CONFIG.CONSTANTS.INS_DUR - cnt_down)
        # event.clearEvents()
        self.win.flip()
        core.wait(CONFIG.CONSTANTS.MARKER_DUR)
        event.clearEvents()
        # self.win.flip()

        while cnt_down > 0:
            count_down.text = str(cnt_down)
            instruction_img.draw()
            count_down.draw()
            trial_count.draw()
            self.marker.draw()
            self.win.flip()
            core.wait(1)
            event.clearEvents()
            cnt_down -= 1

        event.clearEvents()
        core.wait(CONFIG.CONSTANTS.MARKER_DUR)
        self.win.flip()

        instruction_img.pos = (0.0, 0.0)

        # Execution
        instruction_img.image = g_cross
        instruction_img.size = (0.2, 0.43)
        instruction_img.draw()
        # press_text.draw()
        self.marker.draw()
        self.win.flip()
        core.wait(CONFIG.CONSTANTS.EXEC_DUR)
        # key = self.kb.waitKeys(maxWait=CONFIG.CONSTANTS.EXEC_DUR, keyList=['space'], waitRelease=True)
        event.clearEvents()

        event.clearEvents()
        core.wait(CONFIG.CONSTANTS.MARKER_DUR)
        self.win.flip()

        # Rest
        instruction_img.image = r_cross
        instruction_img.size = (0.2, 0.43)
        instruction_img.draw()
        self.marker.draw()
        if CONFIG.CONSTANTS.REST_DUR == "inf":
            if cnt == CONFIG.CONSTANTS.BREAK:
                break_text.draw()
            press_text.draw()
            self.win.flip()
            key = self.kb.waitKeys(keyList=['space'], waitRelease=True)
            if "space" in key:
                event.clearEvents()
        else:
            if cnt == CONFIG.CONSTANTS.BREAK:
                break_text.draw()
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
