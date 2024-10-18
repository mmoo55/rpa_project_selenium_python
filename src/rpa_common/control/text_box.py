from rpa_common.control.control import Control


class TextBox (Control):
    def __init__(self, browser, locator):
        super(TextBox, self).__init__(browser, locator)

    def set_text(self, value):
        self.find_element()
        self.control.send_keys(value)