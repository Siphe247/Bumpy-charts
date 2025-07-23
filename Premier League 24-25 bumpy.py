import pandas as pd
import matplotlib.pyplot as plt
import mplsoccer
import highlight_text
from mplsoccer import Bumpy
import numpy as np

from PIL import Image
from io import BytesIO 
import requests

pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League Bumpy Chart.csv')

# Read the CSV file with semicolon separator
df = pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League Bumpy Chart.csv', sep=';')

#teams need to be column names while row names should be weeks
df = df.T

df.head()

#reset the column names so that we drop the transposed team names
df.columns = df.iloc[0]
df = df.iloc[1:]

df.head()

week = ['Week' + str(num) for num in range(1,39)]

print(df.columns.tolist())

#highlight the dictionary to pass in the color. 
highlight_dict= {
    'Liverpool': 'maroon',
    'Arsenal': '#F10000',
    'Manchester City ': '#0DADD1'
    
}

# instantiate object
bumpy = Bumpy(
    scatter_color="#282828", line_color="#252525",  # scatter and line colors
    rotate_xticks=90,  # rotate x-ticks by 90 degrees
    ticklabel_size=17, label_size=30,  # ticklable and label font-size
    scatter_primary='D',  # marker to be used
    show_right=True,  # show position on the rightside
    plot_labels=True,  # plot the labels
    alignment_yvalue=0.1,  # y label alignment
    alignment_xvalue=0.065  # x label alignment
)

fig,ax = bumpy.plot(
    x_list = week,
    y_list = np.linspace(1,20,20).astype(int),
    values = df,
    secondary_alpha = .5,
    highlight_dict = highlight_dict,
    figsize = (18,18),
    y_label = 'Position',
    ylim = (-.1,23),
    lw = 2.5
)

fig.text(s = '24-25 Premier League Across The Season',x = .5, y = .85,
         c = 'white',size=24,weight='bold',ha='center'
        )

highlight_text.fig_text(x=.5, y= .84, 
                       s = 'Comparing <Liverpool>, <Arsenal> &  <Manchester City>',
                       highlight_textprops = [
                           {"color":'maroon'},
                           {"color":'#F10000'},
                           {"color":'#0DADD1'}
                       ],
                        fontsize = 18,
                        color = 'white',
                        ha='center'
                       )

ax2 = fig.add_axes([.12,0.79,.13,.13])
ax2.axis('off')
img = Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier_League_Logo.png')
ax2.imshow(img)
plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League 24-25 bumpy chart.png', dpi=300, bbox_inches='tight')