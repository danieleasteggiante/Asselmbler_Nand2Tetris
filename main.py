from Parser import Parser as P
from ConverterHackBinaryCode import ConverterHackBinaryCode as C
from LabelConverter import LabelConverter as L

fileToTranslate = input("Enter a filepath: ")


parser = P(fileToTranslate)
row= parser.deleteComments()
label = L(row)
label.clearLabel()
label.findSimbol()
print(label.instruction)
converter = C()

finalConversion = []

for item in label.instruction:
    output = converter.getInstruction(item)
    finalConversion.append(output)

print(finalConversion)

indexLastFolder = fileToTranslate.rfind('\\')
indexPoint = fileToTranslate.rfind('.')

nameFile=fileToTranslate[indexLastFolder+1:indexPoint]

f = open(nameFile+".hack", "a")
for item in finalConversion:
        f.write("%s\n" % item)
f.close()
