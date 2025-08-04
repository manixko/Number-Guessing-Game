import random 

def GenerateNumber(min, max):
    """Generate a random number between min and max."""
    generated_number = random.randint(min, max)
    return generated_number

if __name__ == "__main__":
    print(GenerateNumber(1, 100))
    