def find_motif_positions(sequences, motif):
    results ={}
    for seq in sequences: 
        motif_positions = []
        motif_length = len(motif)
        for i in range(len(seq) - motif_length + 1):
            if seq [i:i+motif_length] == motif:
                motif_positions.append(i)
        results[seq]=motif_positions
    return results

sequences = ["ATGCGATATCG", "GATATATGCATATACTT"]
motif = "ATAT"
motif_positions = find_motif_positions(sequences, motif)
positions_var = motif_positions
print(positions_var)

sequences2 = ["AAAAA", "TTTTT"]
motif2 = "AA"
motif_positions2 = find_motif_positions(sequences2, motif2)
positions_var2 = motif_positions2
print(positions_var2)
