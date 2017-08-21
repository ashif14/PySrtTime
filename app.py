import re

def getSequenceTime(sequence):
# time = '00:00:00,000 --> 00:00:04,440'

	timeframe = sequence.split('-->')
	timecodes = []

	timecodes.append(timeframe[0].strip())
	timecodes.append(timeframe[1].strip()) 

	totalSecs = 0
	for tm in timecodes:
	    timeParts = [int(s) for s in tm.split(',')[0].split(':')]
	    totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
	# totalSecs, sec = divmod(totalSecs, 60)
	# hr, min = divmod(totalSecs, 60)
	# print "%d:%02d:%02d" % (hr, min, sec)
	return totalSecs

def getSubtitleTime(file):
	isSeq = False
	firstSeq = False
	firstTimeSeq = None
	lastTimeSeq = None
	with open(file) as f:
	    for line in f:

	    	if(firstSeq):
	    		firstTimeSeq = line.strip()
	    		firstSeq = False
	    	if(line.strip() == '1'):
	    		firstSeq = True
	    	if(isSeq):
	    		lastTimeSeq = line.strip()
	    		isSeq = False
	    	if(re.compile('[0-9]+$').match(line.strip())):
	    		isSeq = True

	return getSequenceTime(lastTimeSeq) - getSequenceTime(firstTimeSeq)

# print(getSubtitleTime('sample.srt'))