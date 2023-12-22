import tkinter as tk
from Model.Gridworld import runIteration
from numpy.random import choice

# Create main window
root = tk.Tk()
root.title("5x5 Grid with Line Arrows in Cells")

# Create a Canvas widget for the grid
canvas = tk.Canvas(root, width=250, height=250)
canvas.pack(side=tk.LEFT)

def generate_grid(pi_grid):
    #for widget in root.winfo_children():
    #    widget.destroy()  # Clear existing widgets

    # Create cells in the grid
    cell_size = 50
    for i in range(5):
        for j in range(5):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            cell_id = canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags=f"cell_{i}_{j}")
            #canvas.tag_bind(cell_id, '<Button-1>', on_cell_click)

            # Draw arrow as a line inside the cell
            #arrow = x_start, y_start, x_end, y_end
            if(pi_grid[i*5+j]==0):
                arrow = [x1, (y1+y2)/2, x2, (y1+y2)/2]
            if(pi_grid[i*5+j]==1):
                arrow = [x2,(y1+y2)/2, x1,(y1+y2)/2]
            if(pi_grid[i*5+j]==2):
                arrow = [(x1+x2)/2, y1, (x1+x2)/2, y2]
            if(pi_grid[i*5+j]==3):
                arrow = [(x1+x2)/2, y2, (x1+x2)/2, y1]
            canvas.create_line(arrow[0], arrow[1], arrow[2], arrow[3], arrow="last", width=2, fill="black")


perf = -100
actions = [0,1,2,3]
pi = [0]*25
for j in range(25):
    pi[j] = choice(actions,p=[0.25,0.25,0.25,0.25])

generate_grid(pi)
# Function to handle button click
def on_button_click():
    global pi, perf
    [pi,perf] = runIteration(pi,perf)
    print(perf, pi)
    generate_grid(pi)


# Create a Button widget on the side
button = tk.Button(root, text=f"{perf}", command=on_button_click)
button.pack(side=tk.RIGHT, padx=10, pady=10)
"""
# Create cells in the grid
cell_size = 50
for i in range(5):
    for j in range(5):
        x1, y1 = j * cell_size, i * cell_size
        x2, y2 = x1 + cell_size, y1 + cell_size
        cell_id = canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags=f"cell_{i}_{j}")
        #canvas.tag_bind(cell_id, '<Button-1>', on_cell_click)

        # Draw arrow as a line inside the cell
        arrow_start_x = (x1 + x2) / 2
        arrow_start_y = y1
        arrow_end_x = (x1 + x2) / 2
        arrow_end_y = y2
        canvas.create_line(arrow_start_x, arrow_start_y, arrow_end_x, arrow_end_y, arrow="last", width=2, fill="black")
"""
# Run the main loop
root.mainloop()
