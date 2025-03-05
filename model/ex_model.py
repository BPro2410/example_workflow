import tensorflow as tf
from model.helper import helper

class sum_tf:
    def __init__(self, numbers):
        for i in numbers:
            helper.checknumber(i)
        self.sum = tf.reduce_sum(numbers)

