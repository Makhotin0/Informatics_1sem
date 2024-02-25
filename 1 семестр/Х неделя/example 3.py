import random
class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" # TODO

    def __init__(self, keytable):
        lowercase_encode = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_encode = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_encode
        self._encode.update(uppercase_encode)
        lowercase_decode = {x: y for x, y in zip(keytable, self.alphabet)}
        uppercase_decode = {x.upper(): y.upper() for x, y in zip(keytable, self.alphabet)}
        self._decode = lowercase_decode
        self._decode.update(uppercase_decode)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])

keytable = "эьормщднйгычясюцажшбтпвёлеъ+зхкфи"
cipher = Monoalphabet(keytable)
line = input()

#кодировка
'''while line:
    print(cipher.encode(line))
    line = input()'''

#расшифровка
while line:
    print(cipher.decode(line))
    line = input()