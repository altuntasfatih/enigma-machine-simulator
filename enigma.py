import time
import argparse

import  sys



description = """
    Enigma machine v3  implemantation
    Usage: python enigma.py  [ Options ...]  -m plaintext
    Eg: python3 enigma.py -m CYBERSTRUGGLE -sp CSR -n2 E -n3 V 
"""



parser = argparse.ArgumentParser("Enigma machine implemantation", description)
parser.add_argument("--startpos", "-sp", help="Start position of root 1", required=False, default="AAA")
parser.add_argument("--notch2", "-n2", help="notch position of root 2", required=False, default="E")
parser.add_argument("--notch3", "-n3", help="notch position of root 3", required=False, default="V")
parser.add_argument("--message", "-m", help="input message to entry enigma machine ", required=True, default="CSR")
parser.add_argument("--reflactor", "-r", help="reflactor of A,B,C is avilable ", required=False, default='B')


args = parser.parse_args()

class WiringRotors:

    def __init__(self, name, pos,number,notch):
        self.name = name
        self.startpos = pos
        self.notch=notch
        self.scheme={}
        self.uploadScheme(number)

    def push(self,letter):

        temp = None;
        for key, value in self.scheme.items():
            index = ord(key) - 65
            index = ((index - self.startpos) + value) % 26

            if (chr(index + 65) == letter):
                print("Push ",self.name, ": ",letter + " -> " + key)
                temp = key
                break;

        return temp

    def uploadScheme(self,number):

        if number==1:
            self.scheme={"A":-6,'B':-5,'C':-4,'D':3,'E':-4,'F':-2,"G":-1,'H':8,"I":13,
                         "J":-10,"K":-9,"L":-7,"M":-10,"N":-3,"O":-2,"P":4,"Q":-9,"R":6,
                          "S":0,"T":-8,"U":-3,"V":-13,"W":-9,"X":-7,"Y":-10,"Z":10}

        elif number==2:
            self.scheme={"A":0,'B':8,'C':13,'D':-1,'E':-5,'F':-9,"G":11,'H':4,"I":-3,
                         "J":-8,"K":-7,"L":-1,"M":2,"N":6, "O":10,"P":5,"Q":0,"R":-11,
                         "S":12,"T":-6,"U":13,"V":2,"W":-10,"X":11,"Y":-3,"Z":-7}

        else:
            self.scheme={"A":-7,'B':-1,'C':4,'D':-2,'E':11,'F':-3,"G":12,'H':-4,"I":8,
                         "J":-5,"K":10,"L":-6,"M":9,"N":0,"O":11,"P":-8,"Q":8,"R":-9,
                         "S":5,"T":-10,"U":2,"V":-10,"W":-5,"X":-13,"Y":-10,"Z":-13}


def nextIndex(letter,startpos):
    index = ord(letter) - 65
    index = (index - startpos) % 26
    return  index

def reverseIndex(letter,index,rotor,nextstartpos):

    index = ord(letter) - 65
    index = (index - rotor.startpos + rotor.scheme[letter] + nextstartpos) % 26
    print("Reverse Directoin in "+rotor.name+" : " + letter + " -> " + chr(65 + index))

    return index;

def turnRotor(r1,r2,r3):

    if r3.startpos==r3.notch:

        if r2.startpos==r2.notch:
            r2.startpos += 1
            r1.startpos += 1
        else:
            r2.startpos += 1

    r3.startpos += 1


def run():

    rotor1 = WiringRotors("rotor1",ord(args.startpos[0])-65,1,None)
    rotor2 = WiringRotors("rotor2", ord(args.startpos[1])-65, 2,ord(args.notch2)-65)
    rotor3 = WiringRotors("rotor3", ord(args.startpos[2])-65, 3,ord(args.notch3)-65)
    result=""

    for letter in args.message:

        print("Input is :",letter)

        turnRotor(rotor1,rotor2,rotor3)
        newL=rotor3.push(letter)

        index=nextIndex(newL,rotor3.startpos)


        newL=rotor2.push(chr(65+index));
        index = nextIndex(newL, rotor2.startpos)


        newL = rotor1.push(chr(65+index))
        newL=reflactorB(newL,rotor1.startpos);  #reflactor


        # Reverse Now

        print("Reverseee Start ")


        index=reverseIndex(newL,index,rotor1,rotor2.startpos)
        newL = chr(65 + index)

        index = reverseIndex(newL, index, rotor2, rotor3.startpos)
        newL = chr(65 + index)

        index = reverseIndex(newL, index, rotor3,0)
        newL = chr(65 + index)

        print("Output is :", newL)
        result=result+newL
        print("-"*120)


    print("Enigma :",args.message," -> ",result)



def reflactorB(letter,startpos1):

    reflactorBmap = {"A": -2, 'B': -10, 'C': -8, 'D': 4, 'E': 12, 'F': 13, "G": 5, 'H': -4, "I": 7,
                     "J": 14, "K": 3,"L": -5, "M": 2, "N": -3, "O": -2, "P": -7, "Q": -12, "R": 10,
                      "S": -13, "T": 6, "U": 8, "V":1, "W": -1, "X": -14, "Y": 2, "Z": -6}

    index = ord(letter) - 65
    index = (index - startpos1) % 26
    swapvalue=reflactorBmap[chr(65+index)]
    index = (((ord(letter)-65)+swapvalue) % 26)

    print("Reflactor B:", letter + " -> " +chr(65+index) )

    return chr(65+index);










if __name__ == "__main__":
    print("Running")
    if len(sys.argv) < 2:
        print (parser.print_help())
        exit()
    print("Message is ", args.message)
    print("Initial posion of rotor ", args.startpos)
    print("Notch posion of rotor3 and rotor2 ", args.notch3,args.notch3)
    print("-" * 120)
    run()




