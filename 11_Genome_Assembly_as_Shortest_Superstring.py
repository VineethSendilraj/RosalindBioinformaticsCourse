import math
from collections import namedtuple
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

    def getSequence(self, index):
        if ( index >= self.numberOfSequences()):
            return None
        gene = self.splitFile[index]
        return (gene[0],gene[1])
    def findGeneByName(self, name):
        for seq in self.splitFile:
            if ( seq[0]== name):
                return seq[1]

#<-- START: Splits the file and appends it to the list in the format [Name, Gene Sequence] -->
def loadFile(fileName):
    with open(fileName, 'r') as f:
        geneAssembly = loadGenes()
        for line in f:
            updatedLine = line.rstrip()
            if  loadGenes.isNewSequence(updatedLine):
                geneAssembly.addNewSequenceInfo()
                geneAssembly.newSequenceStart(updatedLine)
            else:
                geneAssembly.appendSequence(updatedLine)
        geneAssembly.addNewSequenceInfo()
        return geneAssembly
#<-- END: Splits the file and appends it to the list in the format [Name, Gene Sequence] -->

class checkOverlap:
    geneRel = namedtuple('geneRel',"s1 s1gene s2 s2gene maxlen")
    def setMinVal( s):
        return  math.floor(len(s)/2) + 1

    def __init__(self, genes) -> None:
        self.genes = genes


     # <-- START: Checks if the two strings overlap -->
    def oCheck(s1, s2, minLength):
        start = 0
        while True:
            index = s1.find(s2[:minLength], start)
            if index == -1:
                return (False,-1)
            if s2.startswith(s1[index:]):
                return (True, len(s1[index:]))
            start +=1

    def findMaxMatch(self,s1):
        maxlen, lastMatch, lastmatchname = 0, "", ""
        for i in range(self.genes.numberOfSequences()):
            name,gene = self.genes.getSequence(i)
            if ( gene != s1):
               result, len = checkOverlap.oCheck(s1,gene,checkOverlap.setMinVal(s1))
               if ( result ==True and maxlen < len):
                     maxlen = len
                     lastMatch = gene
                     lastmatchname = name
        return (maxlen, lastmatchname, lastMatch)

    def buildSeq(self):
         finalSeq=[]

         for i in range(self.genes.numberOfSequences()):
            name,gene = self.genes.getSequence(i)
            maxlen, matchname, matchgene =self.findMaxMatch(gene)
            if (maxlen>0 ):
              finalSeq.append(self.geneRel(name, gene, matchname, matchgene, maxlen))
         return finalSeq
    def getFirstSeq (self,lst):
        for elem in lst:
            if ( sum (1 for cur in lst if cur.s2 == elem.s1)==0):
                return elem

    def buildChromosome(self):
        result = self.buildSeq()
        currentgene =  self.getFirstSeq(result) # max(result, key = lambda cur: cur.maxlen )
        finalOutput =[]
        while(len(result)>0 ):
            finalOutput.append(currentgene)
            result.remove(currentgene)
            if ( len(result)==0 ):
              break
            nextSeq =None
            for elem in result:
              if (elem.s1 == currentgene.s2):
                   nextSeq = elem
                   break
            currentgene =(nextSeq, None) [nextSeq == None]
            if (currentgene == None):
                #sequence stops
                break
        return finalOutput

    def buildSequence(self):
        result = self.buildChromosome()
        start = result[0]
        strChromoSome = start.s1gene + start.s2gene[start.maxlen:]
        result.remove(start)
        for grel in result:
            strChromoSome += grel.s2gene[grel.maxlen:]
        return strChromoSome


def genomeShortestString(fileName):
    genes = loadFile(fileName)
    x = checkOverlap(genes)
    x.buildChromosome()
    print(x.buildSequence())

fileName = '11_Genome_AssemblyAs_Shortest_Superstring_Test_File.txt'
genomeShortestString(fileName)