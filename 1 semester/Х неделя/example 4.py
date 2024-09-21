class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keyword):
        self.alphaindex = {self.alphabet[index]: index for index in range(len(self.alphabet))}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def caesar(self, letter, shift):
        if letter in self.alphaindex:
            index = (self.alphaindex[letter] + shift) % len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter

    def encode(self, line, key = None):
        if not key:
            key = self.key
        ciphertext = []
        i = 0
        for letter in line:
            shift = key[i]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter) # была проблема в том, что код после каждого постороннего знака делал шаг
            if cipherletter in self.alphabet: # я немного исправил код, теперь он переводит верно (онлайн калькуляторы зло)
                i = (i + 1) % 4
        return ''.join(ciphertext)

    def decode(self, line):
        keyword = [len(self.alphabet) - shift for shift in self.key]
        return self.encode(line, keyword)

keyword = "мфти"
cipher = Vigenere(keyword)
line = input()

#кодировка
'''while line:
    print(cipher.encode(line))
    line = input()'''

#расшифровка
while line:
    print(cipher.decode(line))
    line = input()