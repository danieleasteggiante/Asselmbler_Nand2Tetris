class LabelConverter:

    memorySpace=15
    instNumber = -1
    exist = None
    isSimbol = False

    userSimbols = {
        }

    userLabels = {
        }

    predefSimbols = {
            "SP":   "0",
            "LCL":  "1",
            "ARG":  "2",
            "THIS": "3",
            "THAT": "4",
            "R0":   "0",
            "R1":   "1",
            "R2":   "2",
            "R3":   "3",
            "R4":   "4",
            "R5":   "5",
            "R6":   "6",
            "R7":   "7",
            "R8":   "8",
            "R9":   "9",
            "R10":  "10",
            "R11":  "11",
            "R12":  "12",
            "R13":  "13",
            "R14":  "14",
            "R15":  "15",
            "SCREEN":   "16384",
            "KBD":   "24576",
            }

    def __init__(self, instruction):
        self.instruction =  instruction

    def clearLabel(self):
        newInstruction = []

        for item in self.instruction:
            if item[0] == '(':
                self.saveLabel(item)
            else:
                self.instructionNumber()
                newInstruction.append(item)

        self.instruction = newInstruction


    def saveLabel(self, instruction):
        key = instruction[1:-1]
        if key not in self.userLabels:
            self.userLabels[key] = self.instNumber + 1


    def findSimbol (self):
        newInstruction=[]
        
        for item in self.instruction:
            if item[0] == '@' and item[1].isalpha():
                self.saveSimbol(item)
                newItem = "@" + str(self.sobstituteSimbol(item))
                newInstruction.append(newItem)
            else:
                newInstruction.append(item)

        self.instruction = newInstruction

                                   
    def saveSimbol(self,instruction):
        key = instruction[1:]
        if key not in self.userSimbols:
            if key not in self.userLabels:
                if key not in self.predefSimbols:
                    self.nextMemorySpace()
                    self.userSimbols[key] = self.memorySpace


    def sobstituteSimbol(self, instruction):
        key = instruction[1:]
        if key in self.userLabels:
            return self.userLabels[key]
        elif key in self.predefSimbols:
            return self.predefSimbols[key]
        elif key in self.userSimbols:
            return self.userSimbols[key]


    def nextMemorySpace(self):
        self.memorySpace = self.memorySpace + 1
        return self.memorySpace

    def instructionNumber(self):
        self.instNumber = self.instNumber + 1
        return self.instNumber



