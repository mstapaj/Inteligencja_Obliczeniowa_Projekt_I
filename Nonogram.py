import math
import numpy as np
import pygad
import pyswarms as ps


def arrayEquals(tab1, tab2):
    if len(tab1) != len(tab2):
        return False
    for i in range(len(tab1)):
        if tab1[i] != tab2[i]:
            return False
    return True


class Nonogram:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def runGA(self, fitness_func, generations, sol_per_pop, mutation_percent_genes, num_parents_mating):
        def fitness(solution, solution_idx):
            resultRow = []
            resultCol = []
            solution = [solution[i:i + len(self.rows)] for i in range(0, len(solution), len(self.rows))]
            for i in solution:
                counter = 0
                temp = []
                for j in i:
                    if j == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultRow.append(temp)
            for i in range(len(solution[0])):
                counter = 0
                temp = []
                for j in range(len(solution[i])):
                    if solution[j][i] == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultCol.append(temp)
            wrongCounter = 0
            for i in range(len(self.rows)):
                if not arrayEquals(self.rows[i], resultRow[i]):
                    wrongCounter -= 1
                if not arrayEquals(self.cols[i], resultCol[i]):
                    wrongCounter -= 1
            return wrongCounter

        def fitness_tuning(solution, solution_idx):
            resultRow = []
            resultCol = []
            solution = [solution[i:i + len(self.rows)] for i in range(0, len(solution), len(self.rows))]
            for i in solution:
                counter = 0
                temp = []
                for j in i:
                    if j == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultRow.append(temp)
            for i in range(len(solution[0])):
                counter = 0
                temp = []
                for j in range(len(solution[i])):
                    if solution[j][i] == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultCol.append(temp)
            wrongCounter = 0
            for i in range(len(self.rows)):
                if len(self.rows[i]) == len(resultRow[i]):
                    for j in range(len(self.rows[i])):
                        if self.rows[i][j] != resultRow[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.rows[i]) - len(resultRow[i]))
                    if len(self.rows[i]) > len(resultRow[i]):
                        for j in range(len(resultRow[i])):
                            if self.rows[i][j] != resultRow[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.rows[i])):
                            if self.rows[i][j] != resultRow[i][j]:
                                wrongCounter -= 1
                if len(self.cols[i]) == len(resultCol[i]):
                    for j in range(len(self.cols[i])):
                        if self.cols[i][j] != resultCol[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.cols[i]) - len(resultCol[i]))
                    if len(self.cols[i]) > len(resultCol[i]):
                        for j in range(len(resultCol[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.cols[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
            return wrongCounter

        def fitness_another(solution, solution_idx):
            tab = [[0 for i in range(len(self.cols))] for j in range(len(self.rows))]
            iterator = 0
            wrongCounter = 0
            solution = solution.astype(int)
            for i in range(len(self.rows)):
                for j in range(len(self.rows[i])):
                    for k in range(self.rows[i][j]):
                        if solution[iterator] + k < len(self.rows):
                            tab[i][solution[iterator] + k] = 1
                        else:
                            wrongCounter -= 1
                    iterator += 1
            for i in range(len(self.cols)):
                for j in range(len(self.cols[i])):
                    for k in range(self.cols[i][j]):
                        if solution[iterator] + k < len(self.cols):
                            tab[solution[iterator] + k][i] = 1
                        else:
                            wrongCounter -= 1
                    iterator += 1
            resultRow = []
            resultCol = []
            solution = tab
            for i in solution:
                counter = 0
                temp = []
                for j in i:
                    if j == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultRow.append(temp)
            for i in range(len(solution[0])):
                counter = 0
                temp = []
                for j in range(len(solution[i])):
                    if solution[j][i] == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultCol.append(temp)
            for i in range(len(self.rows)):
                if len(self.rows[i]) == len(resultRow[i]):
                    for j in range(len(self.rows[i])):
                        if self.rows[i][j] != resultRow[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.rows[i]) - len(resultRow[i]))
                    if len(self.rows[i]) > len(resultRow[i]):
                        for j in range(len(resultRow[i])):
                            if self.rows[i][j] != resultRow[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.rows[i])):
                            if self.rows[i][j] != resultRow[i][j]:
                                wrongCounter -= 1
                if len(self.cols[i]) == len(resultCol[i]):
                    for j in range(len(self.cols[i])):
                        if self.cols[i][j] != resultCol[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.cols[i]) - len(resultCol[i]))
                    if len(self.cols[i]) > len(resultCol[i]):
                        for j in range(len(resultCol[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.cols[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
            return wrongCounter

        def fitness_another_tuning(solution, solution_idx):
            tab = [[0 for i in range(len(self.cols))] for j in range(len(self.rows))]
            iterator = 0
            wrongCounter = 0
            solution = solution.astype(int)
            for i in range(len(self.rows)):
                for j in range(len(self.rows[i])):
                    for k in range(self.rows[i][j]):
                        if solution[iterator] + k < len(self.rows):
                            tab[i][solution[iterator] + k] = 1
                        else:
                            wrongCounter -= 1
                    iterator += 1
            resultCol = []
            solution = tab
            for i in range(len(solution[0])):
                counter = 0
                temp = []
                for j in range(len(solution[i])):
                    if solution[j][i] == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultCol.append(temp)
            for i in range(len(self.cols)):
                if len(self.cols[i]) == len(resultCol[i]):
                    for j in range(len(self.cols[i])):
                        if self.cols[i][j] != resultCol[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.cols[i]) - len(resultCol[i]))
                    if len(self.cols[i]) > len(resultCol[i]):
                        for j in range(len(resultCol[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.cols[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
            return wrongCounter

        gene_space = [0, 1]
        num_genes = len(self.rows) * len(self.cols)

        if fitness_func == "fitness":
            fitness_function = fitness
        elif fitness_func == "fitness_tuning":
            fitness_function = fitness_tuning
        elif fitness_func == "fitness_another":
            fitness_function = fitness_another
            gene_space = [i for i in range(len(self.rows))]
            num_genes = 0
            for i in range(len(self.rows)):
                num_genes += len(self.rows[i])
                num_genes += len(self.cols[i])
        elif fitness_func == "fitness_another_tuning":
            fitness_function = fitness_another_tuning
            gene_space = [i for i in range(len(self.rows))]
            num_genes = 0
            for i in range(len(self.rows)):
                num_genes += len(self.rows[i])

        num_generations = generations
        keep_parents = 2

        parent_selection_type = "sss"

        crossover_type = "single_point"

        mutation_type = "random"

        ga_instance = pygad.GA(gene_space=gene_space,
                               num_generations=num_generations,
                               num_parents_mating=num_parents_mating,
                               fitness_func=fitness_function,
                               sol_per_pop=sol_per_pop,
                               num_genes=num_genes,
                               parent_selection_type=parent_selection_type,
                               keep_parents=keep_parents,
                               crossover_type=crossover_type,
                               mutation_type=mutation_type,
                               mutation_percent_genes=mutation_percent_genes)

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()

        toReturn = {
            "best_solution_generation": ga_instance.best_solution_generation,
            "solution_fitness": solution_fitness,
        }
        return toReturn

    def runSwarm(self, fitness_func, generations, c1, c2, w, k=None, p=None):
        def fitness(temp):
            resultRow = []
            resultCol = []
            solution = []
            for i in temp:
                solution.append(i[0])
            solution = [solution[i:i + len(self.rows)] for i in range(0, len(solution), len(self.rows))]
            for i in solution:
                counter = 0
                temp = []
                for j in i:
                    if j == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultRow.append(temp)
            for i in range(len(solution[0])):
                counter = 0
                temp = []
                for j in range(len(solution[i])):
                    if solution[j][i] == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultCol.append(temp)
            wrongCounter = 0
            for i in range(len(self.rows)):
                if not arrayEquals(self.rows[i], resultRow[i]):
                    wrongCounter -= 1
                if not arrayEquals(self.cols[i], resultCol[i]):
                    wrongCounter -= 1
            return -wrongCounter

        def fitness_tuning(temp):
            resultRow = []
            resultCol = []
            solution = []
            for i in temp:
                solution.append(i[0])
            solution = [solution[i:i + len(self.rows)] for i in range(0, len(solution), len(self.rows))]
            for i in solution:
                counter = 0
                temp = []
                for j in i:
                    if j == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultRow.append(temp)
            for i in range(len(solution[0])):
                counter = 0
                temp = []
                for j in range(len(solution[i])):
                    if solution[j][i] == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultCol.append(temp)
            wrongCounter = 0
            for i in range(len(self.rows)):
                if len(self.rows[i]) == len(resultRow[i]):
                    for j in range(len(self.rows[i])):
                        if self.rows[i][j] != resultRow[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.rows[i]) - len(resultRow[i]))
                    if len(self.rows[i]) > len(resultRow[i]):
                        for j in range(len(resultRow[i])):
                            if self.rows[i][j] != resultRow[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.rows[i])):
                            if self.rows[i][j] != resultRow[i][j]:
                                wrongCounter -= 1
                if len(self.cols[i]) == len(resultCol[i]):
                    for j in range(len(self.cols[i])):
                        if self.cols[i][j] != resultCol[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.cols[i]) - len(resultCol[i]))
                    if len(self.cols[i]) > len(resultCol[i]):
                        for j in range(len(resultCol[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.cols[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
            return -wrongCounter

        def fitness_another(solution):
            tab = [[0 for i in range(len(self.cols))] for j in range(len(self.rows))]
            iterator = 0
            wrongCounter = 0
            temp = []
            solution = solution.astype(int)
            for i in solution:
                temp.append(i[0])
            solution = temp
            for i in range(len(self.rows)):
                for j in range(len(self.rows[i])):
                    for k in range(self.rows[i][j]):
                        if solution[iterator] + k < len(self.rows):
                            tab[i][solution[iterator] + k] = 1
                        else:
                            wrongCounter -= 1
                    iterator += 1
            for i in range(len(self.cols)):
                for j in range(len(self.cols[i])):
                    for k in range(self.cols[i][j]):
                        if solution[iterator] + k < len(self.cols):
                            tab[solution[iterator] + k][i] = 1
                        else:
                            wrongCounter -= 1
                    iterator += 1
            resultRow = []
            resultCol = []
            solution = tab
            for i in solution:
                counter = 0
                temp = []
                for j in i:
                    if j == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultRow.append(temp)
            for i in range(len(solution[0])):
                counter = 0
                temp = []
                for j in range(len(solution[i])):
                    if solution[j][i] == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultCol.append(temp)
            for i in range(len(self.rows)):
                if len(self.rows[i]) == len(resultRow[i]):
                    for j in range(len(self.rows[i])):
                        if self.rows[i][j] != resultRow[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.rows[i]) - len(resultRow[i]))
                    if len(self.rows[i]) > len(resultRow[i]):
                        for j in range(len(resultRow[i])):
                            if self.rows[i][j] != resultRow[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.rows[i])):
                            if self.rows[i][j] != resultRow[i][j]:
                                wrongCounter -= 1
                if len(self.cols[i]) == len(resultCol[i]):
                    for j in range(len(self.cols[i])):
                        if self.cols[i][j] != resultCol[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.cols[i]) - len(resultCol[i]))
                    if len(self.cols[i]) > len(resultCol[i]):
                        for j in range(len(resultCol[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.cols[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
            return -wrongCounter

        def fitness_another_tuning(solution):
            tab = [[0 for i in range(len(self.cols))] for j in range(len(self.rows))]
            iterator = 0
            wrongCounter = 0
            temp = []
            solution = solution.astype(int)
            for i in solution:
                temp.append(i[0])
            solution = temp
            for i in range(len(self.rows)):
                for j in range(len(self.rows[i])):
                    for k in range(self.rows[i][j]):
                        if solution[iterator] + k < len(self.rows):
                            tab[i][solution[iterator] + k] = 1
                        else:
                            wrongCounter -= 1
                    iterator += 1
            resultCol = []
            solution = tab
            for i in range(len(solution[0])):
                counter = 0
                temp = []
                for j in range(len(solution[i])):
                    if solution[j][i] == 1:
                        counter += 1
                    elif counter != 0:
                        temp.append(counter)
                        counter = 0
                if counter != 0:
                    temp.append(counter)
                resultCol.append(temp)
            for i in range(len(self.cols)):
                if len(self.cols[i]) == len(resultCol[i]):
                    for j in range(len(self.cols[i])):
                        if self.cols[i][j] != resultCol[i][j]:
                            wrongCounter -= 1
                else:
                    wrongCounter -= math.fabs(len(self.cols[i]) - len(resultCol[i]))
                    if len(self.cols[i]) > len(resultCol[i]):
                        for j in range(len(resultCol[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
                    else:
                        for j in range(len(self.cols[i])):
                            if self.cols[i][j] != resultCol[i][j]:
                                wrongCounter -= 1
            return -wrongCounter

        options = {'c1': c1, 'c2': c2, 'w': w, 'k': k, 'p': p}
        if fitness_func == "fitness" or fitness_func == "fitness_tuning":
            if fitness_func == "fitness":
                fitness_func = fitness
            elif fitness_func == "fitness_tuning":
                fitness_func = fitness_tuning

            n = len(self.rows) * len(self.cols)
            optimizer = ps.discrete.BinaryPSO(n_particles=n, dimensions=1, options=options)

            toReturn = {
                "best_solution_generation": None,
                "solution_fitness": None,
            }

            stats = optimizer.optimize(fitness_func, iters=generations, verbose=False)

            cost_history = optimizer.cost_history

            toReturn['solution_fitness'] = optimizer.cost_history[len(optimizer.cost_history) - 1]
            for i in range(len(cost_history)):
                if cost_history[i] == toReturn['solution_fitness']:
                    toReturn['best_solution_generation'] = i
                    break
            return toReturn
        else:
            limiter = None
            num_genes = None
            if fitness_func == "fitness_another":
                fitness_func = fitness_another
                limiter = len(self.rows)
                num_genes = 0
                for i in range(len(self.rows)):
                    num_genes += len(self.rows[i])
                    num_genes += len(self.cols[i])
            elif fitness_func == "fitness_another_tuning":
                fitness_func = fitness_another_tuning
                limiter = len(self.rows)
                num_genes = 0
                for i in range(len(self.rows)):
                    num_genes += len(self.rows[i])

            options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

            max_bound = limiter * np.ones(1)
            min_bound = 0 * np.ones(1)
            bounds = (min_bound, max_bound)

            optimizer = ps.single.GlobalBestPSO(n_particles=num_genes, dimensions=1,
                                                options=options, bounds=bounds)

            toReturn = {
                "best_solution_generation": None,
                "solution_fitness": None,
            }

            stats = optimizer.optimize(fitness_func, iters=generations, verbose=False)

            cost_history = optimizer.cost_history

            toReturn['solution_fitness'] = optimizer.cost_history[len(optimizer.cost_history) - 1]
            for i in range(len(cost_history)):
                if cost_history[i] == toReturn['solution_fitness']:
                    toReturn['best_solution_generation'] = i
                    break
            return toReturn
