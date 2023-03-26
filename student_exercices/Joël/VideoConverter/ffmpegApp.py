import tkinter as tk
from tkinter import filedialog
import ffmpeg #ffmpeg-python

LARGE_FONT = ("Verdana", 12)
ser = None
file = None


class ffmpegApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # for F in (StartPage):

        #     frame = F(container,self)

        #     self.frames[F] = frame

        #     frame.grid(row = 0, column = 0, sticky = "nsew")
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Test Joel", font=LARGE_FONT)
        label.grid(row=0, column=0)

        # definition
        w = 10
        fps_list = []
        for i in range(6):
            fps_list.append(str(i * 10 + 4))
        codec_list = ["x264", "x265"]
        tkvar_codec = tk.StringVar(self)
        tkvar_codec.set(codec_list[0])
        tkvar_fps = tk.StringVar(self)
        tkvar_fps.set(fps_list[0])
        self.btn_browse = tk.Button(self, text="Browse to directory", command=lambda: self.browse_button(), height=3,
                                    width=20)
        self.btn_start = tk.Button(self, text="Start it!", command=lambda: self.start_button(), height=3, width=20)
        self.btn_safe = tk.Button(self, text="Browse to directory", command=lambda: self.save_button(), height=3,
                                  width=20)
        self.drp_fps = tk.OptionMenu(self, tkvar_fps, *fps_list)
        self.drp_codec = tk.OptionMenu(self, tkvar_codec, *codec_list)
        self.ePort5 = tk.Entry(self, width=w)
        self.ePort5.insert(0, "Feld5")
        # placement
        self.btn_browse.grid(row=1, column=0)
        self.btn_safe.grid(row=1, column=1)
        self.drp_fps.grid(row=2, column=0)
        self.drp_codec.grid(row=2, column=1)
        self.btn_start.grid(row=3, column=0)

    def browse_button(self):
        self.from_file = filedialog.askopenfilename()
        print(self.from_file)

    def save_button(self):
        self.to_file = filedialog.asksaveasfile()

    def start_button(self):
        print('Conversion start')
        data = ffmpeg.input(self.from_file)
        audio_stream = data.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
        video_stream = data.video.hflip()
        video_stream = ffmpeg.zoompan(video_stream, fps=5)
        result = ffmpeg.output(audio_stream, video_stream, 'C:/Users/pierr/OneDrive/Desktop/out.mp4')
        print(result)
        print('Conversion done')

        # asksaveasfile anstatt askopenfilename
        # --> button machen, als command eine methode zum speichern definieren, analog zu browse_button, aber statt filedialog.askopen wie zeile oben
