# class MediaPlayer:
#
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f"Воспроизведение {self.filename}")
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
# media1.open('filemedia1')
# media2.open('filemedia2')
# media1.play()
# media2.play()
# print(media1.__dict__)

# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         print(*filter(lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1], self.data))
#
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()
# Graph.draw(graph_1)

# class StreamData:
#     def create(self, fields, values):
#         if len(fields) == len(values):
#             for name, value in zip(fields, values):
#                 setattr(self, name, value)
#             return True
#         return False
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()
# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f"воспроизведение видео {self.name}")
#
#
# class YouTube:
#     videos = []
#
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx].play()
#
# v1 = Video()
# v2 = Video()
# v1.create('Python')
# v2.create("Python ООП")
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)


# class Translator:
#     eng_rus_dict = {}
#
#     def add(self, eng, rus):
#         self.eng_rus_dict.setdefault(eng, []).append(rus)
#
#     def remove(self, eng):
#           del self.eng_rus_dict[eng]
#
#     def translate(self, eng):
#         return self.eng_rus_dict.get(eng)
#
# tr = Translator()
# tr.add("car", "машина")
# tr.add("car", "автомобиль")
# tr.add("leaf", "лист")
# tr.add("river", "река")
# tr.add("go", "идти")
# tr.add("go", "ехать")
# tr.remove('car')
# print(*tr.translate('go'))



