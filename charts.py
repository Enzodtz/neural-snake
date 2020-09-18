import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.style.use('dark_background')

def fitnessChart(generation, fitnesses):

    generation_list = [0]
    for i in range(generation):
        generation_list.append(i + 1)

    fig = plt.figure()
    ax = plt.axes()

    ax.set_xlabel('Generation')
    ax.set_ylabel('Fitness')

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    top = max(fitnesses) + 1
    ax.set_ylim(0, top)

    try:
        ax.plot(generation_list, fitnesses);
    except:
        print(generation_list, fitnesses)
        exit()

    plt.savefig('fitnesses')
    plt.close(fig)
    