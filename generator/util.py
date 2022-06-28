from graphing import *
import plotly.graph_objects as go

java_src = open("aux1.txt", "r")
data_java = java_src.read()

swift_src = open("auux.txt", "r")
data_swift = swift_src.read()

first = [None for i in range(80)]
second_s = [None for i in range(80)]
second_j = [None for i in range(80)]
third_s = [None for i in range(80)]
third_j = [None for i in range(80)]

data_java = data_java.split('\n')
data_swift = data_swift.split('\n')

for i in range(len(data_java)):
    data_java[i] = data_java[i].split(' ')
    data_swift[i] = data_swift[i].split(' ')

    first[i] = float(data_swift[i][0])
    second_s[i] = float(data_swift[i][1])
    second_j[i] = float(data_java[i][1])

    third_s[i] = float(data_swift[i][2])
    third_j[i] = float(data_java[i][2])

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()
fig.write_image("metric1_final.pdf")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=first,
    y=second_s,
    name="SwiftNIO"
))


fig.add_trace(go.Scatter(
    x=first,
    y=second_j,
    name="Netty"
))

fig.update_layout(
    title="Метрика №1",
    xaxis_title="Количество клиентов",
    yaxis_title="Среднее полученное количество мегабайт",
    legend_title="Фреймворки",
    font=dict(
        size=18,
    )
)

fig.show()
fig.write_image("metric1_final.pdf")

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()
fig.write_image("metric2_final.pdf")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=first,
    y=third_s,
    name="SwiftNIO"
))


fig.add_trace(go.Scatter(
    x=first,
    y=third_j,
    name="Netty"
))

fig.update_layout(
    title="Метрика №2",
    xaxis_title="Количество клиентов",
    yaxis_title="Отклонение от полученного количества мегабайт",
    legend_title="Фреймворки",
    font=dict(
        size=12,
    )
)

fig.show()
fig.write_image("metric2_final.pdf")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=first,
    y=second_s,
    name="SwiftNIO"
))


fig.add_trace(go.Scatter(
    x=first,
    y=second_j,
    name="Netty"
))

fig.update_layout(
      title="Метрика №1",
    xaxis_title="Количество клиентов",
    yaxis_title="Среднее полученное количество мегабайт",
    legend_title="Фреймворки",
    font=dict(
        size=12,
    )
)

fig.show()
fig.write_image("metric1_final.pdf")