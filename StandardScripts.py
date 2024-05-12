# Imports
import datetime
import sys
import os


logs_directory = 'logs'
START_DATE_TIME = datetime.datetime.now()
END_DATE_TIME= None
valid_count=0
failed_count=0
total_count=0



#create folder for logs
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

# logging part in txt file
def print_logs(logs):
    with open(f'{logs_directory}/log_{START_DATE_TIME.strftime("%Y-%m-%d-%H.%M")}.txt' , 'a') as log:
        log.write(logs+'\n')

def print_success(msg):
    with open(f'{logs_directory}/valid_{START_DATE_TIME.strftime("%Y-%m-%d-%H.%M")}.txt' , 'a') as log:
        log.write(msg+'\n')
        print_logs("Info:"+msg+'\n')
def print_error(msg):
    with open(f'{logs_directory}/valid_{START_DATE_TIME.strftime("%Y-%m-%d-%H.%M")}.txt' , 'a') as log:
        log.write(msg+'\n')
        print_logs("Error:"+msg+'\n')
def print_status():
    END_DATE_TIME= datetime.datetime.now()
    print_logs("Script status:")
    print_logs(f"Start Time: {START_DATE_TIME}, End time: {END_DATE_TIME}\nDuration of the script{END_DATE_TIME-START_DATE_TIME}")
    print_logs(f"Number of valid deletion {valid_count}, Failed to delete: {failed_count}, total count: {total_count}")


# if you pass any param in terminal read it from here using global variable
def read_system_arguments():
    arguments = sys.argv
    print(arguments)
    if len(arguments)>1:
        # Read arguments because
        pass








def operations():
    # things you want to do in the script
    print_status()










if __name__ == "__main__":
    operations()