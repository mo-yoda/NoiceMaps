#%load_ext autoreload
#%autoreload 2

import sys
sys.path.append('../')

import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(12, 12), constrained_layout=True)

layers = plot(
    # 'Wiesbaden, Germany', radius=2000,
    # (50.927072, 11.582887), radius=1800, # innenstadt
    (50.929592,  11.583509), radius=90, # fritz mitte
    ax=ax,

    # backup=layers,

    layers={
        'perimeter': {},
        'streets': {
            'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
            'width': {
                'motorway': 5,
                'trunk': 5,
                'primary': 4.5,
                'secondary': 4,
                'tertiary': 3.5,
                'residential': 3,
                'service': 0,
                'unclassified': 0,
                'pedestrian': 0,
                'footway': 0,
            }
        },
        'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
        'water': {'tags': {'natural': ['water', 'bay']}},
        'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
        'forest': {'tags': {'landuse': 'forest'}},
        'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}}
    },
    drawing_kwargs={
        'background': {'fc': '#EFE7DA', 'ec': '#EFE7DA', 'zorder': -1},
        'perimeter': {'fc': '#EFE7DA', 'ec': '#EFE7DA', 'lw': 0, 'zorder': 0},
        'green': {'fc': '#8db379', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'forest': {'fc': '#508a64', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#346848', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#b6d5e0', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#8cc1e5', 'lw': 1, 'zorder': 2},
        'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 0.5, 'zorder': 3},
        'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
        'building': {'palette': ['#cc5656', '#db8f4f', '#ead977'], 'ec': '#37342f', 'lw': .5, 'zorder': 4},
    },

    osm_credit={'color': '#2F3737'}
)

plt.savefig('C:/Users/monar/Pictures/Projekte/Isabel/fritzM.png', dpi=600)
plt.savefig('C:/Users/monar/Pictures/Projekte/Isabel/fritzM.svg', dpi=600)