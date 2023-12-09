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

arg1 = '203.252.82.93'
msg1 = ' USER:  '+arg1+' '
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
RecAnalysis.py
'''
import RecAnalysis
rec_list = RecAnalysis.find_rec(indata)
rec_list = RecAnalysis.match_strip_method(rec_list)
RecAnalysis.msm_graph(rec_list)




'''
module 0#
grapher.py
'''

