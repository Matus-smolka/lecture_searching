import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as data_file:
        data=json.load(data_file)
    for key in data.keys():
        if field == key:
            sequential_data=data[field]
            return sequential_data
    return None
def linear_search(seq,looking_for):
    splitedseq=[*seq]
    looking_for=[*looking_for]
    pozition= []
    count=0
    for idx in range(0,len(splitedseq)) :
        if splitedseq[idx:(idx+len(looking_for))]==looking_for :
            pozition.append(idx)
            count=count+1
    return pozition,count
def main():
    sequential_data= read_data("sequential.json","dna_sequence")
    print(sequential_data)
    searching_for="GA"
    search_for = linear_search(sequential_data,searching_for)
    print(search_for)

if __name__ == '__main__':
    main()