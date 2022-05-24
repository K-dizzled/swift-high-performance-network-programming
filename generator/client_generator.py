import os
from argparse import ArgumentParser
from generator_config import *
from graphing import *
from atomic_integer import AtomicInteger
from multiprocessing import Pool
import plotly.express as px
import multiprocessing as mp
from threading import Thread
import numpy as np
import sys
import psutil
import subprocess
import time


def run_swift_client(profiling_cpu, start):
	command = './' + swift_client_path

	p = subprocess.Popen(
		[command], 
		shell=True, 
		stdout=subprocess.PIPE
	)

	(output, err) = p.communicate() 
	p_status = p.wait()

	# End measuring time 
	end = time.time()

	print("Number of bytes recieved per second: ", len(output) / (end - start))
	print("Number of bytes recieved in total: ", len(output))
	print("---------------------------------")
	return (len(output) / (end - start) / (1024 ** 2))


def run_n_clients(n, profiling_cpu=False):
	# Start measuring time
	start = time.time()

	bytes_per_second_clients = [None for i in range(n)]

	pool = Pool(processes=mp.cpu_count())

	for i in range(n):
	 	bytes_per_second_clients[i] = pool.apply_async(run_swift_client, (profiling_cpu, start))

	pool.close()
	pool.join()

	return bytes_per_second_clients


def run_server(lang):
	# Returns pid of the process 
	# which runs the server.

	if lang == 'swift':
		if not os.path.exists(swift_server_path):
			os.system('make -C ' + swift_server_dir_path)

		proc = subprocess.Popen([swift_server_path], stdout=subprocess.PIPE)
	elif lang == 'java':
		if not os.path.exists(java_server_path):
			print('Building java server.')
			os.system('gradle build -p ' + java_server_dir_path)

		command = 'java -jar ' + java_server_path
		proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
	else: 
		raise Exception('Unknown language.')

	print('Started process: ', proc.pid)	
	return proc

def run_profiler():
	command = 'python3 profiler.py'
	proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)

	print('Started process: ', proc.pid)	
	return proc

def stop_server(the_process):
	print("Killing process:")
	print(the_process.pid)
	the_process.kill()


if __name__ == '__main__':
	parser = ArgumentParser(description='Client generator.')
	parser.add_argument('--max_client_amount', type=int, default=max_client_amount, help='Amount of clients connecting to the server.')
	parser.add_argument('--language', type=str, default=language, help='Language of the server.')
	args = parser.parse_args()

	if not os.path.exists(swift_client_path):
		os.system('make -C ' + swift_client_dir_path)


	# Start measuring time
	start = time.time()

	averages = [None for i in range(args.max_client_amount)]
	std_devs = [None for i in range(args.max_client_amount)]

	date_time = datetime.now()
	date_str = date_time.strftime("%Y-%m-%d_%H-%M")

	lof_file_name = "%s.%s.%s" % (args.language, date_str, averages_data_logging_file)
	log_file = open(lof_file_name, "w+")
	log_file.close()

	for i in range(1, args.max_client_amount + 1):
		server_process = run_server(args.language)

		if i == args.max_client_amount:
			profiler_process = run_profiler()

		results = run_n_clients(i)

		get_res = [result.get() for result in results]
		average = sum(get_res) / len(get_res)
		std_dev = np.std(get_res) 

		averages[i-1] = average
		std_devs[i-1] = std_dev

		# Save to log file: 
		log_file = open(lof_file_name, "a")
		log_file.write("%d %.3f %.3f\n" % (i, average, std_dev))
		log_file.close()

		stop_server(server_process)

		if i == args.max_client_amount:
			stop_server(profiler_process)

	plot_graph1([i for i in range(1, args.max_client_amount + 1)], averages)
	plot_graph3([i for i in range(1, args.max_client_amount + 1)], std_devs)

	# End measuring time 
	end = time.time()
	
	print('Finished execution in %d seconds.' % (end - start))
