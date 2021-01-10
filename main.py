
def is_all_strings(iterable):
    return all([type(item) == str for item in iterable])


print(is_all_strings(["a", "b", "c"]))
print(is_all_strings([23, "hello", "man"]))

