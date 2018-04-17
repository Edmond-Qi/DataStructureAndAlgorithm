# import gevent
#
#
# def compute_sum(start, end):
#     global sum1
#     sum1 = sum([i for i in range(start, end + 1)])
#
#
# if __name__ == "__main__":
#     sum1 = 0
#     gevent.joinall([gevent.spawn(compute_sum, 0, 100)])
#     print(sum1)


import gevent
import os
from gevent import monkey

monkey.patch_all()


def copy_file(start, end):
    with open("Video_2018-01-19_091805.wmv", "rb") as f:
        f.seek(start)
        content = f.read(end - start)
        with open("Video.wmv", "ab+") as f1:
            f1.seek(start)
            f1.write(content)


if __name__ == "__main__":
    file_name = "Video_2018-01-19_091805.wmv"
    size = os.path.getsize(file_name)
    number = 4
    block = size // number
    for i in range(number):
        if i != number - 1:
            gevent.joinall([gevent.spawn(copy_file, *(i * block, (i + 1) * block))])
        else:
            gevent.joinall([gevent.spawn(copy_file, *(i * block, size))])
