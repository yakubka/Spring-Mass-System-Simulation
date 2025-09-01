import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation
from matplotlib.patches import FancyBboxPatch
from scipy.integrate import solve_ivp
from matplotlib.widgets import Slider
g = 9.81
k_max = 1000
x0, x_dot0 = 0, 0
t_final = 10
fps = 60
state = {'spring_broken': False}

params = {'k': 100, 'm': 1, 'b': 0.25, 'xmax': 1}
def spring_mass_ODE(t, y):
    x, x_dot = y
    return [x_dot, g - params['k']*x/params['m'] - params['b']*x_dot/params['m']]

def solve_system():
    t_eval = np.linspace(0, t_final, t_final*fps + 1)
    sol = solve_ivp(spring_mass_ODE, [0,t_final], [x0, x_dot0], t_eval=t_eval)
    return sol.t, sol.y[0]

t_values, x_values = solve_system()
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1,1)
ax.set_ylim(-2,2)
ax.set_xticks([])
ax.set_yticks(np.linspace(-2,2,5))
n_points = 10
spring_length = 0.2
def generate_spring(n,length,stretch_factor=2):
    data = np.zeros((2,n+2))
    data[1,:] = np.linspace(0, -length*stretch_factor, n+2)
    data[0,1:-1:2] = 0.2
    data[0,2:-1:2] = -0.2
    return data

data = generate_spring(n_points,spring_length,stretch_factor=4)
spring = Line2D(data[0], data[1], color='white', linewidth=3)
y_fixation = 1.8
fixation_line = Line2D([-0.5,0.5],[y_fixation,y_fixation], color='white', linewidth=4)
square_width, square_height = 0.5, 0.5
initial_square_y = y_fixation - spring_length - square_height - 0.13
square = FancyBboxPatch(
    (-square_width/2, initial_square_y - square_height),
    square_width, square_height,
    boxstyle="round,pad=0.04,rounding_size=0.1",
    fc='blue', ec='black', linewidth=1
)

ax.add_line(spring)
ax.add_patch(square)
ax.add_line(fixation_line)
new_data = data.copy()
axcolor = 'lightgoldenrodyellow'
ax_k = plt.axes([0.15, 0.25, 0.7, 0.03], facecolor=axcolor)
ax_m = plt.axes([0.15, 0.20, 0.7, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.15, 0.15, 0.7, 0.03], facecolor=axcolor)
ax_xmax = plt.axes([0.15, 0.10, 0.7, 0.03], facecolor=axcolor)

slider_k = Slider(ax_k, 'k', 10, 2000, valinit=params['k'])
slider_m = Slider(ax_m, 'm', 0.1, 10, valinit=params['m'])
slider_b = Slider(ax_b, 'b', 0, 5, valinit=params['b'])
slider_xmax = Slider(ax_xmax, 'xmax', 0.05, 5, valinit=params['xmax'])
def check_spring_break(x_val):
    return abs(x_val) > params['xmax'] or params['k']*abs(x_val) > k_max*params['xmax']

def animate(i):
    global t_values, x_values
    if state['spring_broken']:
        y_square = square.get_y() - 0.05
        y_square = max(y_square,-2)
        square.set_y(y_square)
        return spring, square

    y_square = initial_square_y - x_values[i] - square_height
    y_square = max(y_square,-2)
    square.set_y(y_square)

    new_data[1,:] = data[1,:]*(y_fixation-(y_square+square_height))/(y_fixation-initial_square_y)
    new_data[1,:] += y_fixation
    spring.set_data(new_data[0], new_data[1])

    if check_spring_break(x_values[i]):
        spring.set_color('red')
        state['spring_broken'] = True
    else:
        spring.set_color('white')

    return spring, square

ani = FuncAnimation(fig, animate, frames=len(t_values), interval=1000/fps, blit=True)
def update(val):
    params['k'] = slider_k.val
    params['m'] = slider_m.val
    params['b'] = slider_b.val
    params['xmax'] = slider_xmax.val
    state['spring_broken'] = False
    global t_values, x_values
    t_values, x_values = solve_system()
    square.set_y(initial_square_y)

slider_k.on_changed(update)
slider_m.on_changed(update)
slider_b.on_changed(update)
slider_xmax.on_changed(update)

plt.show()

