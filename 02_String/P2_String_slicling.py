# Normal slicing
word = "amazing"
print("Normal slicing:")
print("word[0:4] ->", word[0:4])  # 'amaz'
print("word[2:6] ->", word[2:6])  # 'azin'

# Skip slicing (using step)
print("\nSkip slicing:")
print("word[0:7:2] ->", word[0:7:2])  # 'aain'
print("word[1:6:2] ->", word[1:6:2])  # 'mzn'

# Slicing from start to end
print("\nFull word slicing:")
print("word[:] ->", word[:])  # 'amazing'
print("word[::2] ->", word[::2])  # 'aaiig'