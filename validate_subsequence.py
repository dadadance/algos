"""
Given two non-empty arrays of integers, write a funciton that
determines whether the second array is a subsequence of the
first one.

A subsequence of an array is a set of numbers that aren't
necessarily adjacent in the array but that are in the same order
as they appear in the array. For instance, the numbers [1,3,4] form a
subsequence of the array [1,2,3,4], and so do the numbers [2,4]. Note that
a single number in an array and the array itself are both valid subsequences of the array.

{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [1, 6, -1, 10]
}

{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 25, 6, -1, 8, 10]
}

{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 6, -1, 8, 10]
}

"""


def isValidSubsequence(arr, seq):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(arr) and seqIdx < len(seq):
        if arr[arrIdx] == seq[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(seq)


def is_valid_subsequence(arr, seq):
    arr_idx = 0
    seq_idx = 0
    while arr_idx < len(arr) and seq_idx < len(seq):
        if arr[arr_idx] == seq[seq_idx]:
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(seq)


def is_valid_subsequence_00(array, sequence):
    seq_idx = 0
    for value in array:
        if seq_idx == len(sequence):
            break
        if value == sequence[seq_idx]:
            seq_idx += 1
    return seq_idx == len(sequence)


if __name__ == '__main__':
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    # sequence = [5, 1, 22, 6, -1, 8, 10]
    sequence = [22, 25, 6]
    print(is_valid_subsequence_00(array, sequence))
