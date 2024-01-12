import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def get_new_figure(xtick=None, ytick=None):
    """ build a figure appropriate for observing gemoetric objects
    
    Args:
        xtick (np.array): x positions of grid lines
        ytick (np.array): y positions of grid lines
        
    Returns:
        fig (plt.Figure): a figure object
        ax (plt.Axes): an axes object (remember, in subplots a single
            figure can have many axes.  only the axes can contain
            the plot, a figure merely contains one or more plt.Axes)
    """
    if xtick is None:
        xtick = np.linspace(-8, 8, 17)
        
    if ytick is None:
        ytick = np.linspace(-8, 8, 17)
    
    # make a new figure and axis
    fig, ax = plt.subplots(1, 1)
    plt.xticks(xtick)
    plt.yticks(ytick)
    
    # ensure that x axis has same scale as y axis (else circles look like ellipses)
    ax.set_aspect('equal', adjustable='box')
    
    # make a bit bigger, easier to see
    fig.set_size_inches(4, 4)
    
    return fig, ax
    
