def generate_fibonacci(limit):
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] <= limit:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def count_fibonacci_frequency(start, end):
    fib_sequence = generate_fibonacci(end)
    count = 0
    for num in fib_sequence:
        if start <= num <= end:
            count += 1
    return count

# Example usage:
start_range = 1
end_range = 1000
frequency = count_fibonacci_frequency(start_range, end_range)
print(f"The frequency of Fibonacci numbers between {start_range} and {end_range} is {frequency}.")
