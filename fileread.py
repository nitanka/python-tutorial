from os.path import exists
from os import getcwd

FILENAME = 'nitanka.txt'

snow = 10
mode = 'a' if not exists(str.join('/',(getcwd(),FILENAME))) else 'w'

with open(FILENAME,mode) as FILE:
    print ("Mary had a little lamb.",file=FILE)
    print ("Its fleece was white as %d %s." %(snow, 'nitanka'),file=FILE)
    print ("And everywhere that Mary went.",flush=True,file=FILE)
    print ("." * snow,file=FILE)  # what'd that do?

    end1 = "C"
    end2 = "h"
    end3 = "e"
    end4 = "e"
    end5 = "s"
    end6 = "e"
    end7 = "B"
    end8 = "u"
    end9 = "r"
    end10 = "g"
    end11 = "e"
    end12 = "r"

    print(end1,end2,end3,end4,end5,end6,sep='',end=' ',file=FILE)
    print(end7,end8,end9,end10,end11,end12,sep='',file=FILE)

print(str.join('/',(getcwd(),FILENAME)))

mode = 'a' if not exists(str.join('/',(getcwd(),FILENAME))) else 'r'
with open(FILENAME, mode) as FILE:
    for line in FILE:
        print(line)

   


