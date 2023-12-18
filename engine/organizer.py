'''
module organizer

this is module for the WHAT2025 system

this is module for organizing input file according to the time-series

01. this module will organize according to the season first
    - date will be organized according to the season
02. format of the csv file will be date,flow(CMS)

'''
import datetime

dateformat = '%Y-%m-%d'


def read_indata(indata):
    # change the header
    indata[0] = ['date(YYYY-m-d)', 'streamflow', 'Season']
    """_summary_

    Args:
        indata (list): input data from the input file

    Returns:
        list: updated data list
    """
    
    # add month to the indata list and convert the data format
    for i in range(1, len(indata)):
        indata[i] = indata[i].replace('\n','')
        indata[i] = indata[i].split(',')
        if i == 1:
            msg1 = 'data init. date: '+indata[i][0]
            print (msg1.center(40))

        indata[i][1] = round(float(indata[i][1]),4)

        # // convert to datetime
        indata[i][0] = datetime.datetime.strptime(indata[i][0], dateformat)

        # // temp is the month
        temp = indata[i][0].month
        if temp>2 and temp<6:
            indata[i].append ('spring')
        elif temp>5 and temp<9:
            indata[i].append ('summer')
        elif temp>8 and temp<12:
            indata[i].append ('fall')
        else:
            indata[i].append ('winter')
        
    msg2 = ' Data conversion done '
    print (msg2.center(40,'-'))
    
    return indata


 
