# datatest.py
# Dataset untuk simulasi Deadlock Detection (5 proses, 3 resource)

processes = ["P1", "P2", "P3", "P4", "P5"]

# Allocation matrix: resource yang sedang dipakai
allocation = [
    [0, 1, 0],  # P1
    [2, 0, 0],  # P2
    [3, 0, 3],  # P3
    [2, 1, 1],  # P4
    [0, 0, 2],  # P5
]

# Request/Need matrix: resource tambahan yang masih dibutuhkan
request = [
    [0, 0, 1],  # P1
    [1, 0, 1],  # P2
    [0, 0, 0],  # P3
    [0, 1, 0],  # P4
    [0, 0, 1],  # P5
]

# Resource yang tersedia
available = [1, 0, 0]