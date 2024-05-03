#!/usr/bin/env python3

#this file contains all subroutines coded during algorithm exercises in cogniterra course: Bioinformatics algorithms

import sys

# Insert your PatternCount function here, along with any subroutines you need
def pattern_count(text: str, pattern: str) -> int:
    count=0
    for i in range(0,len(text)-len(pattern)+1):
        if text[i:i+len(pattern)]==pattern:
                count+=1
    return count

def FrequencyTable(text: str, k: int) -> dict:
    freqMap = {}
    for i in range(0,len(text)-k+1):
        kmer=text[i:i+k]
        freqMap[kmer]= pattern_count(text,kmer)
    return freqMap

def MaxMap(freqMap: dict) -> int:
    freqMap_max = max(freqMap.values())
    return freqMap_max    

def frequent_words(text: str, k: int) -> list[str]:
    """Find the most frequent k-mers in a given text."""
    FrequentPatterns = [] #array of strings of length zero
    freqMap = FrequencyTable(text, k)
    freqMap_max = MaxMap(freqMap)
    #print(f"the max value is {freqMap_max}")
    for pattern in freqMap.keys():
        if freqMap[pattern] == freqMap_max:
            FrequentPatterns.append(pattern)
    return FrequentPatterns


# Insert your reverse_complement function here, along with any subroutines you need
def reverse_complement(pattern: str) -> str:
    """Calculate the reverse complement of a DNA pattern."""
    rev = pattern[::-1]
    nuc_table= str.maketrans("ACGT","TGCA")
    rev_compl=rev.translate(nuc_table)
    return rev_compl

# Insert your pattern_matching function here, along with any subroutines you need
def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Find all occurrences of a pattern in a genome."""
    pos=[]
    for i in range(0,len(genome)):
        if genome[i:i+len(pattern)] == pattern:
            pos.append(i)
    return pos

# Insert your find_clumps function here, along with any subroutines you need
def find_clumps(genome: str, k: int, l: int, t: int) -> list[str]:
    """Find patterns forming clumps in a genome."""
    pass

# Insert your MinimumSkew function here, along with any subroutines you need
def minimum_skew(genome: str) -> list[int]:
    """Find positions in a genome where the skew diagram attains a minimum."""
    pass

# Insert your hamming_distance function here, along with any subroutines you need
def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    ham=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            ham += 1
    return ham

def approximate_pattern_matching(pattern: str, text: str, d: int) -> list[int]:
    """Find all starting positions where Pattern appears as a substring of Text with at most d mismatches."""
    kmer=len(pattern)
    indexes = []
    for i in range(len(text)-len(pattern)+1):
        if hamming_distance(text[i:i+kmer],pattern) <= d:
            indexes.append(i)
    return indexes

