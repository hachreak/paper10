
"""Plot graph."""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import floor

# config

filename = sys.argv[1]

output = None
if len(sys.argv) > 2:
    output = sys.argv[2]

#

df = pd.read_csv(filename)

df = df.apply(lambda x: x * 100 if x.name != 'epochs' else x, axis=0)

ax = plt.gca()
df.plot(kind='line', x='epochs', ax=ax)
ax.set_ylabel('AUC')
ax.yaxis.set_ticks(
    np.arange(floor(min(df.iloc[:, 1:].min())),
              round(max(df.iloc[:, 1:].max()))+0.5, 2.))
ax.grid(True)

colors = ['g', 'm', 'tab:orange', 'tab:cyan', 'b', 'y']
markers = ['x', 'v', '1', '*', '_', '<']
for i in range(0, len(ax.lines)):
    # set color
    ax.lines[i].set_color(colors[i])
    ax.lines[i].set_marker(markers[i])

# update legend
ax.legend(handles=ax.lines)

if output is None:
    plt.show()
else:
    plt.savefig(output, dpi=300)
