class Video:

    def create(self, name):
        self.name = name

    def play(self):
        return f'воспроизведение видео {self.name}'

class YouTube:
    videos = list()

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        return cls.videos[video_indx].play()

v1 = Video()
v2 = Video()

v1.create('Python')
v2.create('Python ООП')

YouTube.add_video(v1)
YouTube.add_video(v2)
print(YouTube.play(0))
print(YouTube.play(1))

