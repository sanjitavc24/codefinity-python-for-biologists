def gc_content_batch(sequences):
    # Write your code here
    gc_percents=[]
    for seq in sequences: 
        seq=seq.upper()
        valid_bases = [b for b in seq if b in "ATGC"]
        total=len(valid_bases)
        gc_count=sum(1 for b in valid_bases if b in "GC")
        if total == 0:
            gc_percent = 0.0
        else: 
            gc_percent = (gc_count/total) * 100
        gc_percents.append(gc_percent)
    return gc_percents
sequences = ["ATGCGC", "atttggc", "NNNNNN", "GATTACA", "CGCGCG"]
results = gc_content_batch(sequences)
print(results)
