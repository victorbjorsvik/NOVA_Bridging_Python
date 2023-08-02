def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def genPrimes():
    prime_1 = 2
    next = 2
    p = [prime_1]

    while True:
        if is_prime(next):
            yield next
            next += 1
            p.append(next)
        else:
           next += 1

n = int(input("How many primes? "))
i = 0
primes = genPrimes()

while n != 0:
    for i in range(n):
        print(primes.__next__())
    n = int(input("How many primes? "))

print("Have a nice day!")