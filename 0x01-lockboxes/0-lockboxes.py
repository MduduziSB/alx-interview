#!/usr/bin/python3
"""
Method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, false otherwise
    """
    maxNumberOfKeys = len(boxes)
    keys = [0]

    for check in keys:
        for key in boxes[check]:
            if key < maxNumberOfKeys and key not in keys:
                keys.append(key)

    return len(keys) == maxNumberOfKeys
