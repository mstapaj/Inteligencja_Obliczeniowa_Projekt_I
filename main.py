import time

from Nonogram import Nonogram


def mean(tab):
    return sum(tab) / len(tab)


def measureTimeAndResult(func, args, counter=False):
    tabTimes = []
    tabResults = []
    tabBestSol = []
    solved = 0
    if counter:
        for i in range(100):
            start = time.time()
            temp = func(*args)
            tabTimes.append(time.time() - start)
            tabResults.append(temp['best_solution_generation'])
            tabBestSol.append(temp['solution_fitness'])
            if temp['solution_fitness'] == 0:
                solved += 1
            print(i, "/ 100")
    else:
        for i in range(100):
            start = time.time()
            temp = func(*args)
            tabTimes.append(time.time() - start)
            tabResults.append(temp['best_solution_generation'])
            tabBestSol.append(temp['solution_fitness'])
            if temp['solution_fitness'] == 0:
                solved += 1
    print("Średnia generacja:", mean(tabResults))
    print("Średni czas:", mean(tabTimes))
    print("Średnie najlepsze rozwiązanie:", mean(tabBestSol))
    print("Procent poprawnych rozwiązań:", solved)
    print()


nonogram3x3 = {
    "rows": [[3], [1], [2]],
    "columns": [[3], [1, 1], [1]]
}

nonogram5x5 = {
    "rows": [[3], [1, 3], [1, 1], [2, 1], [1]],
    "columns": [[4], [1], [2], [2], [4]]
}

nonogram7x7 = {
    "rows": [[3], [3], [1, 1], [7], [1, 3], [1, 1], [2, 2]],
    "columns": [[2], [1, 1], [2, 4], [5], [2, 4], [1, 1], [2]]
}

nonogram10x10 = {
    "rows": [[1, 4, 3], [2, 3], [2], [1], [2], [2, 7], [1, 7], [6], [1, 4], [4]],
    "columns": [[2, 2], [1, 1], [1], [3, 2], [9], [2, 4], [5], [1, 5], [1, 5], [1, 5]]
}

nonogram20x20 = {
    "rows": [[5, 1, 3], [6, 1, 3], [7, 9], [15], [4, 1, 10], [2, 4, 3], [2, 1, 1, 3], [1, 5, 3], [1, 8, 1, 1], [8, 8],
             [3, 3, 3], [1, 1, 6, 5], [3, 3, 1, 3], [3, 2, 3], [2, 3], [2, 3, 1, 1, 1], [2, 5, 1, 1, 1], [3, 5], [6, 2],
             [4]],
    "columns": [[3, 5, 7], [3, 3, 6], [3, 1, 2, 2, 1], [5, 2], [4, 3, 2], [3, 3, 1, 1], [3, 3, 2, 4], [1, 5, 5],
                [1, 7, 5],
                [3, 6, 5], [1, 3, 1, 1, 3], [5, 2], [4, 2], [3, 2, 1], [3, 1, 1], [3, 1, 1, 2], [8, 1, 1], [8, 8],
                [3, 11],
                [3, 4, 3]]
}

n3x3 = Nonogram(nonogram3x3['rows'], nonogram3x3['columns'])
n5x5 = Nonogram(nonogram5x5['rows'], nonogram5x5['columns'])
n7x7 = Nonogram(nonogram7x7['rows'], nonogram7x7['columns'])
n10x10 = Nonogram(nonogram10x10['rows'], nonogram10x10['columns'])
n20x20 = Nonogram(nonogram20x20['rows'], nonogram20x20['columns'])

n3x3.runGA("fitness", 100, 100, 12, 50)
n5x5.runGA("fitness", 100, 100, 5, 50)
n7x7.runGA("fitness", 100, 100, 5, 50)
n10x10.runGA("fitness", 100, 100, 5, 50)
n20x20.runGA("fitness", 100, 100, 5, 50)

n3x3.runGA("fitness_tuning", 100, 100, 12, 50)
n5x5.runGA("fitness_tuning", 100, 100, 5, 50)
n7x7.runGA("fitness_tuning", 100, 100, 5, 50)
n10x10.runGA("fitness_tuning", 100, 100, 5, 50)
n20x20.runGA("fitness_tuning", 100, 100, 5, 50)

n3x3.runGA("fitness_another", 100, 100, 15, 50)
n5x5.runGA("fitness_another", 100, 100, 8, 50)
n7x7.runGA("fitness_another", 100, 100, 5, 50)
n10x10.runGA("fitness_another", 100, 100, 5, 50)
n20x20.runGA("fitness_another", 100, 100, 5, 50)

n3x3.runGA("fitness_another_tuning", 100, 100, 34, 50)
n5x5.runGA("fitness_another_tuning", 100, 100, 13, 50)
n7x7.runGA("fitness_another_tuning", 100, 100, 9, 50)
n10x10.runGA("fitness_another_tuning", 100, 100, 7, 50)
n20x20.runGA("fitness_another_tuning", 100, 100, 5, 50)

measureTimeAndResult(n3x3.runGA, ["fitness", 100, 100, 12, 50])
measureTimeAndResult(n3x3.runGA, ["fitness_tuning", 100, 100, 12, 50])
measureTimeAndResult(n3x3.runGA, ["fitness_another", 100, 100, 15, 50])
measureTimeAndResult(n3x3.runGA, ["fitness_another_tuning", 100, 100, 34, 50])

measureTimeAndResult(n5x5.runGA, ["fitness", 100, 100, 5, 50])
measureTimeAndResult(n5x5.runGA, ["fitness_tuning", 100, 100, 5, 50])
measureTimeAndResult(n5x5.runGA, ["fitness_another", 100, 100, 8, 50])
measureTimeAndResult(n5x5.runGA, ["fitness_another_tuning", 100, 100, 13, 50])

measureTimeAndResult(n7x7.runGA, ["fitness", 100, 100, 5, 50])
measureTimeAndResult(n7x7.runGA, ["fitness_tuning", 100, 100, 5, 50])
measureTimeAndResult(n7x7.runGA, ["fitness_another", 100, 100, 5, 50])
measureTimeAndResult(n7x7.runGA, ["fitness_another_tuning", 100, 100, 10, 50])

measureTimeAndResult(n10x10.runGA, ["fitness", 100, 100, 5, 50])
measureTimeAndResult(n10x10.runGA, ["fitness_tuning", 100, 100, 5, 50])
measureTimeAndResult(n10x10.runGA, ["fitness_another", 100, 100, 5, 50])
measureTimeAndResult(n10x10.runGA, ["fitness_another_tuning", 100, 100, 7, 50])

measureTimeAndResult(n20x20.runGA, ["fitness", 100, 100, 5, 50])
measureTimeAndResult(n20x20.runGA, ["fitness_tuning", 100, 100, 5, 50])
measureTimeAndResult(n20x20.runGA, ["fitness_another", 100, 100, 5, 50])
measureTimeAndResult(n20x20.runGA, ["fitness_another_tuning", 100, 100, 5, 50])

n3x3.runSwarm("fitness", 1000, 1.5, 0.8, 0.9, 2, 2)
n3x3.runSwarm("fitness_tuning", 1000, 1.5, 0.8, 0.9, 2, 2)
n3x3.runSwarm("fitness_another", 1000, 0.5, 0.3, 0.9)
n3x3.runSwarm("fitness_another_tuning", 1000, 0.5, 0.3, 0.9)

n5x5.runSwarm("fitness", 1000, 1.5, 0.8, 0.9, 2, 2)
n5x5.runSwarm("fitness_tuning", 1000, 1.5, 0.8, 0.9, 2, 2)
n5x5.runSwarm("fitness_another", 1000, 0.5, 0.3, 0.9)
n5x5.runSwarm("fitness_another_tuning", 1000, 0.5, 0.3, 0.9)

n7x7.runSwarm("fitness", 1000, 1.5, 0.8, 0.9, 2, 2)
n7x7.runSwarm("fitness_tuning", 1000, 1.5, 0.8, 0.9, 2, 2)
n7x7.runSwarm("fitness_another", 1000, 0.5, 0.3, 0.9)
n7x7.runSwarm("fitness_another_tuning", 1000, 0.5, 0.3, 0.9)

n10x10.runSwarm("fitness", 1000, 1.5, 0.8, 0.9, 2, 2)
n10x10.runSwarm("fitness_tuning", 1000, 1.5, 0.8, 0.9, 2, 2)
n10x10.runSwarm("fitness_another", 1000, 0.5, 0.3, 0.9)
n10x10.runSwarm("fitness_another_tuning", 1000, 0.5, 0.3, 0.9)

n20x20.runSwarm("fitness", 1000, 1.5, 0.8, 0.9, 2, 2)
n20x20.runSwarm("fitness_tuning", 1000, 1.5, 0.8, 0.9, 2, 2)
n20x20.runSwarm("fitness_another", 1000, 0.5, 0.3, 0.9)
n20x20.runSwarm("fitness_another_tuning", 1000, 0.5, 0.3, 0.9)

measureTimeAndResult(n3x3.runSwarm, ['fitness', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n3x3.runSwarm, ['fitness_tuning', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n3x3.runSwarm, ['fitness_another', 1000, 0.5, 0.3, 0.9])
measureTimeAndResult(n3x3.runSwarm, ['fitness_another_tuning', 1000, 0.5, 0.3, 0.9])

measureTimeAndResult(n5x5.runSwarm, ['fitness', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n5x5.runSwarm, ['fitness_tuning', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n5x5.runSwarm, ['fitness_another', 1000, 0.5, 0.3, 0.9])
measureTimeAndResult(n5x5.runSwarm, ['fitness_another_tuning', 1000, 0.5, 0.3, 0.9])

measureTimeAndResult(n7x7.runSwarm, ['fitness', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n7x7.runSwarm, ['fitness_tuning', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n7x7.runSwarm, ['fitness_another', 1000, 0.5, 0.3, 0.9])
measureTimeAndResult(n7x7.runSwarm, ['fitness_another_tuning', 1000, 0.5, 0.3, 0.9])

measureTimeAndResult(n10x10.runSwarm, ['fitness', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n10x10.runSwarm, ['fitness_tuning', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n10x10.runSwarm, ['fitness_another', 1000, 0.5, 0.3, 0.9])
measureTimeAndResult(n10x10.runSwarm, ['fitness_another_tuning', 1000, 0.5, 0.3, 0.9])

measureTimeAndResult(n20x20.runSwarm, ['fitness', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n20x20.runSwarm, ['fitness_tuning', 1000, 1.5, 0.8, 0.9, 2, 2])
measureTimeAndResult(n20x20.runSwarm, ['fitness_another', 1000, 0.5, 0.3, 0.9])
measureTimeAndResult(n20x20.runSwarm, ['fitness_another_tuning', 1000, 0.5, 0.3, 0.9])
