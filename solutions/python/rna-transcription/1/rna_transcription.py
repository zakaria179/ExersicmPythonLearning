def to_rna(dna_strand):
    dna='ACGT'
    rna='UGCA'
    rna_complement=""
    for nucleotide in  dna_strand :
        if nucleotide==dna[0]:
            rna_complement+=rna[0]
        elif nucleotide==dna[1]:
            rna_complement+=rna[1]
        elif nucleotide==dna[2]:
            rna_complement+=rna[2]
        elif nucleotide==dna[3]:
            rna_complement+=rna[3]
    return rna_complement
            
        
