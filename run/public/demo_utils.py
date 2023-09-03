import numpy as np
import os
import matplotlib.pyplot as plt
from demoProj.models.analytic import analytic_model_1d
from demoProj.utils.filemanager import save_script
from demoProj.utils.logger import init_logger
from demoProj.utils.argparser import get_config


# ---------------------
# --- Setup section ---
# ---------------------

# result folder
tag = "util_demo"
result_folder = save_script(os.path.realpath(__file__), tag, max_daily_folders = 7, max_res_folders = 7)

# logger
logger = init_logger(result_folder, "logfile")

# Get user input from: cmd line > config file > defaults
config = get_config("run\\public\\util_demo.yaml", result_folder, logger)

# -------------------
# --- Run section ---
# -------------------

# create and run model 1
my_mod_1 = analytic_model_1d(config = config, logger = logger)
x = np.linspace(0.0, 10, config.nx)
y = my_mod_1.calculate(x)

# --------------------
# --- Plot section ---
# --------------------

# Plotting
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Demo')
plt.savefig(result_folder + "/" + tag + "_plot.pdf")

plt.show()





















