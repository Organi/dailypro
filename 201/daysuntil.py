from datetime import date

raw = raw_input()
raw = raw.split(' ')

today = date.today()
until = date(int(raw[0]), int(raw[1]), int(raw[2]))
diff = until - today

print "%s days from %s to %s" % (diff.days, today, until)
