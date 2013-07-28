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

def get_key(wub_dict, measure):
		
	time = [ .5 ,1, 2, 3, 4]
	time_avail = []
	if measure == 0:
		key = time[randint(0,4)]
		#print 'first key', key
		return key
	else:
		for i in range(len(time)):
			if measure + i <= 4:
				#print 'time[i]', time[i]
				time_avail.append(time[i])
		key = time_avail[randint(0,len(time_avail)-1)]
		#print 'other key', key		
		return key


def get_beats(wub_dict):
	measure = 0
	key = get_key(wub_dict, measure)
	while (measure + key) <= 4:
		#print type(key), 'key', key
		beat = wub_dict[key][randint(0, len(wub_dict[key])-1)]
		print beat,
		measure = measure + key
		#print 'measure', measure
		#print 'key', key
		key = get_key(wub_dict, measure)

def the_drop(x):
		pass

#key, measure = get_key(wub_dict)
get_beats(wub_dict)
#get vocals(vocal_dict)
	