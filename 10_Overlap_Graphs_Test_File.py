class overlapGraph:
    splitFile = []
    name, Gsequence = '', ''

    # <-- START: Splits the file into list -->
    def isNewSequence(line):
        return line[0] == '>'

    def newSequenceStart(self, line):
          self.name = line[1:]  

    def addNewSequenceInfo(self):
        if(len(self.Gsequence)>0):
            self.splitFile.append([self.name, self.Gsequence])
            self.name, self.Gsequence = '', ''
    def appendSequence(self, line):
        self.Gsequence += line
    # <-- END: Splits the file into list -->

    # <-- START: Checks if the two strings overlap -->
    def oCheck(self, s1, s2, minLength):
        start = 0
        while True:
            if s1[len(s1) - minLength:] == s2[:minLength]:
                return True
            else:
                return False
            start +=1
    # <-- END: Checks if the two strings overlap -->
    


fileName = '10_Overlap_Graphs_Test_File.txt' 
with open(fileName, 'r') as f:
    oGraph = overlapGraph()

    #<-- START: Splits the file and appends it to the list in the format [Name, Gene Sequence] -->
    for line in f:
        updatedLine = line.rstrip()
        if  overlapGraph.isNewSequence(updatedLine):
            oGraph.addNewSequenceInfo()
            oGraph.newSequenceStart(updatedLine)
        else:
            oGraph.appendSequence(updatedLine)
    oGraph.addNewSequenceInfo()
    #<-- END: Splits the file and appends it to the list in the format [Name, Gene Sequence] -->

    for item in range(len(oGraph.splitFile)):
        s1 = oGraph.splitFile[item][1]
        for item2 in oGraph.splitFile: 
            s2 = item2[1]
            if s1 != s2:
                if oGraph.oCheck(s1, s2, 3):
                    print(oGraph.splitFile[item][0], item2[0])