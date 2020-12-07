class Parser:
    lines = None
    def __init__(self, pathFile):
        self.pathFile = pathFile
        self.openFileToParse()

    def openFileToParse(self):
        f = open(self.pathFile, "r")
        self.lines = f.readlines()
        

    def deleteComments(self):
        self.lines
        lines = []
        for item in self.lines:
            if not item.startswith('//'):
                if not item.startswith('\n'):
                    item = self.deleteAcapo(item,'\n')
                    item = self.deleteCommentInline(item)
                    lines.append(item.strip())
        self.lines = lines
        return self.lines

    def deleteAcapo(self, string, strToDel):
        item = string.replace('\n', '')
        return item

    def deleteCommentInline(self, string):
        result = string.find('//')
        if (result != -1):
            return string[0:result]
        else:
            return string
        
        
   


