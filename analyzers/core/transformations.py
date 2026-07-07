def first_differences(sequence):
    if len(sequence) < 2:
        return []
    first_difference_sequence = []
    for i in range(0,len(sequence)-1):
        first_difference_sequence.append(sequence[i+1]-sequence[i])
    return first_difference_sequence

def nth_differences(sequence,n):
    if len(sequence) < 2:
        return []
    changing_sequence = sequence
    for _ in range(n):
        changing_sequence = first_differences(changing_sequence)
    return changing_sequence

def first_ratios(sequence):
    if len(sequence) < 2:
        return []
    ratios = []
    for i in range(len(sequence)-1):
        if sequence[i] == 0:
            ratios.append(None)
        else:
            ratios.append((sequence[i+1])/(sequence[i]))
    return ratios

def subtract_sequences(Seq1,Seq2):
    subSeq = []
    for i in range(len(Seq1)):
        subSeq.append(Seq1[i]-Seq2[i])
    return subSeq