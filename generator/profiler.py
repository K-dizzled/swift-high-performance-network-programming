import psutil 
import os
import time
from generator_config import *
from datetime import datetime

if __name__ == '__main__':
	date_time = datetime.now()
	date_str = date_time.strftime("%Y-%m-%d_%H-%M")

	cpu_log_file_name = "%s.%s.%s" % (language, date_str, cpu_data_logging_file)
	vmem_log_file_name = "%s.%s.%s" % (language, date_str, vmem_data_logging_file)

	cpu_file = open(cpu_log_file_name,"w+")
	cpu_file.close()
	vmem_file = open(vmem_log_file_name,"w+")
	vmem_file.close()

	while True:
		cpu_file = open(cpu_log_file_name,"a")
		vmem_file = open(vmem_log_file_name,"a")

		cpu_file.write(str(psutil.cpu_percent()) + '\n')
		vmem_file.write(str(psutil.virtual_memory().used) + '\n')

		time.sleep(1)
		cpu_file.close()
		vmem_file.close()