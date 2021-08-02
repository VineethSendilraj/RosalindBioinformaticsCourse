import csv

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

class RNASplicer(FastaConverter):
    def __init__(self, fastaConverter):
        self.convertedFile = fastaConverter.splitFile
        self.slicedGenome = fastaConverter.splitFile[:1][0][1]
    
    def intronSlicing(self):
        for intron in (self.convertedFile[1:]):
            loc = self.slicedGenome.find(intron[1])
            if loc >= 0:
                self.slicedGenome = self.slicedGenome[:loc] + self.slicedGenome[loc+len(intron[1]):]

class transcribeDNA(RNASplicer):
    def __init__(self, DNAspliced):
        self.sequence = DNAspliced.slicedGenome
        self.rnaString = ""

    def DNAtranscribe(self):
        for letter in self.sequence:
            self.rnaString += 'U' if letter == 'T' else letter
        
class aminoAcidConverter(transcribeDNA):
    rnaTranslator = {} # Creates a dictionary out of the RNA CSV file
    aminoSequence = []
    def __init__(self, rnaSpliced):
        rnaFile = "RNACodeonKey.csv"  # Opens RNA conversion table and Amino Acid information
        self.rnaReader = csv.reader(open(rnaFile)) # Opens file and skips header
        self.rnaReader.__next__()
        for row in self.rnaReader:
            key = row[0]
            raa = row[1] #raa = rna amino acid
            for line in key.split(" or "):
                self.rnaTranslator[line] = raa
        self.sequence = rnaSpliced.rnaString

    def createCodeon(self):
        return [(self.sequence[i:i+3]) for i in range(0, len(self.sequence), 3)] # Splits the string every 3 characters

    def convertRNA(self): # Function that converts the nucleotides into Amino acids
        allCodeons = self.createCodeon()
        for codeon in range(len(allCodeons)):
            rraa = (self.rnaTranslator[allCodeons[codeon]])
            self.aminoSequence.append(rraa)
        print(''.join(self.aminoSequence))

fileName = '14_RNA_Splicing.txt' 
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
    FastaFormatter(FastaConverter, f, ConvertFasta)#Splits the file and appends it to the list in the format [Name, Gene Sequence]
    CleanRNA = RNASplicer(ConvertFasta) #Takes information from fasta converter object
    CleanRNA.intronSlicing()
    DNAtoRNA = transcribeDNA(CleanRNA)
    DNAtoRNA.DNAtranscribe()
    rnaAAconverter = aminoAcidConverter(DNAtoRNA)
    rnaAAconverter.convertRNA()