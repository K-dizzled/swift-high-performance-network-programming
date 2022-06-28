from graphing import *
import plotly.graph_objects as go

java_vmem_src = open("java.2022-05-24_03-00.vmem_profiling.txt", "r")
data_vmem_java = java_vmem_src.read()

swift_vmem_src = open("swift.2022-05-24_03-04.vmem_profiling.txt", "r")
data_vmem_swift = swift_vmem_src.read()

java_cpu_src = open("java.2022-05-24_03-00.cpu_profiling.txt", "r")
data_cpu_java = java_cpu_src.read()

swift_cpu_src = open("swift.2022-05-24_03-04.cpu_profiling.txt", "r")
data_cpu_swift = swift_cpu_src.read()

data_vmem_java = data_vmem_java.split('\n')[:-33]
data_vmem_swift = data_vmem_swift.split('\n')[1:-94]
data_cpu_java = data_cpu_java.split('\n')[:-33]
data_cpu_swift = data_cpu_swift.split('\n')[1:-94]

for i in range (0, 99):
    data_vmem_java[i] = float(data_vmem_java[i])
    data_vmem_swift[i] = float(data_vmem_swift[i])
    data_cpu_java[i] = float(data_cpu_java[i])
    data_cpu_swift[i] = float(data_cpu_swift[i])    

first = [i for i in range(1, 100)]

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()
fig.write_image("metric3_final.pdf")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=first,
    y=data_cpu_swift,
    name="SwiftNIO"
))


fig.add_trace(go.Scatter(
    x=first,
    y=data_cpu_java,
    name="Netty"
))

fig.update_layout(
    title="Метрика №3",
    xaxis_title="Секунды",
    yaxis_title="Нагрузка на CPU",
    legend_title="Фреймворки",
    font=dict(
        size=12,
    )
)

fig.show()
fig.write_image("metric3_final.pdf")

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()
fig.write_image("metric4_final.pdf")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=first,
    y=data_vmem_swift,
    name="SwiftNIO"
))


fig.add_trace(go.Scatter(
    x=first,
    y=data_vmem_java,
    name="Netty"
))

fig.update_layout(
    title="Метрика №4",
    xaxis_title="Секунды",
    yaxis_title="Виртуальной памяти задействовано",
    legend_title="Фреймворки",
    font=dict(
        size=12,
    )
)

fig.show()
fig.write_image("metric4_final.pdf")