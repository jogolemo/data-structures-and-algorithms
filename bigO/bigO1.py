# nemo = ['nemo']

# everyone = ['dory', 'bruce', 'marlin', 'nemo',
#             'gill', 'bloat', 'nigel', 'squirt',
#             'darla', 'hank']

# large = ['nemo'] * 10000


# def find_nemo(arr):
#     for i in range(len(arr)):
#         if arr[i] == 'nemo':
#             print('Found Nemo!')


# find_nemo(large)  # O(n) --> Linear Time


boxes = [0, 1, 2, 3, 4, 5]


def log_first_two_boxes(boxes):
    print(boxes[0])
    print(boxes[1])


# O(1) --> Constant Time. constant # of operations regardless of size of 'boxes'
log_first_two_boxes(boxes)
