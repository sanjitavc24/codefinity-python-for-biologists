def reverse_complement_batch(sequences):
    output_list=[]
    for seq in sequences:
        seq_upper=seq.upper()
        valid_bases = [b for b in seq_upper if b in "ATGC"]
        clean_seq = "".join(valid_bases)
        if clean_seq == "":
            output_list.append("")
            continue
        complement_table = str.maketrans ("ATCG", "TAGC")
        complement = clean_seq.translate(complement_table)
        reverse_complement = complement[::-1]
        output_list.append(reverse_complement)

    return output_list
        
        
        
# Sample calls
batch1 = ["ATCG", "ggta", "ACGTN", "xyz", "AAGCCTT"]
result1 = reverse_complement_batch(batch1)
print(result1)

batch2 = ["", "NNNN", "AGCTAGC"]
result2 = reverse_complement_batch(batch2)
print(result2)
