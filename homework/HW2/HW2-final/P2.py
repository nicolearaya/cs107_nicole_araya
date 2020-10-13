def dna_complement(dna):
    if not dna:
        return None
    dna = dna.upper()
    output = ""
    for x in dna:
        if x == "A":
            output = output + "T"
        elif x == "T":
            output = output + "A"
        elif x == "C":
            output = output + "G"
        elif x == "G":
            output = output + "C"
        else:
            return None
    return output

string1 = "ATTAGCCgTATAtaGCA"
print(string1)
print(dna_complement(string1))
string2 = "FEIUBvevonru"
print(string2)
print(dna_complement(string2))

