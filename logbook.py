#! python
import datetime

def contact():
	# Store contact details
	heard_callsign = raw_input('Station Heard: ').upper()
	rst_heard = raw_input('Station Heard RST: ')
	working_callsign = raw_input('Working Callsign: ').upper()
	rst_working = raw_input('Station Working RST: ')
	freq = raw_input('Frequency (e.g 7038): ')
	mode = raw_input('Mode (e.g PSK31, PSK63, RTTY): ').upper()
	comment = raw_input('Comment (e.g Name, Location): ')

	utc_datetime = datetime.datetime.utcnow()

	# Output contact details
	print('\nQSO Logged:')
	print('Date/Time\t\tHeard\tRST\tWorking\tRST\tFreq\tMode\tComment')
	print(utc_datetime.strftime("%d/%m/%Y %H:%M") + '\t\t' + heard_callsign + '\t' + rst_heard + '\t' + working_callsign + '\t' + rst_working + '\t' + freq  + '\t' + mode  + '\t' + comment);


	# Create a create or open file logbook.txt and store amateur radio contact
	with open("logbook.txt", "a") as myfile:
		myfile.write(utc_datetime.strftime("%d/%m/%Y %H:%M") + '\t' + heard_callsign + '\t' + rst_heard + '\t' + working_callsign + '\t' + rst_working + '\t' + freq  + '\t' + mode  + '\t' + comment + '\n')
		
def logbook():
	print('\nLogbook:')
	print('Date/Time\t\tHeard\tRST\tWorking\tRST\tFreq\tMode\tComment')
	t = open('logbook.txt', 'r')
	print(t.read() + '\n')

def no_such_action():
	print('\nAction not found\n')

def main():
	actions = {"contact": contact, "logbook": logbook}
	while True:
		print('Python Amateur Radio Logbook')
		print('\nMenu Options')
		print('\ncontact: allows you to create an entry')
		print('logbook: shows all log entrys\n')
		selection = raw_input("Your selection: ")
		if "quit" == selection:
			return
		toDo = actions.get(selection, no_such_action)
		toDo()

if __name__ == "__main__":
	main()