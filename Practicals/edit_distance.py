def edit_distance(a, b):
    if len(a) == 0: return len(b)
    if len(b) == 0: return len(a)

    if a[0] == b[0]:
        return edit_distance(a[1:], b[1:])
    else:
        insert = 1 + edit_distance(a, b[1:])
        delete = 1 + edit_distance(a[1:], b)
        replace = 1 + edit_distance(a[1:], b[1:])
        return min(insert, delete, replace)

# Example usage
word1 = "write"
word2 = "right"

distance = edit_distance(word1, word2)
print(f"Edit distance between '{word1}' and '{word2}' is: {distance}")
