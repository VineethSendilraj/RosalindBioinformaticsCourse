s = "TTTAGCTATATAGCTTTAGCCATGTAGTCAGTGAGCATGCCTAAGACACACGTGCTAAGGAACAAACGCGCCTCTAAGCACTGTCATGAGAAAGCGCGGACCTACAGCAATTACCTGTATGCTTGTTTATAGAGGAAAAGAAGTACCTGGGATCCACTCACCTCCGTGTTAGCCAGGCGCCTCTACTGGTGCCTGAAGCAGGACGCTTGAAATGTTCAGACAATGTTCCGTAATAGCCATTGTAAACTCTCCTCCCTTTGCAGTTTTTTAGGATCGACGAAGATGGCAGTTGCACGGAGACCGCCAGTTTCCGTATAGCGTAGGTCTTATGCAGATAGCACCTATTAAGTCAAATACCTATCTAACCTCTAAGCTGGCCACCTATTTCTGGCGGTTGATTAACAGACTATAAGGTTCCAAAGGCTCTGATTCAAGTCCGTTGATATATCTCGTGGCGGGCCCTATAAGACGAAACTCGGAAGTCCTGCCAACTATCTTAGTCTTACCCCTCACCGTCCTGCAGGGAGTTTCCGTGGTGCCATGACACTTGAGAATAAGCTAGGAACCTGTACAGTGTCACCGATAACCTAACGATTGTTTCAGGCCTTTACAAGACTCGGCTTGGTAGGGCCCATCCAATAACATGATACAGGTCTCACCACCTTATACCCGGGATACGGTGACGTAGAAATCAGCCCGTATGATGCCAGCCTGATTTTTTTCGAATCTAGGGTAAGTTTTAGTGTCGGCTGCATTAACGTTTACCCATTAATAAGCAAGGTAGACCCGGATCTTGATCCCGGAATATACACGCGTCGGTGCGCTAGAGGGTCTAGGGGAAATTCAACGGCGAGTGAGCCCTAATAAGACGCGATGGATTGAACTCAGTAGCGTGGGCGATGACAATCTTTAAGACGAGAAGTCGTTCGGTCATATACCTAACGGGTGACGCCGTCTCACAACCGGGCGTTGCCGGGTGTCATCT"

a = 0
c = 0
t = 0
g = 0

for i in s:
    if i == 'A':
        a+=1
    if i == 'C':
        c+=1
    if i == 'T':
        t+=1
    if i == 'G':
        g+=1

print(str(a) + ' '+ str(c) + ' ' +str(g) +' '+ str(t))