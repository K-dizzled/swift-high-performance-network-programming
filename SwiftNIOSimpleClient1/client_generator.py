import os
from argparse import ArgumentParser
from generator_config import *
import sys
import subprocess
import time

def run_server(lang):
	# Returns pid of the process 
	# which runs the server.

	if lang == 'swift':
		if not os.path.exists(swift_server_path):
			os.system('make -C ' + swift_server_dir_path)

		proc = subprocess.Popen([swift_server_path], stdout=subprocess.PIPE)

		print("Started process:")
		print(proc.pid)
		return proc

def stop_server(the_process):
	print("Killing process:")
	print(the_process.pid)
	the_process.kill()


if __name__ == '__main__':
	parser = ArgumentParser(description='Client generator.')
	parser.add_argument('--client_amount', type=int, default=client_amount, help='Amount of clients connecting to the server.')
	parser.add_argument('--language', type=str, default=language, help='Language of the server.')
	args = parser.parse_args()

	# server_process = run_server(args.language)

	if not os.path.exists(swift_exe_name):
		os.system('make')

	commands = './' + swift_exe_name
	for i in range(args.client_amount - 1):
		commands += (' & ./' + swift_exe_name)

	# Start measuring time
	start = time.time()

	p = subprocess.Popen(
		[commands], 
		shell=True, 
		stdout=subprocess.DEVNULL
	)

	(output, err) = p.communicate() 
	p_status = p.wait()

	# End measuring time 
	end = time.time()

	# stop_server(server_process)
	print('Finished execution in %d seconds.' % (end - start))
