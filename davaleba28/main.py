from abc import ABC, abstractmethod


# Interface defining basic media player functionality
class MediaPlayerInterface(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Interface for recorded media with additional playback features
class RecordedMediaInterface(MediaPlayerInterface):
    @abstractmethod
    def reverse(self):
        pass

    @abstractmethod
    def fastForward(self):
        pass


# class implementing an audio player
class AudioPlayer(RecordedMediaInterface):
    def __init__(self, audiofile):
        self.audiofile = audiofile

    def play(self):
        print(f"Start playing {self.audiofile}")

    def pause(self):
        print(f"{self.audiofile} is paused")

    def stop(self):
        print(f"{self.audiofile} has been stopped")

    def reverse(self, seconds=15):
        if seconds < 0:
            raise ValueError("Seconds must be positive")
        print(f"{self.audiofile} reversed to {seconds} seconds")

    def fastForward(self, seconds=15):
        if seconds < 0:
            raise ValueError("Seconds must be positive")
        print(f"{self.audiofile} fast forwarded by {seconds} seconds")


# class implementing a video player
class VideoPlayer(RecordedMediaInterface):
    def __init__(self, videofile):
        self.videofile = videofile

    def play(self):
        print(f"Start playing {self.videofile}")

    def pause(self):
        print(f"{self.videofile} is paused")

    def stop(self):
        print(f"{self.videofile} has been stopped")

    def reverse(self, seconds=15):
        if seconds < 0:
            raise ValueError("Seconds must be positive")
        print(f"{self.videofile} reversed to {seconds} seconds")

    def fastForward(self, seconds=15):
        if seconds < 0:
            raise ValueError("Seconds must be positive")
        print(f"{self.videofile} fast forwarded by {seconds} seconds")


# class implementing a stream player
class StreamPlayer(MediaPlayerInterface):
    def __init__(self, streamfile):
        self.streamfile = streamfile

    def play(self):
        print(f"Streaming {self.streamfile}")

    def pause(self):
        print(f"{self.streamfile} is paused")

    def stop(self):
        print(f"{self.streamfile} has been stopped")


# Usage examples
audio = AudioPlayer("'I am an Audio'")
audio.play()
audio.reverse(20)
audio.stop()
print()

video = VideoPlayer("'I am a Video'")
video.play()
video.fastForward()
video.stop()
print()

stream = StreamPlayer("'I am a Livestream'")
stream.play()
stream.stop()
