import pyjokes
import os
# 1. print multiple lines
print('''Morning sun begins to rise,
Painting gold across the skies.
      
Soft winds whisper through the trees,
Dancing gently with the breeze.
      
Dreams awake with hopeful light,
Turning darkness into bright.''')

# 2. print table of 5 using REPL(read evaluate print loop)
for i in range(1, 11):
    print("5 x", i, "=", 5*i)

# 3. install a module and use of it
jokes = pyjokes.get_joke()
print(jokes)

# 4. print content of a directory using os module
path = r"c:\Users\gaura\OneDrive\Desktop\python"
path2 = "c:\\Users\\gaura\\OneDrive\\Desktop\\python"
files = os.listdir(path)
for file in files:
    print(file)