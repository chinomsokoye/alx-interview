#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ Given `n` x `n` 2D Matrix
    Rotate it 90 degrees clockwise
    """
    # Replica Matrix
    replica = matrix[:]

    for i in range(len(matrix)):
        # retract column from replica
        column = [row[i] for row in replica]
        # Replace in matrix in reverse order
        matrix[i] = column[::-1]
