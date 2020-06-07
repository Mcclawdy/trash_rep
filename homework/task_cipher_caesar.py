def encode(s, rotn = 1):
        text_c = []
        for i in s:
                if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                        if 65 <= ord(i) <= 90 and ord(i) + rotn > 90:
                            text_c = text_c + list(chr((ord(i) - 26) + rotn))
                        elif 97 <= ord(i) <= 122 and ord(i) + rotn > 122:
                            text_c = text_c + list(chr((ord(i) - 26) + rotn))
                        else:
                            text_c = text_c + list(chr(ord(i) + rotn))
                else:
                        text_c = text_c + [i]
        text_c = ''.join(text_c)
        print (text_c)
        return text_c
                         

def decode(s, rotn = 0):
        text_d = []
        for i in s:
                if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                        if 65 <= ord(i) <= 90 and ord(i) - rotn < 65:
                            text_d = text_d + list(chr((ord(i) + 26) - rotn))
                        elif 97 <= ord(i) <= 122 and ord(i) - rotn < 97:
                            text_d = text_d + list(chr((ord(i) + 26) - rotn))
                        else:
                            text_d = text_d + list(chr(ord(i) - rotn))
                else:
                    text_d = text_d + [i]
        text_d = ''.join(text_d)
        print (text_d)
        return text_d