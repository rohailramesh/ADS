def find_mode(array):
    count = {}
    modes = []
    for num in array:
        count[num] = 1 + count.get(num, 0)
    max_freq = max(count.values())
    for num, freq in count.items():
        if freq == max_freq:
            modes.append(num)
array = [2,2,1,2,2,1,1,1]
find_mode(array)