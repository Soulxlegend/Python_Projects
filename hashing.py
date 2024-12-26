
class encrypting:
    def __init__(self, key):
        self.key = key
        # self.shift = ord(key) - ord('a')
        # self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        # self.cipher_text = ''
        # self.plain_text = ''

    def encrypt(self):
        string = self.key[2:7] + self.key[7:] + self.key[0:2] 
        layer2 = string[6:] + string[0:3] + string[3:6]
        layer3 = layer2[5:7] + layer2[0:3] + layer2[7:] + layer2[3:5] 
        layer4 = layer3[6:] + layer3[2:6] + layer3[0:2] 
        layer5 = layer4[1:4] + layer4[0] + layer4[4:7] + layer4[7:]
        layer6 = layer5[6:] + layer5[0:2] + layer5[2:6]
        layer7 = layer6[5:7] + layer6[0:3] + layer6[3:5] + layer6[7:]
        string = layer7[0:3] + layer7[3:6] + layer7[6:]
        print(string)
        

        
        
      

class decrypting:
    def __init__(self):
        self.key = "oulSxleg12end#33"
        # self.shift = ord(key) - ord('a')
        # self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        # self.cipher_text = ''
        # self.plain_text = ''

    def decrypt(self):
        # Reverse Layer 5
        # Starting from the final string value:
        string = self.key
        rev_layer7 = string[0:3] + string[3:6] + string[6:]
        rev_layer6 = rev_layer7[0:2] + rev_layer7[5:7] + rev_layer7[2:5] + rev_layer7[7:]
        rev_layer5 = rev_layer6[0:2] + rev_layer6[2:6] + rev_layer6[6:]
        rev_layer4 = rev_layer5[1:4] + rev_layer5[0] + rev_layer5[4:7] + rev_layer5[7:]
        rev_layer3 = rev_layer4[2:6] + rev_layer4[0:2] + rev_layer4[6:]
        rev_layer2 = rev_layer3[0:3] + rev_layer3[3:5] + rev_layer3[5:7] + rev_layer3[7:]
        self.key = rev_layer2[0:2] + rev_layer2[2:7] + rev_layer2[7:]
        print(self.key)
        






if __name__ == "__main__":
    # x = encrypting("python")
    # x.encrypt()
    encrypting("Soulxlegend1233#").encrypt()
    # decrypting().decrypt()