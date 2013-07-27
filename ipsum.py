# sum the time to = 4
# need a count of the measure
# need to drop the beat
from random import randint


wub_dict = {
	.5 : ['wub', 'wob'],
	1 : ['wuub', 'woob', 'blat'],
	2 : ['whoomp','wobble'],
	3 : ['breeeeeeeeeeeee', 'squeeeeeeeee'],
	4 : ['pssssssssssssssssh']
	}
	
vocal_dict = {
	2 : ['Let the beat drop'],
	4 : ['And the invaders came from the dark clouds']
}

def get_beats(wub_dict):
	
	
	measure = 0
	while measure < 4:
		time = [ .5 ,1, 2, 3, 4]
		key = time[randint(0,4)]
		#print type(key), 'key', key
		beat = wub_dict[key][randint(0, len(wub_dict[key])-1)]
		print beat
		measure = measure + key
		#print 'measure', measure
		#print 'key', key

def the_drop(x):
		pass

get_beats(wub_dict)
#get vocals(vocal_dict)
	