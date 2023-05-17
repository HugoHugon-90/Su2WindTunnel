import numpy as np
from matplotlib import pyplot as plt
from matplotlib import figure
import matplotlib
matplotlib.use('SVG')

def plot_image(r_min, r_maj, distance, b_d, W, D,df, arg):
    plt.rcParams['text.usetex'] = True
    w, h = figure.figaspect(1)
    plt.rcParams["figure.figsize"] = [w, h] #[7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True


    ngridx = 100
    ngridy = 100
    x = np.array(df.x)
    y = np.array(df.y)

    if arg == 'Heat_Flux':
        z = np.array(df.Heat_Flux)
        plt.title('Heat Flux')
        save = "Heat_Flux.png"
    elif arg == 'Pressure':
        z = np.array(df.Pressure)
        plt.title('Pressure')
        save = "Pressure.png"
    else:
        z = np.array(df.Energy)
        plt.title('Surface Energy')
        save = "surface_energy.png"



# -----------------------
    # Interpolation on a grid
    # -----------------------
    # A contour plot of irregularly spaced data coordinates
    # via interpolation on a grid.

    # Create grid values first.
    xi = np.linspace(-1, 1, ngridx)
    yi = np.linspace(-1, 1, ngridy)

    # ----------
    # Tricontour
    # ----------
    # Directly supply the unordered, irregularly spaced coordinates
    # to tricontour.

    plt.tricontour(x, y, z, levels=50, linewidths=0.3, colors='k')
    cntr1 = plt.tricontourf(x, y, z, levels=50, cmap="RdBu_r")

    plt.colorbar(cntr1)
    plt.plot(x, y, '.', color = 'lightgray', alpha =0.5,  ms=1)
    plt.xlim(-r_maj/2. - W*r_min/2., r_maj/2. + W*r_min/2. )
    plt.ylim(-(b_d+0.5)*distance, 0.5*distance + D )
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')


    plt.savefig("./../output/plots/" + save, dpi=300)
    print(save + " published to the output/plots folder")
    plt.close()
