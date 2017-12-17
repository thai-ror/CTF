hexdb = {" ": "20",    "!": "21",    "\"": "22",   "#": "23",
"$": "24",    "%": "25",    "&": "26",    "'": "27",
"(": "28",    ")": "29",    "*": "2a",    "+": "2b",
",": "2c",    "-": "2d",    ".": "2e",    "/": "2f",
"0": "30",    "1": "31",    "2": "32",    "3": "33",
"4": "34",    "5": "35",    "6": "36",    "7": "37",
"8": "38",    "9": "39",    ":": "3a",    ";": "3b",
"<": "3c",    "=": "3d",    ">": "3e",    "?": "3f",
"@": "40",    "A": "41",    "B": "42",    "C": "43",
"D": "44",    "E": "45",    "F": "46",    "G": "47",
"H": "48",    "I": "49",    "J": "4a",    "K": "4b",
"L": "4c",    "M": "4d",    "N": "4e",    "O": "4f",
"P": "50",    "Q": "51",    "R": "52",    "S": "53",
"T": "54",    "U": "55",    "V": "56",    "W": "57",
"X": "58",    "Y": "59",    "Z": "5a",    "[": "5b",
"\"": "5c",   "]": "5d",    "^": "5e",    "_": "5f",
"`": "60",    "a": "61",    "b": "62",    "c": "63",
"d": "64",    "e": "65",    "f": "66",    "g": "67",
"h": "68",    "i": "69",    "j": "6a",    "k": "6b",
"l": "6c",    "m": "6d",    "n": "6e",    "o": "6f",
"p": "70",    "q": "71",    "r": "72",    "s": "73",
"t": "74",    "u": "75",    "v": "76",    "w": "77",
"x": "78",    "y": "79",    "z": "7a",    "{": "7b",
"|": "7c",    "}": "7d",    "~": "7e"}

hexdb_Reverse={'24': '$', '25': '%', '26': '&', '27': "'", '20': ' ', '21': '!', '23': '#', '28': '(', '29': ')', '5e': '^', '5d': ']', '5f': '_', '5a': 'Z', '5c': '"', '5b': '[', '59': 'Y', '58': 'X', '55': 'U', '54': 'T', '57': 'W', '56': 'V', '51': 'Q', '50': 'P', '53': 'S', '52': 'R', '2d': '-', '2e': '.', '2f': '/', '2a': '*', '2b': '+', '2c': ',', '3c': '<', '3b': ';', '3a': ':', '3f': '?', '3e': '>', '3d': '=', '39': '9', '38': '8', '33': '3', '32': '2', '31': '1', '30': '0', '37': '7', '36': '6', '35': '5', '34': '4', '60': '`', '61': 'a', '62': 'b', '63': 'c', '64': 'd', '65': 'e', '66': 'f', '67': 'g', '68': 'h', '69': 'i', '6a': 'j', '6b': 'k', '6c': 'l', '6d': 'm', '6e': 'n', '6f': 'o', '7e': '~', '7d': '}', '7c': '|', '7b': '{', '7a': 'z', '48': 'H', '49': 'I', '46': 'F', '47': 'G', '44': 'D', '45': 'E', '42': 'B', '43': 'C', '40': '@', '41': 'A', '77': 'w', '76': 'v', '75': 'u', '74': 't', '73': 's', '72': 'r', '71': 'q', '70': 'p', '79': 'y', '78': 'x', '4f': 'O', '4d': 'M', '4e': 'N', '4b': 'K', '4c': 'L', '4a': 'J'}



def shTurn(char):
    char = char.replace(char, hexdb[char])
    return char

def decodeTurn(char):
    char = char.replace(char, hexdb_Reverse[char])
    return char

def shGenerate(string):
    shlist =  map(shTurn, string)
    shlist = "\\x".join(shlist)
    shlist = "\\x"+shlist
    return shlist

def shDecode(string):
    shlist=""
    try:
        for i in range(0,len(string),2):
            s=string[i:i+2]
            #print s,
            shlist+=shlist.join(decodeTurn(s))
    except:
        print "Err"
    return shlist

def main():
    print "[1].Shellcode --> Ascii shellcode : "
    print "[2].Ascii shellcode -->Shellcode  : "
    c=raw_input("Choice ")
    print "~"*30
    if c=="2":
        string =raw_input("Input string: ")
        
        print shGenerate(string)
        print "Disassemble at: https://defuse.ca/online-x86-assembler.htm#disassembly2"
    elif c=="1":
        string =raw_input("Input string: ")
        
        print shDecode(str(string))


if __name__ == '__main__':
    main()
