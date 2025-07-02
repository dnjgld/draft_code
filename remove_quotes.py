def remove_quotes(s):
    return s.replace('"', '').replace("'", "")

# 示例
s = "['babacbbac', 'bacbabacb', 'bacbbacba', 'cbabacbba', 'bbacbabac', 'abacbbacb', 'cbbacbaba', 'acbabacbb', 'acbbacbab'] sorted_L: ['abacbbacb', 'acbabacbb', 'acbbacbab', 'babacbbac', 'bacbabacb', 'bacbbacba', 'bbacbabac', 'cbabacbba', 'cbbacbaba']"
print(remove_quotes(s))
