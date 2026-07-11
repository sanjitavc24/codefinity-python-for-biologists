import matplotlib.pyplot as plt

def plot_gc_content(sequences):
    gc_values = [((seq.count("G") + seq.count("C")) / len(seq)) * 100 for seq in sequences]
    labels = [f"Seq{i+1}" for i in range (len(sequences))]
    
    colors = []
    for gc in gc_values: 
        if gc > 60:
            colors.append("#FF1493")
        elif gc < 30:
            colors.append ("#E76F51")
        else:
            colors.append ("#4361EE")

    plt.figure(figsize = (8,5))
    bars = plt.bar (labels, gc_values, color=colors)
    plt.xlabel("Sequence")
    plt.ylabel("GC content %")
    plt.title ("GC Content Across DNA sequences")
    plt.ylim(0,100)
    plt.show()
sequences = [
    "ATGCGCGTA",
    "ATATATATAT",
    "GGGCCCGGG",
    "TTAACCGGTT",
    "GCGCGCGCGC"
]
plot_gc_content(sequences)
