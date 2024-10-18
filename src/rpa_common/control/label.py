from rpa_common.control.control import Control


class Label (Control):
    def __init__(self, browser, locator):
        super(Label, self).__init__(browser, locator)