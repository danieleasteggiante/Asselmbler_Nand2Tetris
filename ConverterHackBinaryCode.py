class ConverterHackBinaryCode:

    cInstruction = {
            "dest" : {
              "M":  "001",
              "D":  "010",
              "MD": "011",
              "A":  "100",
              "AM": "101",
              "AD": "110",
              "AMD":"111"
            },

            "jump" : {
                "JGT":"001",
                "JEQ":"010",
                "JGE":"011",
                "JLT":"100",
                "JNE":"101",
                "JLE":"110",
                "JMP":"111"
            },

            "comp" : {
                "!a":{
                        "0" : "101010",
                        "1" : "111111",
                        "-1" : "111010",
                        "D" : "001100",
                        "A" : "110000",
                        "!D": "001101",
                        "!A": "110001",
                        "-D": "001111",
                        "-A": "110011",
                        "D+1":"011111",
                        "A+1":"110111",
                        "D-1":"001110",
                        "A-1":"110010",
                        "D+A":"000010",
                        "D-A":"010011",
                        "A-D":"000111",
                        "D&A":"000000",
                        "D|A":"010101",                
                    },
                
                "a" : {                
                        "M" : "110000",                    
                        "!M": "110001",                        
                        "-M": "110011",                       
                        "M+1":"110111",                        
                        "M-1":"110010",
                        "D+M":"000010",
                        "D-M":"010011",
                        "M-D":"000111",
                        "D&M":"000000",
                        "D|M":"010101"
                        }
                  }
           }




    def __init__(self):
        pass

    def aOrcInstruction (self, instruction):
        intructionTrype= None
        if instruction[0] == "@":
            instructionType = "a"
        else:
            instructionType = "c"
        return instructionType

    def convertAInstruction(self,instruction):
        aInstruction = int(instruction.replace("@", "0"))
        aInstruction = format(aInstruction, "016b")
        aIntruction =  str(aInstruction)
        return aInstruction

    def separeCInstruction(self, instruction):
        dest = None
        comp = None
        jump = None
        separatorDC=0
        separatorCJ=0

        if "=" in instruction and ";" not in instruction:
            separatorDC = instruction.find("=")
            dest = instruction[0:separatorDC]
            comp = instruction[separatorDC+1:]
        elif ";" in instruction and "=" not in instruction:
            separatorCJ = instruction.find(";")
            comp = instruction[separatorDC:separatorCJ]
            jump = instruction[separatorCJ+1:]
        elif ";" in instruction and "=" in instruction:
            separatorDC = instruction.find("=")
            separatorCJ = instruction.find(";")
            dest = instruction[0:separatorDC]
            comp = instruction[separatorDC+1:separatorCJ]
            jump = instruction[separatorCJ+1:]

        cInstruction = [dest,comp,jump]
        return cInstruction

    def convertCInstruction(self, instruction):
        destBinary = self.cInstruction["dest"][instruction[0]] if instruction[0] else "000"
        jumpBinary = self.cInstruction["jump"][instruction[2]] if instruction[2] else "000"
        compBinary = self.convertComputation(instruction[1])
        cInstruction = "111" + compBinary + destBinary + jumpBinary
        return cInstruction

    def convertComputation(self, computation):
        computationBinary = None
        if computation in  self.cInstruction["comp"]["!a"]:
            computationBinary = "0" + self.cInstruction["comp"]["!a"][computation]
        elif computation in self.cInstruction["comp"]["a"]:
            computationBinary = "1" + self.cInstruction["comp"]["a"][computation]
        else:
            computationBinary = "0000000"
        return computationBinary

    def getInstruction(self, instruction):
        typeOfInstruction = self.aOrcInstruction(instruction)
        if typeOfInstruction == "a":
            aInstruction = self.convertAInstruction(instruction)
            return aInstruction
        elif typeOfInstruction =="c":
            cInstructionArr = self.separeCInstruction(instruction)
            cInstruction = self.convertCInstruction(cInstructionArr)
            return cInstruction
        else:
            return "Error type of instruction does not exist"


        
