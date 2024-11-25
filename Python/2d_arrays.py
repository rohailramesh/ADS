first_year = ["PRP", "ISA", "CSN"]
second_year = ["SWE", "GUI", "IPA"]
third_year = ["CCA", "BDT", "WBP"]

# print(first_year)
ug_degree = [first_year, second_year, third_year]
for year in ug_degree:
    for modules in year:
        print(modules, end=" ")
    print()

rows = len(ug_degree)
cols = len(ug_degree[0])
print(rows)
print(cols)

def find_common_element(two_d_array):
    count_element = {}
    for nums in two_d_array:
        for num in nums:
            if num in count_element:
                count_element[num] +=1
            else:
                count_element[num] = 1
    common_elements_ls = []
    max_freq = max(count_element.values())
    print(max_freq)
    for common_num, freq in count_element.items():
        if freq == max_freq:
            common_elements_ls.append(common_num)
    return common_elements_ls

two_d_array = [
    [1, 2, 3],
    [2, 2, 2],
    [3, 3, 3]
]
print(find_common_element(two_d_array))