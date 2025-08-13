import random

# Set a seed (optional, for reproducibility)
random.seed(42)

# Generate random integers and floats
print(random.randint(1, 100))     # Random integer between 1 and 100
print(random.random())            # Random float between 0 and 1

import secrets

# Secure random integer
print(secrets.randbelow(100))     # Random int < 100

# Generate a secure random token
print(secrets.token_hex(16))      # 32-character hex string (128 bits)
