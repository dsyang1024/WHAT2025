'''
module importer

this is module for the WHAT2025 system

this is module for importing/reading the input file

01. this module will import/read the file
#! this will sue the sample file from WHAT2020
#todo if available, let's make usgs data imported

02. format of the csv file will be date,flow(CMS)
    date(YYYY-m-d),streamflow
    ex:
    2023-1-1,3.00

'''


#? import library
import os


warnsign = ' WARNING '


def find_file(ipaddress):
    """_summary_

    Args:
        ipaddress (string): address of the ip. this is user's ip address

    Returns:
        file (string): name of the input file for WHAT2025
    """
    # // find the file from the ip address folder
    # ! if not needed, should be changed
    filelist = os.listdir(ipaddress)
    filelist = [x for x in filelist if x.endswith(".csv")]

    # // if there is more than one file, will make error
    # ! there will be one file with the correct name, this is not a problem for the desktop version
    if (len(filelist) > 1):
        print (warnsign.center(40,'*'))
        print ('you have more than one file')
        print (filelist)
    else:
        infile = filelist[0]
    
    return infile


def read_file(ipaddress,infile):
    """_summary_

    Args:
        ipaddress (string): address of the ip. this is user's ip address
        infile (string): name of the input file

    Returns:
        list: list of the input data in file
    """
    msg1 = 'input file: '+infile
    print (msg1.center(40))

    # // read the file and make them as a list
    with open(ipaddress+'/'+infile) as f:
        indata = f.readlines()
    msg2 = 'data length: '+f"{len(indata):,}"
    print (msg2.center(40))

    msg3 = ' File import done '
    print (msg3.center(40,'-'))
    
    return indata