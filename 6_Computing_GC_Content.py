
class fastaSequences:
    name, Gsequence = '', ''
    GDataSets=[]
    def isNewSequence(line):
        return line[0] == '>'

    def newSequenceStart(self, line):
          self.name = line[1:]  

    def addNewSequenceInfo(self):
        if(len(self.Gsequence)>0):
            self. GDataSets.append([self.name, self.Gsequence])
            self.name=''
            self. Gsequence =  ''  
    def appendSequence(self, line):
        self.Gsequence += line

    def processSeqeunce(self):
        percentages = []
        for line in self.GDataSets:
            repititons, percent = 0, 0
            for char in line[1]:
                if char == 'G' or char == 'C':
                    repititons += 1
            percent = (repititons/len(line[1]) * 100)
            percentages.append([percent, line[0]])
        percentages.sort()
        return percentages[-1]



fileName = '5_ComputingGC_Content_Test_File.txt'
with open(fileName, 'r') as f:
    table = fastaSequences() 
    
    for line in f:
        updateLine = line.rstrip()
        if  fastaSequences.isNewSequence(updateLine):
            table.addNewSequenceInfo()
            table.newSequenceStart(updateLine)
        else:
            table.appendSequence(updateLine)
    table.addNewSequenceInfo()
    percentage = table.processSeqeunce()
    print(percentage[1])
    print(percentage[0])


