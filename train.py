def train(rows):
    """Toy training function: returns the mean of the values."""
    return sum(rows) / len(rows)


if __name__ == "__main__":
    print(train([1, 2, 3]))
