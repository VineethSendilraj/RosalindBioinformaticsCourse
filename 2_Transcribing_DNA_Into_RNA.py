s = 'CTGGGATCATTCTACGTATCGCAGGACGGTAACTCGTTCGCTCCGCCTACTTGGGAAAAAATCGATCCGATGTCCTAAGTTAGTCCGCGTTCCTTTTCCTTCATTCTCGCCTACGCGAATGGCCGGTCCCAGGGCAATACCCCGAAGGGGGTCCCAATGGCAGCCGAGCATTTAAGCCTTCAATTGCCTTTATCGATATGGCGGCCTGGAAAGCCAACTGGGCGTAAGGGCATGTCAGGACAGATTTGCCTCTCGCTCGGAGTAAGACCTGTGCCTAAAAAAGAGGCGGTCCGATTTTAAACTGACCTAAATTGACGGGAAACTCGAGTTGGTCGTAGCGCAAGGCTGAGCAACGACTAAACAGTAGCTACCACCCGGGGTTTATTCCGGGATCACACTCCGGGCTTGAACGTGCACGGAGAGTTCCGGATTAGAGGTGCAACGTTCGATCGGCCACCAATGCACCTGTCGAATGCGATCCCACGGATACCTCCCGTACGCGCATTAGCATGGGCCACTAGGGGGCCGTACTATAAACGTCGTCGTAGATCAGATCGAAATACCACGATGTGTTGGATTCATAGCATTGATGAATCGTTACCATATTACGGTGTATGCCCAGTAATATGGCGACTATACGTTAGATTTCGAGGTGGAGATGTTAATGCCGACGGAGCCCGCGGCGATTCACATGGCCGGGTAGATTCGATGAACCTAACGCAGTCATGGCCAGACATCTGGGTACAAGATATGACTAAAACGAGTCGGCGAGTGGGAAAGTGTGAGCTAGGGCCGCGATATTGTGTTAACCTTGACCATGGGACTGTAGTACAGCCACGTCTGCCTTGCAGAAAAAAGCGCCTGTTAGTCCGTGGTAAGGTGACGTCACCTAAACTGCGCACTAAGAATCAACAGTTATCTAAACCATTTTCCATTGCGGTATCATCTGCCCGTCGACA'
ns = []
for i in s:
    if i == 'T':
        ns.append('U')
    else:
        ns.append(i)

print(''.join(ns))