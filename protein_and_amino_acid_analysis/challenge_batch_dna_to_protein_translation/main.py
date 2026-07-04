def batch_translate_dna_to_protein(dna_sequences):
    codon_table = {
        "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
        "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
        "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
        "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
        "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
        "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
        "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
        "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
        "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
        "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
        "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
        "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
        "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
        "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
        "TAC":"Y", "TAT":"Y", "TAA":"_", "TAG":"_",
        "TGC":"C", "TGT":"C", "TGA":"_", "TGG":"W",
    }
    protein_results = []
    for dna_seq  in dna_sequences:
        protein_seq = ""
        for i in range (0, len(dna_seq)-2, 3):
            codon = dna_seq [i:i+3]
            amino_acid = codon_table.get(codon, "X")
            if amino_acid == "_":
                break
            protein_seq += amino_acid
        protein_results.append(protein_seq)
    return protein_results 
    

# Sample calls
print(batch_translate_dna_to_protein(["ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]))
print(batch_translate_dna_to_protein(["ATGTACTAA", "ATGCGT"]))
print(batch_translate_dna_to_protein(["ATGAAATGA", "ATGTTTGGGCCC"]))
