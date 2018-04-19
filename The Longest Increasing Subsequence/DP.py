# 方法

def findsequence(sequence):
    partial_result = []
    max_collection = []
    index = 1
    while index <= len(sequence):
        if (index < len(sequence)) and (sequence[index] > sequence[index - 1]):
            if len(partial_result) == 0:
                partial_result.append(sequence[index - 1])
            partial_result.append(sequence[index])
        else:
            if len(partial_result) > len(max_collection):
                max_collection = []
                for item in partial_result:
                    max_collection.append(item)
            partial_result = []
        index = index + 1
    return max_collection


if __name__ == '__main__':
    sequence = [-1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 10, 1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 56]
    print(findsequence(sequence))