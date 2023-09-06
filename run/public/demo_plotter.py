import numpy as np
import os
from demoProj.models.analytic import analytic_model_1, analytic_model_2, analytic_model_3
from demoProj.utils.logger import init_logger
from demoProj.utils.argparser import get_config
from sky.plotlib import Plotter, get_multcolumn_subplot
from sky.filemanager import save_script

# ---------------------
# --- Setup section ---
# ---------------------

# result folder
tag = "1d_sin_wave"
result_folder = save_script(os.path.realpath(__file__), tag, max_daily_folders = 7, max_res_folders = 7)

# logger
logger = init_logger(result_folder, "logfile")

# Get user input from: cmd line > config file > defaults
config = get_config("run\intern\model_A.yaml", result_folder, logger)

# -------------------
# --- Run section ---
# -------------------

# create and run model 1
my_mod_1 = analytic_model_1(config = config, logger = logger)
x = np.linspace(0.0, 10, config.nx)
plt_A = my_mod_1.calculate(x, returnType= "plot")

# create and run model 1b
my_mod_1b = analytic_model_2(config = config, logger = logger)
x = np.linspace(0.0, 10, config.nx)
plt_B = my_mod_1b.calculate(x, returnType= "plot")

# Create and run model B
my_mod_2 = analytic_model_3(logger = logger)
x_disc = np.linspace(0.0, 10, 100)
y_disc = np.linspace(0.0, 10, 50)
plt_C = my_mod_2.calculate(x_disc, y_disc, returnType= "plot")


# --------------------
# --- Plot section ---
# --------------------

# Set up plotter objects
plotter = Plotter(save_path = result_folder, stylesheet= "src\\demoProj\\utils\\mpl_stylesheets\\presentation.mplstyle")
plotter_paper = Plotter(save_path = result_folder, stylesheet= "src\\demoProj\\utils\\mpl_stylesheets\\paper.mplstyle")

# Create plots
plotter.plot(plt_A, filename = f'{tag}_plot1')

plotter_paper.plot(plt_A, plt_B, plt_C, filename = f'{tag}_plot2', subplot_grid = [3,1])

fig, ax = get_multcolumn_subplot(n_regular_plots = 3, n_multi_colm = 1, regular_plot_grid = [1,3])
plotter.plot(plt_A, plt_B, plt_C, plt_A, filename = f'{tag}_plot3', custom_fig = [fig, ax])



















