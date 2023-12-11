'''
module graphical_analysis

this is module for the WHAT2025 system

this is module for conducting graphical analysis
a few graphical analysis will be conducted from this module
    1. FDC
    2. Boxplot for flow duration
    3. flow grid
    4. 

01. this module will import indata from organizer module
#! this will sue the sample file from WHAT2020
#todo if available, let's make usgs data imported

02. format of the csv file will be date,flow(CMS)
    date(YYYY-m-d),streamflow
    ex:
    2023-1-1,3.00

'''

import seaborn as sns
sns.set_style('whitegrid')
import matplotlib.pyplot as plt
import numpy as np
import datetime

def fdc_plot(indata):
    flowdata = [i[1] for i in indata]
    # // convert streamflow to the float array
    flowdata = np.array(flowdata[1:], dtype='float64')
    flowdata = np.sort(flowdata)

    # // according to the FDC flow duration range, find flow point of 10%, 40%, 60%, 90%
    # ! Flow criteria
    # High Flows (HF) : 0-10% occurence
    # Moist Conditions (MC) : 10-40% occurence
    # Mid-range Flows (MF) : 40-60% occurence
    # Dry Conditions (DC) : 60-90% occurence
    # Low Flows (LF) : 90-100% occurence

    HFpoint = np.percentile(flowdata,90,method='nearest')
    MCpoint = np.percentile(flowdata,60,method='nearest')
    MFpoint = np.percentile(flowdata,40,method='nearest')
    DCpoint = np.percentile(flowdata,10,method='nearest')
    
    msg2 = ' FDC break points are below '
    print (msg2.center(40,'-'))
    print(HFpoint,MCpoint,MFpoint,DCpoint)

    # // assign occurence to the each flow
    uniqueflow, flowcounts = np.unique(flowdata, return_counts=True)
    # convert flowcounts to the occurence
    for i in range(1,len(flowcounts)):
        flowcounts[i] = flowcounts[i-1]+flowcounts[i]
    flowcounts = flowcounts/len(flowdata)*100

    plt.figure(figsize=(8,5))
    fdc = sns.lineplot(x=flowcounts[::-1],y=uniqueflow[::-1], color='b')
    fdc.set(title='Flow Duration Curve', xlabel='Occurence (%)', ylabel='Streamflow (Log $\mathregular{m^{3}}$/sec)')
    plt.yscale('log')
    plt.xlim(max(flowcounts),0)
    plt.vlines(90,0,max(flowdata), linestyles ="dashed", colors ="k")
    plt.vlines(60,0,max(flowdata), linestyles ="dashed", colors ="k")
    plt.vlines(40,0,max(flowdata), linestyles ="dashed", colors ="k")
    plt.vlines(10,0,max(flowdata), linestyles ="dashed", colors ="k")
    plt.savefig('FDC_graph.png', dpi=600)
    plt.clf()
    # plt.show()


    # // assign flows to the different list depends on the flow duration
    # ! draw flow boxplot per flow duration
    HFdur = [i for i in flowdata if i>HFpoint]
    MFdur = [i for i in flowdata if i>MCpoint and i<= HFpoint]
    MCdur = [i for i in flowdata if i>MFpoint and i<= MCpoint]
    DCdur = [i for i in flowdata if i>DCpoint and i<= MFpoint]
    LFdur = [i for i in flowdata if i<= DCpoint]

    plt.figure(figsize=(10,5))
    ax= plt.subplot()
    ax.set_title('Flow Duration Curve')
    plt.boxplot([HFdur, MFdur, MCdur, DCdur, LFdur])
    plt.yscale('log')
    plt.xlabel('Flow Durations')
    ax.set_xticklabels(['High Flows','Moist Conditions','Mid-range Flows','Dry Conditions','Low Flows'])
    plt.tight_layout()
    plt.savefig('FDC_box_graph.png', dpi=600)
    plt.clf()
    # plt.show()


    # // streamflow colormap
    # make yearly-monthly average
    yearlist = [str(i[0].year)+'-'+str(i[0].month).zfill(2) for i in indata[1:]]
    flowlist = [i[1] for i in indata[1:]]
    unique_ym = list(set(yearlist))
    unique_ym.sort()

    # calculate average streamflow per month
    avgflow = []
    for i in unique_ym:
        temp = 0
        count = 0
        for r in range(len(yearlist)):
            if yearlist[r] == i:
                temp = temp + flowlist[r]
                count += 1
        tempa = i.split('-')
        avgflow.append([int(tempa[1]),int(tempa[0]),round(temp/count,4)])
    # arrange list by month-year
    avgflow.sort()

    # make the pcolormap
    x = np.arange(2009, 2009+len(avgflow)/12,1) # twelve months
    y = np.arange(1,13,1) # total years
    # ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    X, Y = np.meshgrid(x, y)
    z = np.array([i[2] for i in avgflow])
    Z = np.reshape(z, (len(y), len(x)))


    # plot
    c = plt.pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), cmap='RdYlBu', shading='auto')
    plt.colorbar(c, label='Monthly Avg. Streamflow ($\mathregular{m^{3}}$/sec)')
    plt.xlabel('Year')
    plt.ylabel('Month')
    plt.savefig('Flowgram.png',dpi=600)


    return [HFpoint,MCpoint,MFpoint,DCpoint]