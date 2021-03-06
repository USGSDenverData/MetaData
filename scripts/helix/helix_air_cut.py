#===============================================================================
# EXTRACTION SCRIPT helix_air_cut.py
#===============================================================================
'''
modifier: 1
eqtime: 10
'''

def main():
    info('Air pipette')

    open('3')
    close('2')
    open('1')

    # close of chambers
    close('8')
    close('9')

    close('7')

    #pump out pipette
    open('5')
    open('11')
    open('6')
    sleep(15)
    close('6')

    sleep(2)
    if analysis_type=='blank':
        info('Blank. Not filling pipette')
    else:
        info('Filling pipette')
        open('7')

    sleep(30)
    close('7')
    #expand pipette
    close('5')
    close('4')

    sleep(2)
    open('6')

    #firststagecleanup
    info('first stage cleanup')
    sleep(30)

    #cut gas
    close('6')
    close('11')
    sleep(2)
    open('4')
    open('5')
    sleep(2)
    open('3')
    sleep(60)
    close('3')
    close('5')
    open('11')
    sleep(30)
    #end cut gas

    close('3')
    sleep(2)
    open('4')
    
    #secondstagecleanup
    info('second stage cleanup')
    sleep(30)

    #gas staged behind inlet

#===============================================================================
# POST EQUILIBRATION SCRIPT helix_pump_prep.py
#===============================================================================
def main():
    close('6')
    open('4')
    sleep(2)
    open('11')
    open('5')
    sleep(10)
    close('4')
    sleep(2)
    open('3')
#===============================================================================
# POST MEASUREMENT SCRIPT helix_pump_ms.py
#===============================================================================
def main():
    open('1')
