import plotly.express as px
from datetime import datetime
import pandas as pd
from generator_config import *

def plot_graph1(x_data, y_data): 
    df = pd.DataFrame(dict(
        x = x_data,
        y = y_data
    ))

    fig = px.line(df, x="x", y="y",
                  labels={
                         "x": "Amount of clients",
                         "y": "Average recieved in megabytes"
                     },
                  title="%s. Performance metric №1" % (language.capitalize())
                  ) 
    fig.show()

    date_time = datetime.now()
    date_str = date_time.strftime("%Y-%m-%d_%H-%M")

    fig.write_image("%s.plot.%s.png" % (language, date_str))


def plot_graph2(): 
    data_src = open("cpu_profiling.txt", "r")
    data = data_src.read()
    data = data.split('\n')
    data = data[1:-1]
    data = [float(el) for el in data]

    df = pd.DataFrame(dict(
        x = [i for i in range(1, len(data) + 1)],
        y = data
    ))

    fig = px.line(df, x="x", y="y",
                  labels={
                         "x": "Time in seconds",
                         "y": "CPU load percentage"
                     },
                  title="%s. Performance metric №2" % (language.capitalize())
                  ) 
    fig.show()

    date_time = datetime.now()
    date_str = date_time.strftime("%Y-%m-%d_%H-%M")

    fig.write_image("%s.plot_cpu.%s.png" % (language, date_str))


def plot_graph3(x_data, y_data): 
    df = pd.DataFrame(dict(
        x = x_data,
        y = y_data
    ))


    fig = px.line(df, x="x", y="y",
                  labels={
                         "x": "Amount of clients",
                         "y": "Standard deviation in megabytes"
                     },
                  title="%s. Performance metric №3" % (language.capitalize())
                  ) 
    fig.show()

    date_time = datetime.now()
    date_str = date_time.strftime("%Y-%m-%d_%H-%M")

    fig.write_image("%s.plot_std.%s.png" % (language, date_str))


def plot_graph4(): 
    data_src = open("vmem_profiling.txt", "r")
    data = data_src.read()
    data = data.split('\n')
    data = data[1:-1]
    data = [float(el) for el in data]

    df = pd.DataFrame(dict(
        x = [i for i in range(1, len(data) + 1)],
        y = data
    ))

    fig = px.line(df, x="x", y="y",
                  labels={
                         "x": "Time in seconds",
                         "y": "Used virtual memory"
                     },
                  title="%s. Performance metric №4" % (language.capitalize())
                  ) 
    fig.show()

    date_time = datetime.now()
    date_str = date_time.strftime("%Y-%m-%d_%H-%M")

    fig.write_image("%s.plot_vmem.%s.png" % (language, date_str))
