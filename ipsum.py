# sum the time to = 4
# need a count of the measure
# do dict logic
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
	.5 : ['Yep'],
	1 : ['Engage'],
	2 : ['Let the beat drop'],
	3 : ['blank'],
	4 : ['And the invaders came from the dark clouds', 
	'blocking the out Earth\'s sun']
}

drop_dict = {
	.5 : ['BRE', 'WOB', 'WUB', 'WOBBLE', 'BEE', 'wub', 'wob'],
	1 : ['WUUB', 'WOOB', 'BREEMP', 'BROOT', 'BREE', 'wuub', 'woob', 'blat'],
	2 : ['WHOOMP', 'BWAMP', 'whoomp','wobble'],
	3 : ['BREeEEEEEEeeEEEEE', 'breeeeeeeeeeeee', 'squeeeeeeeee'],
	4 : ['BRAAAAAAAAAAAAAAAAAAAAAAP']
}

fade_dict = {
	.5 : ['tss', 'taa'],
	1 : ['tsssssss', 'taa'],
	2 : ['tsssssssssssss', 'taaaaaaaaaaaaa'],
	3: ['pssssssssssssssssssstaaa'],
	4 : ['tssssssssssssssstaaaaaaaaaaaaaaaaaaa']
}

all_the_dicts = [wub_dict, vocal_dict, fade_dict]

def get_key(dict_in_a_box, measure):
		
	time = [ .5 ,1, 2, 3, 4]
	time_avail = []
	#this is only true for the first loop
	if measure == 0:
		key = time[randint(0,4)]
		#print 'first key', key
		return key
	else:
		for i in range(len(time)):
			#this is to see which element is valid given what has already been choosen
			if measure + i <= 4:
				#print 'time[i]', time[i]
				time_avail.append(time[i])
		key = time_avail[randint(0,len(time_avail)-1)]
		#print 'other key', key		
		return key


def get_beats(dict_in_a_box):
	measure = 0
	key = get_key(dict_in_a_box, measure)
	while (measure + key) <= 4:
		#print type(key), 'key', key
		beat = dict_in_a_box[key][randint(0, len(dict_in_a_box[key])-1)]
		print beat,
		measure = measure + key
		#print 'measure', measure
		#print 'key', key
		key = get_key(dict_in_a_box, measure)
		#return key
		
def choose_dict(all_the_dicts, measure):
		
	if (measure >14 and measure < 21):
		dict_in_a_box = drop_dict
		return dict_in_a_box
	else:
	#in cm, it's bigger that way
		size = len(all_the_dicts)
		dict_in_a_box = all_the_dicts[randint(0,(size-1))]
		return dict_in_a_box
	
def create_song(num_of_measures):
#def create_song(num_of_measures, which_measure):
	which_measure = 0
	while which_measure < num_of_measures:
		#while which_measure < num_of_measures:
		dict_in_a_box = choose_dict(all_the_dicts, which_measure)
		get_beats(dict_in_a_box)
		which_measure += 1
		print which_measure
	


# ask user to pass in how many songs they need
create_song(30)
	