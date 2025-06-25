import os
print("Current directory:", os.getcwd())
print("Files in RedInstance:", os.listdir(os.path.dirname(__file__)))

from redbot import Red
Red().run()
