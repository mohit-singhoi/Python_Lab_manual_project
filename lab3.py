#Q.3 Create Python functions for mathematical operations and demonstrate reading/writing files.


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# --- Main Program ---
def main():
    x, y = 20, 5   # sample numbers

    results = [
        f"Addition of {x} and {y}: {add(x, y)}",
        f"Subtraction of {x} and {y}: {subtract(x, y)}",
        f"Multiplication of {x} and {y}: {multiply(x, y)}",
        f"Division of {x} and {y}: {divide(x, y)}"
    ]

    # --- Writing results to file ---
    with open("results.txt", "w") as f:
        for line in results:
            f.write(line + "\n")

    print("Results written to results.txt")

    # --- Reading results back ---
    with open("results.txt", "r") as f:
        content = f.read()
        print("\nReading results back from file:\n")
        print(content)


# Run the program
if __name__ == "__main__":
    main()
