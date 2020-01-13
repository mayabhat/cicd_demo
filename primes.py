import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)

@profile
def primes(start, end):
    primes = []
    nb_primes = 0

    for val in range(start, end + 1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                primes.append(val)
                nb_primes += 1

    return nb_primes

nb_primes = primes(0, 1000)
print(nb_primes)
