
from problems import problems, functions, solutions

incorrect = lambda n: not functions[n]() == solutions[n] != None
incorrect_ns = set(filter(incorrect, functions.keys()))

solved_ns = sorted(list(functions.keys() - incorrect_ns))
n_solved = len(solved_ns)

print('Problems solved:', solved_ns)
print('Number of problems solved:', n_solved)
print('Incorrect solutions #:', incorrect_ns if incorrect_ns else None)