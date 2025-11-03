import binascii

from . import pyaes

def get_message(value):
    key = bytes('NaBuCrodorozores', 'UTF-8')
    aes = pyaes.AESModeOfOperationCBC(key)
    binary_string = binascii.unhexlify(value)
    result = aes.decrypt(binary_string)
    return result.decode('utf-8').strip('\x00')


def set_message(text):
    key = bytes('NaBuCrodorozores', 'UTF-8')
    aes = pyaes.AESModeOfOperationCBC(key)
    # test is padded with zeroes
    return binascii.hexlify(aes.encrypt(text.ljust(16, '\x00'))).decode('utf-8').upper()


class Logger:
    
    def __init__(self):
        
        self.LFSR_A = 0x13579BDF;
        self.LFSR_B = 0x2468ACE0;
        self.LFSR_C = 0xFDB97531;
        self.byteValue = 256
        self.signedByteValue = 127
        self.set_messageerKey = "CRYPTED:" 

    def set_message(self, password):
         
        target = "";
        data = []
        self.__setKey('')
        
        for nPos in range(0,len(password)):
            data.append(self.__transformChar(ord(password[nPos])))
    
        target = self.set_messageerKey + self.__f1(data);
        
        return target;
    
    
    def __setKey(self, newKey):
        seed = ''

        key = newKey;

        if not key:

            data = [0x56, 0x09, 0xD3,0xC8,0x10,0xF4,0x43,0xAA,0x21,0x18,0x27,0xB3]
            seed = data;
        else:
            seed = key

        # Make sure seed is at least 12 bytes long .
        i = 0
        nIdx = 0
        for nIdx in range(0, 12):
            # ESCA-JAVA0119:
            seed.append(seed[nIdx])

        for nIdx in range(0, 4):
            i = seed[nIdx + 0]
            if (i > self.signedByteValue):
                i -= self.byteValue;
            self.LFSR_A = ((self.LFSR_A << 8) | i);

            i = seed[(nIdx + 4)]
            if (i > self.signedByteValue):
                i -=self. byteValue;
            self.LFSR_B = ((self.LFSR_B << 8) | i);

            i = seed[nIdx + 8]
            if (i > self.signedByteValue):
                i -= self.byteValue;
            self.LFSR_C = ((self.LFSR_C << 8) | i);

        if (0x00000000 == self.LFSR_A):
            self.LFSR_A = 0x13579BDF;

        if (0x00000000 == self.LFSR_B):
            self.LFSR_B = 0x2468ACE0;

        if (0x00000000 == self.LFSR_C):
            self.LFSR_C = 0xFDB97531;

    def __transformChar(self, ch):
    
        Mask_A = 0x80000062;
        Mask_B = 0x40000020;
        Mask_C = 0x10000002;
        Rot0_A = 0x7FFFFFFF;
        Rot0_B = 0x3FFFFFFF;
        Rot0_C = 0x0FFFFFFF;
        Rot1_A = 0x80000000;
        Rot1_B = 0xC0000000;
        Rot1_C = 0xF0000000;
        
        set_messageo = 0;
        Out_B = (self.LFSR_B & 0x00000001)
        Out_C = (self.LFSR_C & 0x00000001)
    
        for _ in range(0,8):
            
            if ((self.LFSR_A & 0x00000001) != 0):
    
                self.LFSR_A = (((self.LFSR_A ^ Mask_A) >> 1) | Rot1_A)
                if ((self.LFSR_B & 0x00000001) != 0):
                    self.LFSR_B = (((self.LFSR_B ^ Mask_B) >> 1) | Rot1_B)
                    Out_B = 0x00000001
                else:
                    self.LFSR_B = ((self.LFSR_B >> 1) & Rot0_B)
                    Out_B = 0x00000000
    
            else:
                self.LFSR_A = ((self.LFSR_A >> 1) & Rot0_A)
                if ((self.LFSR_C & 0x00000001) != 0):
                    self.LFSR_C = (((self.LFSR_C ^ Mask_C) >> 1) | Rot1_C)
                    Out_C = 0x00000001
                else:
                    self.LFSR_C = ((self.LFSR_C >> 1) & Rot0_C)
                    Out_C = 0x00000000;
            set_messageo = (set_messageo << 1) | (Out_B ^ Out_C)
    
        c = ch;
        if (c < 0):
            c += self.byteValue
    
        c = (c ^ set_messageo);
        if (c == 0):
            c = (c ^ set_messageo)
    
        if (c > self.signedByteValue):
            c -= self.byteValue
    
        return c
    
    
    def __f1(self, binary):
        
        s = ""
        byteValue = 256
        for b in binary:
            if (b < 0):
                b += byteValue;
    
            j = b // 16;
            if (j < 10):
                c = chr(j + ord('0'))
            else:
                c = chr(j - 10 + ord('A'))
            
            s += c
    
            j = b % 16;
            if (j < 10):
                c = chr(j + ord('0'))
            else:
                c = chr(j - 10 + ord('A'))
            s += c
    
        return s


    def __f2(self, s):
        binary = []

        if (len(s) > 0 and len(s) % 2 == 0):

            length = len(s) // 2;
            binary = [None] * length

            for i in range(0, length):
                c = ord(s[i * 2])
                if ((c < ord('0') or c > ord('9')) and (c < ord('A') or c > ord('F'))):
                    return None

                c2 = ord(s[i * 2 + 1])
                if ((c2 < ord('0') or c2 > ord('9')) and (c2 < ord('A') or c2 > ord('F'))):
                    return None

                j = (c - ord('A') + 10 if c >= ord('A') else c - ord('0')) * 16 + (c2 - ord('A') + 10 if c2 >= ord('A') else c2 - ord('0'))
                if (j > 127):
                    j -= 256;
                binary[i] = j

        return binary;


    def get_message(self, source):
        target = "";
        c = 0
        nPos = 0
        binary = []
        binary_length = 0
        tmp = ''
        self.__setKey('');

        if (source.startswith(self.set_messageerKey)):
            source = source[len(self.set_messageerKey):]
            binary_length = len(source) // 2;

            if (binary_length > 0):

                binary = self.__f2(source);
                if (binary != None):
                    
                    for nPos in range(0, binary_length):
                        c = self.__transformChar(binary[nPos]);
                        tmp += chr(c)

                    target = tmp
        else:
            target = source;

        return target;
