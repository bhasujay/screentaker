import customtkinter as ctk
from capture import *
from render import *
from time import sleep

# Capture Manager Instance
capture_manager = CaptureManager()
render_manager = RenderManager()

# Button Actions
def start_action():
    capture_manager.listen_to_clipboard()
    status.configure(text="Status: Listening to clipboard...")
    stop_btn.configure(state="normal")
    start_btn.configure(state="disabled")

def stop_action():
    capture_manager.close_clipboard_listener()
    status.configure(text=f"Status: captured {capture_manager.image_count} images")
    stop_btn.configure(state="disabled")
    render_btn.configure(state="normal")
    progress.configure(mode="indeterminate")
    progress.start()

def render_action():
    global capture_manager  # Make sure to use the global variable
    
    progress.set(0)
    status.configure(text="Status: Rendering...")

    total = capture_manager.image_count
    for i in range(total):
        progress.set((i + 1) / total)
        root.update_idletasks()
        
    status.configure(text="Status: Rendering complete!")

    # Destroy and recreate the capture_manager object
    del capture_manager
    capture_manager = CaptureManager()


# Main Window
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Screentaker")
root.geometry("500x200")
root.resizable(False, False)

title = ctk.CTkLabel(root, text="Screentaker", font=ctk.CTkFont(size=20, weight="bold"))
title.pack(pady=10)

btn_frame = ctk.CTkFrame(root, fg_color="transparent")
btn_frame.pack(pady=10, padx=10, fill="x")

btn_font = ctk.CTkFont(size=16, weight="bold")

start_btn = ctk.CTkButton(btn_frame, text="Start", fg_color="#139832", hover_color="#14732a", text_color="white", height=42, font=btn_font)
start_btn.pack(side="left", expand=True, padx=5)

stop_btn = ctk.CTkButton(btn_frame, text="Stop", fg_color="#dc3545", hover_color="#731b24", text_color="white", height=42, font=btn_font)
stop_btn.pack(side="left", expand=True, padx=5)

render_btn = ctk.CTkButton(btn_frame, text="Render", fg_color="#0d6efd", hover_color="#133567", text_color="white", height=42, font=btn_font)
render_btn.pack(side="left", expand=True, padx=5)

progress = ctk.CTkProgressBar(root, width=460)
progress.pack(pady=10)
progress.set(0)

status = ctk.CTkLabel(root, text="Status: Idle", text_color="#6b7280")
status.pack(pady=5)

start_btn.configure(command=start_action)
stop_btn.configure(command=stop_action)
render_btn.configure(command=render_action)

# Disable Stop and Render buttons on startup
stop_btn.configure(state="disabled")
render_btn.configure(state="disabled")

root.mainloop()