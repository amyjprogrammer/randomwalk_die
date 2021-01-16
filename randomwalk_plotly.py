import plotly.graph_objects as go

from randomwalk import RandomWalk

#Keep making new walks
while True:
    #Creating the walk
    rw = RandomWalk()
    rw.fill_walk()

    fig = go.Figure(data=go.Scattergl(
        x = rw.x_values,
        y = rw.y_values,
        mode='markers',
        marker=dict(
            colorscale = 'Viridis',
            line_width = 1,
        )
    ))

    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
