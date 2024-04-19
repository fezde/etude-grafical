from json import load

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from colour import Color


def divide_chunks(the_list: list, size_of_chunk):
    # looping till length l
    for i in range(0, len(the_list), size_of_chunk):
        yield the_list[i:i + size_of_chunk]


def construc_gradient(list_of_colors: list, total_steps: int) -> list:
    gradient = []
    divisions = len(list_of_colors)-1
    steps_in_division = int(total_steps/divisions)
    for i in range(divisions):
        colors = list(list_of_colors[i].range_to(list_of_colors[i+1], steps_in_division))
        gradient.extend([x.rgb for x in colors])
    return gradient


with open("data.json", "r") as fh:
    data = load(fh)

data_aggregated = []
data_pos = []
data_colors = []


chunk_size = 50
chunks = [x for x in divide_chunks(data, chunk_size)]
n = 0
for c in chunks:
    data_aggregated.append(sum(c))
    data_pos.append(n*chunk_size)
    data_colors.append((n/len(chunks), 0, 0))
    n += 1

gradient = construc_gradient(
    [
        Color(rgb=(0.7, 0, 0)),
        Color(rgb=(0.5, 0.5, 0.5)),
        Color(rgb=(0, 0.8, 0))
    ],
    len(chunks)
)


plt.figure(figsize=(16, 10))
plt.title(f"Number of Sentences by Sentiment ({sum(data):,.0f} Sentences in total)")
# fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

plt.bar(
    data_pos,
    height=data_aggregated,
    width=50,
    color=gradient
)
plt.plot(data, color="#232323")

ax = plt.gca()
ax.set_ylim([0, 700_000])

ax.set_xlabel('<-- negative   ---   neutral   ---   positive -->', fontsize=12)
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))


ax.annotate(
    '> 4.7 Mio sentences \nin the neutral cluster', xy=(980, 696_000), xytext=(650, 642_000), fontsize=12,
    arrowprops=dict(facecolor='blue', shrink=0.05))

plt.tight_layout()
plt.savefig("meditation.png", dpi=72)
