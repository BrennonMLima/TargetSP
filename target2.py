def is_fibonacci(n):
    if n < 0:
        return False
    
    a, b = 0, 1
    
    if n == a or n == b:
        return True
    
    while b < n:
        a, b = b, a + b
    
    return b == n

def main():
    num = int(input("Informe um número: "))
    
    if is_fibonacci(num):
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
