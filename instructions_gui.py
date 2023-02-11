from gui_base import GuiBase
import json
import pickle

intro_text = ["Hello! Welcome to Our Experiment!\n Press Space Key When You Are Ready to Start"]

if __name__ == "__main__":
    data_file = "trials.txt"


    def parse(d):
        dictionary = dict()
        # Removes curly braces and splits the pairs into a list
        pairs = d.strip('{}').split(', ')
        for i in pairs:
            pair = i.split(': ')
            # Other symbols from the key-value pair should be stripped.
            dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
        return dictionary


    try:
        data_file = open(data_file, 'rt')
        lines = data_file.read().split('\n')
        trial_sequence = []
        for l in lines:
            if l != '':
                dictionary = parse(l)
                trial_sequence.append(dictionary)
        data_file.close()
        # trial_sequence = [{"type": "hand"},
        #                   {"type": "solo"},
        #                   {"type": "joint"}]
        gui = GuiBase(intro_text)
        gui.start(trial_sequence)
    except Exception as e:
        print("Something unexpected occurred!")
        print(e)

    # trial_sequence = [{"type": "hand", "side": "l"},
    # {"type": "move", "side": "l"},
    # {"type": "hand", "side": "r"},
    # {"type": "move", "side": "r"}]
