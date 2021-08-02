class loadGenes:
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

    def numberOfSequences(self):
        return len(self.splitFile)
    # <-- END: Splits the file into list -->

#<-- START: Splits the file and appends it to the list in the format [Name, Gene Sequence] -->
def loadFile(fileName):
    with open(fileName, 'r') as f:
        geneAssembly = loadGenes()
        for line in f:
            updatedLine = line.rstrip()
            if loadGenes.isNewSequence(updatedLine):
                geneAssembly.addNewSequenceInfo()
                geneAssembly.newSequenceStart(updatedLine)
            else:
                geneAssembly.appendSequence(updatedLine)
        geneAssembly.addNewSequenceInfo()
        return geneAssembly
#<-- END: Splits the file and appends it to the list in the format [Name, Gene Sequence] -->


class occurrences:
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A' }
    fullList, repetitions, errors, correctReads = [], [], [], []

    def __init__(self, reads) -> None:
        self.reads = reads

    def reverseComplement(self, gene):
        reverseComplementedGene = []
        reverseGene = gene[::-1]
        for char in reverseGene:
            reverseComplementedGene.append(self.complement[char])
        return ''.join(reverseComplementedGene)

    def countGeneOccurrences(self, gene):
        count = 0
        for seq in self.reads.splitFile:
            if seq[1] == gene:
                count+=1
            if seq[1] == self.reverseComplement(gene):
                count+=1
        return count

    def makeFullList(self):
        for seq in self.reads.splitFile:
            self.fullList.append(seq[1])
            self.fullList.append(self.reverseComplement(seq[1]))

    def occurrencesCounts(self):
        for item in self.reads.splitFile:
            self.repetitions.append([item[0], item[1], self.countGeneOccurrences(item[1])])

    def findErrorsAndCorrectReads(self):
        correct = []
        for item in self.repetitions: # finds Eroors
            if item[2] == 1:
                self.errors.append(item)
        for item in self.fullList:
            if (self.fullList.count(item) > 1 and
                 self.correctReads.count(item)==0):
                  self.correctReads.append(item)
        # for item in correct:
        #     if self.correctReads.count(item) == 0:
        #         self.correctReads.append(item)

    def hammingDistance(self, s1, s2):
        hammingDistance = 0
        for char in range(len(s2)):
            if s2[char] != s1[char]:
                hammingDistance += 1
        return hammingDistance
            
    def correctedRead(self):
        for seqA in self.errors:
            for seqB in self.correctReads:
                if self.hammingDistance(seqA[1], seqB) == 1:
                    print(seqA[1]+'->'+seqB)
                    

def errorCorrectionInReads(fileName):
    reads = loadFile(fileName)
    occurrencesCheck = occurrences(reads)
    occurrencesCheck.occurrencesCounts()
    occurrencesCheck.makeFullList()
    occurrencesCheck.findErrorsAndCorrectReads()
    occurrencesCheck.correctedRead()


fileName = '12_Error_Correction_in_Reads.txt'
errorCorrectionInReads(fileName)