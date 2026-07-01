def amino_acid_compositions(sequences):
    valid_aa = set("ACDEFGHIKLMNPQRSTVWY")
    compositions = []
    for seq in sequences:
        seq_upper=seq.upper()
        aa_counts ={}
        total = 0
        for aa in seq_upper:
            if aa in valid_aa:
                aa_counts[aa]=aa_counts.get(aa,0)+1
                total += 1
        if total == 0:
            compositions.append({})
            continue
            
        comp_dict = {}
        for aa in aa_counts:
            percent = (aa_counts[aa] / total) * 100
            comp_dict[aa] = percent
        compositions.append(comp_dict)
    return compositions
            

# Sample calls
seqs = [
    "MKTIIALSYIFCLVFADYKDDDDA",
    "GAVLIPFYWSTCMNQDEKRH",
    "MXXKZZ",
    ""
]
result = amino_acid_compositions(seqs)
for i, res in enumerate(result):
    print(f"Sequence {i+1} composition: {res}\n")
