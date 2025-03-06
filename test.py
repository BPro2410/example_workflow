#

print("HELLO")

import numpy as np
np.__version__

import pandas as pd
pd.__version__

import matplotlib
matplotlib.__version__

import matplotlib.pyplot as plt

import tensorflow as tf
tf.__version__

import tensorflow_probability as tfp
tfp.__version__

import cmake
cmake.__version__



from seededpf import SPF
print("HELLO")

# Example documents - customer reviews about either smartphones or computers
documents = [
    "My smartphone's battery life is fantastic, lasts all day!",
    "The camera on my phone is incredible, takes crystal-clear photos.",
    "Love the smooth performance, but it overheats with heavy apps.",
    "This phone charges super fast, very convenient.",
    "Upgraded my PC and it boots in seconds!",
    "Great for gaming, but gets hot after long sessions.",
    "My computer sometimes freezes, but a restart fixes it.",
    "Best laptop I’ve owned, powerful and reliable!"
]

# Define topic-specific seed words
smartphone = {"smartphone", "iphone", "phone", "touch", "app"}
pc = {"laptop", "keyboard", "desktop", "pc"}

keywords = {"smartphone": smartphone, "pc": pc}

spf = SPF(keywords = keywords)
spf