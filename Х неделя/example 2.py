class Caesar:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter1 = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter1] = encoded
            self._encode[letter1.upper()] = encoded.upper()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter2 = self.alphabet[i]
            decoded = self.alphabet[(i + (33 - key)) % len(self.alphabet)]
            self._decode[letter2] = decoded
            self._decode[letter2.upper()] = decoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])

key = 19
cipher = Caesar(key)
line = input()

#кодировка
'''while line:
    print(cipher.encode(line))
    line = input()'''

#расшифровка
while line:
    print(cipher.decode(line))
    line = input()