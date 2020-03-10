import matplotlib.pyplot as plt
import numpy as np

class Plot():
    def __init__(self):
        pass

    def basicPlot(self, df, x, y):
        plt.plot(df[x], df[y])
        self.show()


    # Plots a nice looking plot that 
    # is far better to look at
    def coolPlot(self, df, x, y, title):
        fig = plt.figure()

        ax = fig.add_subplot(111)

        ax.plot(df[x], df[y])

        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title)

        plt.xticks(np.arange(0, len(df[y]), step=len(df[y]) // 4))

        for axis in ['top', 'right']:
            ax.spines[axis].set_visible(False)

        ax.yaxis.tick_left()
        ax.xaxis.tick_bottom()

        self.show()

    def show(self):
        plt.show()