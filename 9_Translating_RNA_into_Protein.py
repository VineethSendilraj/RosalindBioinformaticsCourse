import csv
rnaFile = "9_Rosland_RNA_Codeon_Table.csv"  # Opens RNA conversion table and Amino Acid information

rnaReader = csv.reader(open(rnaFile)) # Opens file and skips header
rnaReader.__next__()

rnaTranslator = {} # Creates a dictionary out of the RNA CSV file
for row in rnaReader:
    key = row[0]
    raa = row[1]
    for line in key.split(" or "):
       rnaTranslator[line] = raa

aminoSequence = []
def rnaConverter(codeons): # Function that converts the nucleotides into Amino acids
    for codeon in range(len(codeons)):
        finalCodeon = (codeons[codeon])
        rraa = ((rnaTranslator[finalCodeon]))
        aminoSequence.append(rraa)
    print('')
    print('The protien Sequence Is')
    print(''.join(aminoSequence))


sequence = input('Enter your Sequence: ')
codeons = [(sequence[i:i+3]) for i in range(0, len(sequence), 3)] # Splits the string every 3 characters
rnaConverter(codeons)
