from bokeh.plotting import figure, output_file, show
from math import pi


fig = figure()
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

def graficar_circle():
  x = 0
  y = 0
  radius = 1
  start_angles = [0, pi / 2, pi, 3 * pi / 2]
  end_angles = [pi / 2, pi, 3 * pi / 2, 2 * pi]
  colors = ["red", "blue", "green", "yellow"]

  # Crear figura
  fig = figure(
      title="4 Secciones en un Círculo", x_range=(-1.5, 1.5), y_range=(-1.5, 1.5)
  )

  # Graficar secciones
  for start_angle, end_angle, color in zip(start_angles, end_angles, colors):
      fig.wedge(x, y, radius, start_angle, end_angle, color=color)
  
  # Mostrar la figura
  output_file("graficado_circle.html")
  show(fig)


def graficar_line(x, y, color):
    fig.line(x, y, line_width=2, color=color)
    output_file("graficado_line.html")
    show(fig)


def graficar_square(x, y, color):
    fig.scatter(x, y, size=10, color=color, marker='square')
    output_file("graficado_square.html")
    show(fig)


if __name__ == '__main__':
    graficar_circle()
    graficar_line(x, y, 'blue')
    graficar_square(x, y, 'green')

