import tensorflow as tf
from exAmple2410.helper import helper

class sum_tf:
    def __init__(self, numbers):
        print("HELLO")
        for i in numbers:
            helper.checknumber(i)
        self.sum = tf.reduce_sum(numbers)

