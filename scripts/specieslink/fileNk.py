class File:

    def writeToFile(self,fileName,content):
        file = open(fileName,"w")
        file.write(content)
        file.close()
