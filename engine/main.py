# this should be at the very top of the file
# incoming arguments
arg1 = '203.252.82.93'
msg1 = ' USER:  '+arg1+' '


# importing libraries
import warnings
warnings.filterwarnings("ignore")
import os
os.remove(arg1+'/'+arg1+".log")
import logging
logging.basicConfig(filename=arg1+'/'+arg1+".log", level=logging.INFO)


'''
Dev by  : Dongseok Yang
Contact : yang2309@purdue.edu

init: 2023-12-06
check with the Read.md file to check the update history
this program is for the desktop purpose


'''
print ('===========================================')
print ('= WHAT 2025 ===============================')
print ('= Developed by Dongseok Yang              =')
print ('= The world best Baseflow separation tool =')
print ('============    Now begins!    ============',end='\n\n')
logging.info(msg1)
print (msg1.center(40,'='))


'''
module 01
importer.py
'''
import importer
infile = importer.find_file(arg1)
indata = importer.read_file(arg1, infile)
print('')


'''
module 02
orgnizer.py
'''
import organizer
indata = organizer.read_indata(indata)
print('')


'''
module 03
graphical_analysis.py
'''
import graphical_analysis
FDC_points = graphical_analysis.fdc_plot(indata)


'''
module 04
RecAnalysis.py
'''
import RecAnalysis
rec_list = RecAnalysis.find_rec(indata)
rec_list = RecAnalysis.match_strip_method(rec_list)
RecAnalysis.msm_graph(rec_list, FDC_points)


'''
module 05
MRC.py
'''