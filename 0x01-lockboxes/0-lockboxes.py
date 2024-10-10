#!/usr/bin/python3

"""
Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    lock boxes
    """

    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True
    keys = [0]  # Start with the key to the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < len(boxes) and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys.append(key)

    return all(unlocked_boxes)
