import numpy as np
import os
from demoPkg.models.analytic import analytic_model_1d, analytic_model_2d
from demoPkg.utils.filemanager import save_script
from demoPkg.utils.logger import init_logger
from demoPkg.utils.argparser import get_config
from sky.plotlib import Plotter, get_multcolumn_subplot

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

# create and run model A
my_mod = analytic_model_1d(config = config, logger = logger)
x = np.linspace(0.0, 10, config.nx)
plt_A = my_mod.calculate(x, returnType= "plot")

# Create and run model B
my_mod_B = analytic_model_2d(logger = logger)
x_disc = np.linspace(0.0, 10, 100)
y_disc = np.linspace(0.0, 10, 50)
plt_B = my_mod_B.calculate(x_disc, y_disc, returnType= "plot")


# --------------------
# --- Plot section ---
# --------------------

# Set up plotter objects
plotter = Plotter(save_path = result_folder, stylesheet= "src\\demoPkg\\utils\\mpl_stylesheets\\presentation.mplstyle")
plotter_paper = Plotter(save_path = result_folder, stylesheet= "src\\demoPkg\\utils\\mpl_stylesheets\\paper.mplstyle")

# Create plots
plotter.plot(plt_A, filename = f'{tag}_plot1')

plotter_paper.plot(plt_A, plt_B, plt_A, filename = f'{tag}_plot2', subplot_grid = [3,1])

fig, ax = get_multcolumn_subplot(n_regular_plots = 3, n_multi_colm = 1, regular_plot_grid = [1,3])
plotter.plot(plt_A, plt_B, plt_A, plt_A, filename = f'{tag}_plot1', custom_fig = [fig, ax])



















