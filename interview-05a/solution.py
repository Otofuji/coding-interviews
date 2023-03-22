def longest_sequence(n: int) -> int:
    binary = bin(n)[2:]  # convert n to binary string
    prev_len = curr_len = max_len = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            curr_len += 1
        else:
            # update max_len if flipping this bit results in a longer sequence of 1s
            max_len = max(max_len, prev_len + curr_len + 1)
            prev_len, curr_len = curr_len, 0
    # edge case: if the last bit is 1, we need to update max_len one last time
    max_len = max(max_len, prev_len + curr_len + 1) if curr_len > 0 else max_len
    return max_len
