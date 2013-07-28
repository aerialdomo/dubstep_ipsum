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
	
all_the_dicts = [wub_dict, vocal_dict,drop_dict]

measure = 0	
def choose_dict(all_the_dicts, measure):
	#in cm, it's bigger that way
	size = len(all_the_dicts)
	dict_in_a_box = all_the_dicts[randint(0,(size-1))]
	print dict_in_a_box
	# do dict logic


choose_dict(all_the_dicts, measure)	
			
		