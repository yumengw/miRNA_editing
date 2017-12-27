#!/usr/bin/python

import sys

global score_cutoff, max_pos_low_quality, short_read_cutoff, long_read_cutoff

def Usage():
	print '''filter out low quality reads(default score 20, max num of low quality sites 3), and reads that is too short(default 15bp) or too long(default 28 bp) from fastq file
	Usage: %s <fastq> [option for score cutoff] [option for max number of low quality in each reads] [option for short read cutoff] [option for long read cutoff]
	'''%sys.argv[0]
	
def process_reads(each_seq):
	seq = each_seq[1]
	quality = each_seq[3]
	if len(seq) != len(quality):
		print 'Error in fastq: sequence length does no match quality score length'
		exit(1)
	if len(seq) < short_read_cutoff or len(seq) > long_read_cutoff: return 0
	low_quality_sites = 0
	for i in quality:
		#print ord(i) 	#debug
		if ord(i)-33 < score_cutoff: low_quality_sites +=1
		if low_quality_sites > 3: return 0
	return 1


if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		Usage()
		exit()
	
	try: score_cutoff = int(sys.argv[2])
	except: score_cutoff = 20
	try: max_pos_low_quality = int(sys.argv[3])
	except: max_pos_low_quality = 3
	try: short_read_cutoff = int(sys.argv[3])
	except: short_read_cutoff = 15
	try: long_read_cutoff = int(sys.argv[4])
	except: long_read_cutoff = 28
	
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[1] + '.filtered', 'w')
	total_seq = 0
	qualified_seq = 0
	each_seq = 0 # range 1-4, used as a marker to know all info of each sequence in fastq
	each_seq_info = []
	if_qualify = 0 # decision made based on filter criteria
	for line in infile:
		#print line  # debug
		each_seq += 1
		if (each_seq <= 4): each_seq_info.append(line.strip())
		if (each_seq == 4): 
			if_qualify = process_reads(each_seq_info)
			total_seq += 1
			if (if_qualify):
				for info in each_seq_info: outfile.write(info + '\n')
				qualified_seq +=1
			each_seq_info = []
			each_seq = 0
			if_qualify = 0
	infile.close()
	outfile.close()
	
	print 'Input seq: %d Qualified seq: %d' %(total_seq, qualified_seq)




