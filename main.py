import random
import numpy as np



def generate_alignment_matrix(seq1, seq2, match_score, mismatch_score):
    matrix = [[0 for j in range(len(seq2)+1)] for i in range(len(seq1)+1)]
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            diagonal_score = matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], diagonal_score)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Function to perform the traceback and return the alignments
def traceback(seq1, seq2, matrix, match_score, mismatch_score):
    align1, align2 = '', ''
    i, j = len(seq1), len(seq2)
    while i > 0 and j > 0:
        score = matrix[i][j]
        diagonal_score = matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
        if score == diagonal_score:
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif score == matrix[i-1][j]:
            align1 += seq1[i-1]
            align2 += '-'
            i -= 1
        else:
            align1 += '-'
            align2 += seq2[j-1]
            j -= 1
    return align1[::-1], align2[::-1]


#generating a random sequence
def sequence_generate():
    chars = ['A','C','G','T']
    S1 = ''.join([random.choice(chars) for i in range(16)])
    S2 = ''.join([random.choice(chars) for i in range(16)])
    return S1,S2

match_score = 5
mismatch_score = -4


print("The sequences are:\n")
S1,S2 = sequence_generate()
print(f'S1:{S1}\nS2:{S2}\n')

matrix = generate_alignment_matrix(S1,S2, match_score, mismatch_score)
align1, align2 = traceback(S1,S2, matrix, match_score, mismatch_score)

print_matrix(matrix)

print('Alignment 1:', align1)
print('Alignment 2:', align2)
