import re

dict = {
	'lol': 'laugh out loud',
	'dw': 'dont\'t worry',
	'hf': 'have fun',
	'gg': 'good game',
	'brb': 'be right back',
	'g2g': 'got to go',
	'wtf': 'what the fuck',
	'wp': 'well played',
	'gl': 'good luck',
	'imo': 'in my opinion'
}

line = raw_input();

for abbv,long in dict.items():
	line = re.sub(r"\b"+abbv+r"\b", long, line);

print line;
