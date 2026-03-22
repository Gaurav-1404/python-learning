# 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one? 

# Create first environment
    # python -m venv env1

# Activate it
    # env1\Scripts\activate   # Windows

# Install packages
    # pip install numpy pandas flask

# Save packages
    # pip freeze > requirements.txt

# python -m venv env2
# env2\Scripts\activate

# Install same packages
    # pip install -r requirements.txt