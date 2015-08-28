import sys
class PHPGoAway:
    vdict = {}
    key = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz!'

    def __init__(self):
        pass

    def setKey(self, keyword):

        l = len(self.alphabet)
        keyword = keyword.lower()

        self.key = keyword
        
        for k in keyword:
            if not k in self.alphabet: continue
            if k not in self.vdict:
                i = self.alphabet.find(k)
                self.vdict[k] = [self.alphabet[(l+i+j) % l] for j in range(l)]

    def forLove(self, message):
        message = message.lower()
        s = ''
        mykey = self.key*((len(message)//len(self.key))+1)
        
        for i in range(len(message)):
            if message[i] not in self.alphabet:
                s += message[i]
            else:
#                s += self.vdict[mykey[i]][ord(message[i])-ord(self.alphabet[0])]
                s += self.vdict[mykey[i]][self.alphabet.find(message[i])]
        return s

    def fromLove(self, message):
        pass

def main():
    myClass = PHPGoAway()
    #myClass.setKey("LEMON")

    #for i in myClass.vdict.items():
    #    print(i)

    print(myClass.forLove("ATTACK AT DAWN!!!"))
    myClass.fromLove("Test")

if __name__ == "__main__":
    sys.exit(int(main() or 0))
