class File:

    def writeToFile(self,fileName,content):
        file = open(fileName,"w")
        file.write(content)
        file.close()


    def readFileToArray(self,fileName):
        file = open(fileName,"r")
        lines = (file.read()).split("\n")
        out = []
        for line in lines:
            if line.strip()!="":
                out.append(line)
        return out
