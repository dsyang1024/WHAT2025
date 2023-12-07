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



arg1 = '203.252.82.93'
warnsign = ' WARNING '


def find_file(ipaddress):
    """_summary_

    Args:
        ipaddress (string): address of the ip. this is user's ip address

    Returns:
        file (string): name of the input file for WHAT2025
    """
    filelist = os.listdir(ipaddress)
    filelist = [x for x in filelist if x.endswith(".csv")]

    if (len(filelist) > 1):
        print (warnsign.center(40,'*'))
        print ('you have more than one file')
        print (filelist)
    else:
        infile = filelist[0]
        print (warnsign.center(40,'*'))
        print ('you have one file')
    
    return infile


def read_file(infile):
    infile = infile
    print ('file: ',infile)
    with open(arg1+'/'+infile) as f:
        flines = f.readlines()
    print (' len: ',len(flines))
    print (flines[0])
    print (flines[1])


infile = find_file(arg1)
read_file(infile)