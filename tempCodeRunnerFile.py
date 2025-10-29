btn_font = ctk.CTkFont(size=16, weight="bold")

start_btn = ctk.CTkButton(btn_frame, text="Start", fg_color="#28a745", text_color="white", height=42, font=btn_font)
start_btn.pack(side="left", expand=True, padx=5)

stop_btn = ctk.CTkButton(btn_frame, text="Stop", fg_color="#dc3545", text_color="white", height=42, font=btn_font)
stop_btn.pack(side="left", expand=True, padx=5)

render_btn = ctk.CTkButton(btn_frame, text="Render", fg_color="#0d6efd", text_color="white", height=42, font=btn_font)
render_btn.pack(side="left", expand=True, padx=5)