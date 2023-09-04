import numpy as np
from sky.plotlib import LinePlot, ContourPlot
from sky.datastructures import Grid

class analytic_model_0():
    def __init__(self, config, logger = None) -> None:
        self.logger = logger
        self.amp = config.amp
        self.freq = config.freq

    def calculate(self, x):

        if self.logger is not None: self.logger.info("Mod 1 started calculation")

        y = self.amp * np.sin(2 * np.pi * self.freq * x)

        if self.logger is not None: self.logger.info("Mod 1 finished calculation \n")

        return y



class analytic_model_1():
    def __init__(self, config, logger = None) -> None:
        self.xlabel = "x"
        self.ylabel = "pressure" 
        self.logger = logger
        self.amp = config.amp
        self.freq = config.freq

    def calculate(self, x, returnType = "numpy"):

        if self.logger is not None: self.logger.info("Mod 1 started calculation")

        y = self.amp * np.sin(2 * np.pi * self.freq * x)

        if self.logger is not None: self.logger.info("Mod 1 finished calculation \n")

        plt = LinePlot(x,y)
        plt.x_label = self.xlabel
        plt.y_label = self.ylabel
        plt.color_no = 0

        if returnType == "plot":
            return plt
        elif returnType == "numpy":
            return y
        

class analytic_model_2():
    def __init__(self, config, logger = None) -> None:
        self.xlabel = "x"
        self.ylabel = "pressure" 
        self.logger = logger
        self.amp = config.amp
        self.amp2 = config.amp2
        self.freq = config.freq

    def calculate(self, x, returnType = "numpy"):

        if self.logger is not None: self.logger.info("Mod 1b started calculation")

        y = np.exp(-0.2*x) * self.amp * np.sin(2 * np.pi * self.freq * x)

        if self.logger is not None: self.logger.info("Mod 1b finished calculation \n")


        plt = LinePlot(x,y, linestyle = "--")
        plt.x_label = self.xlabel
        plt.y_label = self.ylabel

        if returnType == "plot":
            return plt 
        elif returnType == "numpy":
            return y

class analytic_model_3():
    def __init__(self, logger = None) -> None:
        self.xlabel = "x"
        self.ylabel = "y"
        self.logger = logger

    def calculate(self, x, y, returnType = "numpy"):

        if self.logger is not None: self.logger.info("Mod 2 started calculation")

        grid = Grid(x, y)
        y = np.sin(grid.nodes[:,0]) * np.cos(grid.nodes[:,1])

        if self.logger is not None: self.logger.info("Mod 2 finished calculation \n")

        plt = ContourPlot(grid, y)

        if returnType == "plot":
            return plt 
        elif returnType == "numpy":
            return y





    

