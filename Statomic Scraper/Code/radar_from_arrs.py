import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import pandas_scraping as ps

#plots radar chart
def radar(statVals, statNames, playerName):
    
    #derives what angles to create plots at
    plot_angles = []
    
    #evenly spaces out plots
    for i in range(0, 360, 360//len(statNames)):
        # degrees to radians conversion , as pyplot uses radians
        plot_angles.append(float(i) * (pi/180))
    
    #creates subplot, must be polar so that circle shape is achieved
    plt.subplot(polar=True)
    
    #statNames used for x ticks
    statNames_ticks = []
    
    #abbreviates stat names so that plot looks a little neater
    def abv(string):
        string = string.replace("-", " ")
        string = string.replace("(", "")
        string = string.replace(")", "")
        arr = string.split(" ")
        nstr = ""

        if len(arr) > 1:
            for word in arr:
                nstr += word[0]

            return nstr

        return string
    
    #populates stat name ticks array
    for x in range(len(statNames)):
        statNames_ticks.append(
            abv(statNames[x]) + " (" + str(int(statVals[x])) + ")")
    
    #adds x ticks at angles specified
    plt.xticks(plot_angles, statNames_ticks)
        
    #adds player name to plot
    name = plt.figtext(0.1, 0.85, playerName)
    
    #appending array as first and last values need to be the same for plot() function
    plot_angles.append(plot_angles[0])
    statVals.append(statVals[0])
    
    #plots values at angles specified
    plt.plot(plot_angles, statVals, "#1c1c1c", alpha=0.7)
    
    #not necessary, added for aesthetic purposes
    plt.fill(plot_angles, statVals, "#4b8057", alpha=0.3)

    #removes 0, 10, 20 etc. steps to make plot look neater
    plt.gca().axes.yaxis.set_ticklabels([])

    #hidesedge of polar subplot
    plt.gca().spines["polar"].set_visible(False)

    #set max value of percentile (100) and adds 1 unit so that plot looks neater
    plt.ylim(0, 101)
    
    '''Enter a gile name to save plt, otherwise it will just be displayed'''
    #plt.savefig(filename)
    
    #show plot
    plt.show()
