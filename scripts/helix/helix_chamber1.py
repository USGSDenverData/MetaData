#===============================================================================
# EXTRACTION SCRIPT helix_chamber1.py
#===============================================================================
def main():
	info('Sample Chamber 1 analysis')
	gosub('PrepareForChamber1Analysis')

	if analysis_type=='blank':
		info('is blank. not heating')
		close('5')
		close('3')
		sleep(1)
		open('4')
		sleep(len(position)*duration)
	else:
		info('move to position {}'.format(position))
		for i,p in enumerate(position):

			move_to_position(position)
			sleep(2)
			if i==0:
				enable()
				close('5')
				close('3')
				sleep(1)
				open('4')
			extract(extract_value)
			sleep(duration)
			if disable_between_positions:
				disable()

		disable()

	sleep(cleanup)

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
