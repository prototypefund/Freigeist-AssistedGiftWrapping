#TODO: real number depending on rotary encoder
amount_of_steps_per_cm = 10


class PaperLengthWatcher():

    def __init__(self, on_paper_pushed_out):
        self.on_paper_pushed_out = on_paper_pushed_out
        self.reset()

    def set_paper_dimensions(self, width, length):
        self.paper_width = width
        #TODO: define max_paper_length differently
        self.min_paper_length = length
        self.max_paper_length = length + 20
        print("paper length should be in range " + str(self.min_paper_length) + " " + str(self.max_paper_length))
        self.active = True
        # TODO: turn led on

    # TODO: needs to be called when the user cut off the paper (probably noticed by button press)
    def reset(self):
        self.active = False
        self.pushed_out = False
        self.paper_width = -1
        self.min_paper_length = -1
        self.max_paper_length = -1
        self.current_paper_length = -1
        # TODO: turn led off

    def finish(self):
        if self.active:
            self.on_paper_pushed_out(self.current_paper_length)
            self.reset()

    def new_encoder_value(self, value):
        length = value / amount_of_steps_per_cm
        if self.active:
            self.current_paper_length = length
            if self.min_paper_length <= length <= self.max_paper_length:
                print("pushed out far enough")
                # self.on_paper_pushed_out()
                # TODO: led green
            else:
                print("not in range")
                # TODO: led red
