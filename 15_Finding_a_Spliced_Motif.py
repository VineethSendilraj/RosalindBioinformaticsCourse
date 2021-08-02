class FastaConverter:
    splitFile = []
    name, Gsequence = '', ''

    # <-- START: Splits the file into list -->
    def isNewSequence(line):
        return line[0] == '>'

    def newSequenceStart(self, line):
          self.name = line[1:]  

    def addNewSequenceInfo(self):
        if(len(self.Gsequence) > 0):
            self.splitFile.append([self.name, self.Gsequence])
            self.name, self.Gsequence = '', ''
    def appendSequence(self, line):
        self.Gsequence += line
    # <-- END: Splits the file into list -->

class subSequenceFinder(FastaConverter): 
    indicesLocation = [0]
    def __init__(self, sequence):
        self.sequence = sequence.splitFile[0][1]
        self.subSequence = sequence.splitFile[1][1]
    def findIndices(self): #Gives the indices location for a subsequence
        for letter in self.subSequence:
            loc = self.sequence[self.indicesLocation[-1]:].find(letter)
            if loc >= 0:
                self.indicesLocation.append(loc+self.indicesLocation[-1]+1) #Appends the location + the index of the last appended number
        print(' '.join(str(index) for index in self.indicesLocation[1:])) #adds a space between the indices(not in list format -> [1,2,3])


fileName = '15_Finding_a_Spliced_Motif.txt' 
def FastaFormatter(FastaConverter, f, ConvertFasta):
    for line in f:
        updatedLine = line.rstrip()
        if  FastaConverter.isNewSequence(updatedLine):
            ConvertFasta.addNewSequenceInfo()
            ConvertFasta.newSequenceStart(updatedLine)
        else:
            ConvertFasta.appendSequence(updatedLine)
    ConvertFasta.addNewSequenceInfo()

with open(fileName, 'r') as f:
    ConvertFasta = FastaConverter()
    FastaFormatter(FastaConverter, f, ConvertFasta) #Splits the file and appends it to the list in the format [Name, Gene Sequence]
    checkSS = subSequenceFinder(ConvertFasta)
    checkSS.findIndices()
