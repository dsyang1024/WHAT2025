'''
module RecAnalysis

this is module for the WHAT2025 system

this module will analyze recession curve from each segments


01. this module will extract recession curve from the each events
    - the minimum recession day is 3 days
02. format of the csv file will be date,flow(CMS)

'''
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid", palette="pastel")




def find_rec(indata):
    """_summary_

    Args:
        indata (list): streamflow data

    Returns:
        list: list of the recession curves
    """
    temp = [] # temp is list for temporary list of the recession curve
    rec_list = [] # rec_list is list for the recession curves
    
    # // starting from the first day, find the recession curve
    for i in range(2,len(indata)):
        # ? if streamflow is decreasing from previous day(s), add to the temp list
        if indata[i][1] < indata[i-1][1]:
            temp.append(indata[i-1][1])
        else:
            # ? if streamflow is increasing, recession days is more than 3 days, save it to the list and reset temp list
            if len(temp) > 3:
                rec_list.append(temp)
                temp = []
            else:
                temp = []
    
    return rec_list


def match_strip_method(rec_list):
    """_summary_

    Args:
        rec_list (list): list of the recession curve

    Returns:
        list: list of the recession curve with the recession date
    """
    # sort 
    rec_list = sorted(rec_list, reverse=True)

    # ! this part is implementing matching strip method manually
    # // for the first event with the biggest flow, and assign the recession days
    for i in range(len(rec_list[0])):
        rec_list[0][i] = [i+1, rec_list[0][i]]
    
    # // from the second event, assign days depends on the first day of the recession
    # // find which day from the previous recession (in order of the size)
    # for each recession curve
    for i in range(1,len(rec_list)):
        # find the closest flow from previous flow to biggest flow of current recession
        value_index = find_closest(rec_list[i-1],rec_list[i][0])
        rec_init_day = rec_list[i-1][value_index][0] # rec_init_day is recession date of the first streamflow
        # for each streamflow, assign recession date using rec_init_day variable
        for r in range(len(rec_list[i])):
             rec_list[i][r] = [rec_init_day, rec_list[i][r]]
             rec_init_day += 1
    
    # // updated recession list with the recession date will be returned
    return rec_list


def msm_graph(rec_list, FDC_points):
    """_summary_
        this function is making graph for the matching strip method
    Args:
        rec_list (list): list of the recession curve with the recession date 
        FDC_points (list): list of the FDC points from the streamflow data
    """
    # todo do the msm plot depends on the flow duration
    # figure size control
    plt.figure(figsize=(8,5))

    def color_picker(peakflow, FDC_points):
        # this funtion is in-function for the color picker
        if peakflow > FDC_points[0]:
            return 'black'
        elif peakflow <= FDC_points[0] and peakflow > FDC_points[1]:
            return 'blue'
        elif peakflow <= FDC_points[1] and peakflow > FDC_points[2]:
            return 'green'
        elif peakflow <= FDC_points[2] and peakflow > FDC_points[3]:
            return 'orange'
        else:
            return 'red'


    for i in range(len(rec_list)):
        x_values = [r[0] for r in rec_list[i]]
        y_values = [r[1] for r in rec_list[i]]
        # peakflow is first streamflow of the recession i event
        peakflow = rec_list[i][0][1]
        sns.lineplot(x=x_values,y=y_values,color=color_picker(peakflow, FDC_points),linewidth=0.5)
    
    plt.yscale('log')
    plt.xlabel('Recession date (days)')
    plt.ylabel('Streamflow (Log $\mathregular{m^{3}}$/sec)')
    plt.title('Matching Strip Method')
    plt.savefig('MSM_fig.png',dpi=600)


def find_closest(value_list,value):
    value_list = [k[1] for k in value_list]
    diff_list = [round(abs(k-value),4) for k in value_list]
    value_index = diff_list.index(min(diff_list))
    return value_index

