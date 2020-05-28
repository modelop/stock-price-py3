import sys as sys

# fastscore.schema.0: stock_quote
# fastscore.schema.1: stock_quote

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	
	yield(datum)
