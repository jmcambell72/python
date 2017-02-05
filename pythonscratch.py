# simple testing. boolean 
# sea = None
# if sea:
#	print sea.upper()
# else:
#	print 'does not exist'

#sea = 'red'
#if sea == None:
#		print 'sea is empty'
#elif sea == 'atlantic':
#	print sea, 'ocean is green'
#elif sea == 'pacific':
#	print sea, 'ocaen is blue'
#elif sea == 'red':
#	print sea, 'sea is red'
#else:
#	print sea, 'sea is unknown'

#flight = [342, 'ARN', 'XYZ', 3211.89]

#print flight[0]
#if flight[3] > 4000:
#	print 'Cost exceeds the max'
#else: 
#	print 'Flight is ok'
#	tax = 2.00
#	flight[3] = flight[3] * tax
#	print flight[3]

#print flight[::2]

from Tkinter import Tk, Label, Button, mainloop

def setup_gui(base, prompt='Default Instructions'):
	infolabel = Label(base, text=prompt, bg='white', fg='blue')
	infolabel.pack(side='left', expand=1, fill='both')

	execbutton = Button(base, text='Execute', fg='black')
	execbutton.pack(side='left')

	exitbutton = Button(base, text='Exit', fg='Red')
	exitbutton.pack(side='right')

	pushbutton = Button(base, text='Push', fg='Red')
	pushbutton.pack(side='left')

	checkprocess = Button(base, text='PS', fg='Red')
	checkprocess.pack(side='left')

root = Tk()
root.title('Houses')
setup_gui(root)

mainloop()

# List method examples 

#airports = ['SFO','LNY','YHZ','YYZ','NRT','CDG']
#airports.append('LGA')
#airports.insert(0,'AMS')
#airports.sort()
#print airports 
#airports.remove('NRT')
#print airports 

# Tuple 

#planes = 'A350','A380','B747','B737'

#print planes 

#biggest_plane = 'A370',

#print biggest_plane

#oldest_plane = 'B747',

#print oldest_plane

#print airports[1:3] * 2

#codes = ['LAX','HNL','YYZ','NRT','CDG']
#destinations = tuple(codes) 

#print destinations

#print airports == destinations

# dictionary

#cities = {'XYZ' : 'Toronto', 'NRT' : 'Tokyo/Narita'}
#print cities['XYZ']

#print cities.keys()
#print cities.values()
#print cities.get(0)

#print len(cities)

#print cities.items()

# zip 

#countires = ['FR','GB','CA','JP','US']
#prefixes = [33, 44, 1, 81]

#output = zip (countires,prefixes)

#print "==================="
#print "this is the output ", output
#print "==================="


#airports = ['SFO','LNY','YHZ','YYZ','NRT','CDG']
#planes = 'A350','A380','B747','B737'

#for airport in airports:
#	for plane in planes:
#		dest = airports + planes

#print dest

#airports = {'YYZ': 'Toronto', 'NRT' : 'Tokyo'}

#for key, value in airports.items(): 
	# print key, value 

# simple function

#def print_one():
#	num = 1
#	print 'the value of num is', num 

#def print_two():
#	num = 2 
#	print 'the value of num is', num


#print_one()

#print_two()

#print print_one
#print print_two

#def printposit(depart, arrive):
#	print 'This flight departs from', depart, ' and arrives in', arrive

#printposit('LHR','JFK')

#def airportplan(depart='LAX', arrive='HNL'):
#		print 'depart and arrive defaults:', depart, arrive 

#print airportplan(depart='LHR')

#print id(airportplan)

#var = 'outside function of report'
#def logdata(ddata):
#	def print_header():
#		print 'Report starting'
#		header = 'Variable inside header'
#		print header 
#	def print_footer():
#		print 'End of report'
#		footer = 'Variable inside footer'
#		print footer 
#	print_header()
#	print 'Log Data'
#	print ddata
#	return ddata + ddata
#	print ddata
#	print_footer()

#print var 
#logdata(1)









