import json
import threading


# function to read and print json data from files
def read_json(file_name):
    with open(file_name, 'r') as json_file:
        json_data = json.load(json_file)

        for data in json_data:
            print(f"{file_name}, Data: {data}")


json_list = ["file1.json", "file2.json", "file3.json"]


thread_list = []
# create and start threads for each json file
for file in json_list:
    thread = threading.Thread(target=read_json, args=(file,))
    thread.start()
    thread_list.append(thread)

# wait for all threads to finish
for thread in thread_list:
    thread.join()

print("Done!")
