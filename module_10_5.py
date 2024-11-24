import time
import datetime
from multiprocessing import Pool


def convert_seconds(seconds):
    return str(datetime.timedelta(seconds=seconds))


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# ---------------------------------Линейный вызов----------------------------

time_start = time.time()

for filename in filenames:
    read_info(filename)

time_stop = time.time()
ellapsed_time = time_stop - time_start
print(f'{convert_seconds(ellapsed_time)} (линейный)')

# ---------------------------------Многопроцессный----------------------------

# if __name__ == '__main__':
#     time_start = time.time()
#     with Pool() as p:
#         p.map(read_info, filenames)
#
#     time_stop = time.time()
#     ellapsed_time = time_stop - time_start
#     print(f'{convert_seconds(ellapsed_time)} (многопроцессный)')
