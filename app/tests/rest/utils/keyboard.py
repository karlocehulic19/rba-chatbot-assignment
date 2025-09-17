class KeyboardRow:
    def __init__(self, row_number, chars):
        self.row_number = row_number
        self.chars = chars

    def get_char(self, index):
        if index < 0 or index >= len(self.chars):
            return None

        return self.chars[index]

    def get_char_index(self, char):
        return self.chars.find(char)

    def get_row_number(self):
        return self.row_number

    def get_neighbors(self, char):
        if char not in self.chars:
            return []
        index = self.get_char_index(char)
        nei = []
        if index - 1 >= 0:
            nei.append(self.chars[index - 1])

        if index + 1 < len(self.chars):
            nei.append(self.chars[index + 1])

        return nei


class Keyboard:
    def __init__(self, keyboard_chars_as_list):
        self.keys = {}
        self.row = []

        for row_i in range(len(keyboard_chars_as_list)):
            CurrKeyboardRow = KeyboardRow(row_i, keyboard_chars_as_list[row_i])
            self.row.append(CurrKeyboardRow)
            for c in keyboard_chars_as_list[row_i]:
                self.keys[c] = CurrKeyboardRow

    def get_neighbors(self, char, row_offset=None):
        if char not in self.keys:
            return []

        CharRow = self.keys[char]
        if not row_offset:
            return CharRow.get_neighbors(char) + \
                self.get_neighbors(char, 1) + self.get_neighbors(char, -1)

        char_row_index = CharRow.get_row_number()
        if char_row_index + row_offset >= len(self.row) or \
                char_row_index + row_offset < 0:
            return []

        char_index = CharRow.get_char_index(char)
        OffsetCharRow = self.row[char_row_index + row_offset]

        middle_offset_char = OffsetCharRow.get_char(char_index)
        return OffsetCharRow.get_neighbors(middle_offset_char) + \
            [middle_offset_char]


CroatianKeyboard = Keyboard([
    "1234567890'+",
    "qwertzuiopšđ",
    "asdfghjklčćž",
    "<yxcvbnm,.-",
])
