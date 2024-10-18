from rpa_common.control.control import Control


class Button (Control):
    def __init__(self, browser, locator):
        super(Button, self).__init__(browser, locator)