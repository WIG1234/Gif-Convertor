import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, concatenate_videoclips

def select_gif():
    gif_path = filedialog.askopenfilename(title="Select GIF File", filetypes=[("GIF files", "*.gif")])
    gif_entry.delete(0, tk.END)  # Clear the entry
    gif_entry.insert(0, gif_path)  # Insert the selected path

def convert_gif_to_mp4():
    gif_path = gif_entry.get()
    loops = loop_entry.get()

    if not gif_path:
        messagebox.showerror("Error", "Please select a GIF file.")
        return
    
    try:
        loop_count = int(loops)
        if loop_count <= 0:
            raise ValueError("Number of loops must be a positive integer.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    # Prompt user to choose the output file path and name
    video_path = filedialog.asksaveasfilename(
        defaultextension=".mp4", 
        filetypes=[("MP4 files", "*.mp4")],
        title="Save As"
    )

    if not video_path:  # If the user cancels the dialog
        return

    try:
        # Convert GIF to VideoFileClip
        clip = VideoFileClip(gif_path)

        # Repeat the clip as specified
        looped_clip = concatenate_videoclips([clip] * loop_count)

        # Write the looped video to the specified MP4 file
        looped_clip.write_videofile(video_path, codec="libx264", fps=clip.fps)

        messagebox.showinfo("Success", f"Converted to {video_path} successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("GIF to MP4 Converter")

# Create and place the widgets
gif_label = tk.Label(root, text="Select GIF File:")
gif_label.pack(pady=5)

gif_entry = tk.Entry(root, width=50)
gif_entry.pack(pady=5)

browse_button = tk.Button(root, text="Browse", command=select_gif)
browse_button.pack(pady=5)

loop_label = tk.Label(root, text="Number of Loops:")
loop_label.pack(pady=5)

loop_entry = tk.Entry(root, width=5)
loop_entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert to MP4", command=convert_gif_to_mp4)
convert_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
