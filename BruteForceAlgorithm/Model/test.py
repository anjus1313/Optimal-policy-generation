import tkinter as tk

# Function to handle cell click
def on_cell_click(event):
    cell_id = event.widget.find_withtag(tk.CURRENT)
    if cell_id:
        cell = cell_id[0]
        row, col = divmod(cell - 1, 5)  # Calculate row and column
        print(f"Cell clicked at row {row + 1}, column {col + 1}")

# Function to handle button click
def on_button_click():
    print("Button clicked!")

# Create main window
root = tk.Tk()
root.title("5x5 Grid with Cells and Button")

# Create a Canvas widget for the grid
canvas = tk.Canvas(root, width=250, height=250)
canvas.pack(side=tk.LEFT)

# Create cells in the grid
cell_size = 50
for i in range(5):
    for j in range(5):
        x1, y1 = j * cell_size, i * cell_size
        x2, y2 = x1 + cell_size, y1 + cell_size
        cell_id = canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags=f"cell_{i}_{j}")
        canvas.tag_bind(cell_id, '<Button-1>', on_cell_click)

# Create a Button widget on the side
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the main loop
root.mainloop()
