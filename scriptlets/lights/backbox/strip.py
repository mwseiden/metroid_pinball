from mpf.core.rgb_color import RGBColor

class Strip:
    def __init__(self, machine, offset, size, forward):
        self.machine = machine
        self.offset = offset
        self.size = size
        self.forward = forward
        self._lights = list(range(offset, offset + size) if forward else range(offset + size - 1, offset - 1, -1))
        self._initialize_state()

    def get_led(self, index):
        return None if self._index_out_of_range(index) else _get_led(index)

    def set_color(self, index, color):
        if self._index_out_of_range(index):
            return None

        self._set_color(index, color)

    def set_color_with_invert(self, index, color, invert):

        if invert:
            index = 10 - index

        if self._index_out_of_range(index):
            return None

        self._set_color(index, color)


    def get_color(self, index):
        if self._index_out_of_range(index):
            return None

        return self._get_color(index)

    def set_all_colors(self, color):
        for index in range(self.size):
            self._set_color(index, color)

    def save_state(self):
        self._state = [None] * self.size
        for index in range(self.size):
            self._state[index] = self._get_color(index)

    def restore_state(self):
        for index in range(self.size):
             self._set_color(index, self._state[index])

    # private ----------------------------------------------------------------

    def _index_out_of_range(self, index):
        return index < 0 or index >= self.size

    def _get_led(self, index):
        return self.machine.lights[self._get_light_key(self._lights[index])]

    def _set_color(self, index, color):
        self._get_led(index).color(color, None, 50000, 'bb')

    def _get_color(self, index):
        return self._get_led(index).get_color()

    def _get_light_key(self, index):
        return 'led{:02X}'.format(index)

    def _initialize_state(self):
        self._state = [RGBColor('off')] * self.size