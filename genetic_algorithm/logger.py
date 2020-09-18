print('\033[2J')

def updateConsole(generation, population, max_score):
    print('\033[1;0H', '-'*40, '   ')
    print('\033[2;0H', 'Generation:', generation, '   ')
    print('\033[3;0H', '-'*40, '   ')
    print('\033[4;0H', 'Element:', population.actual_individual + 1, '/', population.size, '   ')
    print('\033[5;0H', 'Actual Score:', population.individuals[population.actual_individual].fitness, '   ')
    print('\033[6;0H', 'Max Score:', max_score, '   ')