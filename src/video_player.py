"""A video player class."""

from src.video_library import VideoLibrary
from src.video import Video
from src.video_playlist import Playlist
import random
import enum

class video_state(enum.Enum):
    Playing = 1
    Pause = 2
    Stop = 3
    Continue = 4

class video_loading:
    def __init__(self):
        self.Video = None
        self.status = video_state.Stop

    def set_video(self, video, state):
        self.video = video
        self.set_status(state)

    def set_status(self, state):
        self.status = state

        if self.status == video_state.Playing:
            print("Playing video: " + self.video._title)
        elif self.status == video_state.Pause:
            print("Pausing video: " + self.video._title)
        elif self.status == video_state.Stop:
            print("Stopping video: " + self.video._title)
        elif self.status == video_state.Continue:
            print("Continuing video: " + self.video._title)

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.video_loading = video_loading()

        self.playlists = dict()
        self.userWrittenStylePlaylists = dict()

    def get_video_details(self, video):
        addition_string = ""
        #if video.flagged != None:
            #addition_string = " - FLAGGED (reason: " + video.flagged + ")"

        return str(video._title + " (" + video._video_id + ") [" + ' '.join(list(video._tags)) + "]" + addition_string)

    def Sort_video_WRT_Titles(self, videos):
        videos.sort(key = lambda x: x._title)
        return videos

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        all_vids = list(self._video_library._videos)
        for i in self.Sort_video_WRT_Titles(self._video_library.get_all_videos()):
            print(" ", self.get_video_details(i))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        vid = self._video_library.get_video(video_id)
        if vid != None:
            if self.video_loading.status == video_state.Playing:
                self.stop_video()

        video = self._video_library.get_video(video_id)
        if video != None:
            #if (video.flagged == None):
                #if self.video_loading.status != video_state.Stop:
                    #self.stop_video()

                self.video_loading.set_video(video, video_state.Playing)
            #else:
                #print("Cannot play video: Video is currently flagged (reason: " + video.flagged + ")")

        else:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""
        if self.video_loading.status != video_state.Stop:
            self.video_loading.set_status(video_state.Stop)

        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self.video_loading.status == video_state.Playing:
            self.stop_video()
        videos = self._video_library.get_all_videos()

        #if len([x for x in videos if x.flagged == None]) == 0:
            #print("No videos available")
            #return

        vid = videos[random.randint(0, len(videos)-1)]
        self.play_video(vid._video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self.video_loading.status != None:
            if self.video_loading.status != video_state.Pause:
                if self.video_loading.status != video_state.Stop:
                    self.video_loading.set_status(video_state.Pause)
                else:
                    print("Video stopped so cannot be paused:", self.video_loading.get_video(video_id)._title)

            else:
                print("Video already paused:", self.video_loading.video._title)

        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.video_loading.video != None:
            if self.video_loading.status == video_state.Pause:
                self.video_loading.set_status(video_state.Continue)
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if self.video_loading.video != None:
            if self.video_loading.status != video_state.Pause:
                if self.video_loading.status != video_state.Stop:
                    print("Currently playing:", self.get_video_details(self.video_loading.video))
                else:
                    print("No video is currently playing")
            else:
                print("Currently playing:", self.get_video_details(self.video_loading.video), "- PAUSED")
        else:
            print("--No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
