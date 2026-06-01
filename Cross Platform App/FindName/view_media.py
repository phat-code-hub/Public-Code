import os
import subprocess
import tempfile
import hashlib

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer

from FindName.languages import *
from FindName.constants import DEFAULT_CONFIG,STATES
from FindName import MAX_VOL
# ============================================================
#  FLV → MP4 conversion with caching
# ============================================================

CACHE_DIR = os.path.join(tempfile.gettempdir(), "media_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

def get_cache_name(filepath):
    """Generate unique MP4 cache name based on original FLV path."""
    h = hashlib.md5(filepath.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, h + ".mp4")

def convert_flv(filepath):
    """Convert FLV → MP4 using FFmpeg (stream copy: fast, lossless)."""
    cached = get_cache_name(filepath)

    # If cached file exists → return immediately
    if os.path.exists(cached):
        return cached

    # Convert FLV → MP4
    cmd = [
        "ffmpeg", "-y",
        "-i", filepath,
        "-vcodec", "copy",
        "-acodec", "copy",
        cached
    ]

    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return cached if os.path.exists(cached) else None
    except Exception:
        return None

# ============================================================
#  Main media handler (with FLV support)
# ============================================================

def main_media(self, filepath, ext, ord):

    self.player.setVideoOutput(self.video_widget)
    self.player.setAudioOutput(self.audio_output)

    # ----------------------------------------------------
    #  Step 1: Detect FLV → convert automatically
    # ----------------------------------------------------
    if ext.lower() == ".flv":
        self.image_view.setText(f'{PREVIEW["Media"]["FLV"][self.language]}')
        self.image_view.setAlignment(Qt.AlignCenter)
        self.preview_top.setCurrentWidget(self.image_view)

        converted = convert_flv(filepath)
        if not converted:
            self.image_view.setText(f'{PREVIEW["Media"]["Convert"][self.language]}')
            self.image_view.setAlignment(Qt.AlignCenter)
            self.preview_top.setCurrentWidget(self.image_view)
            return

        filepath = converted  # Use converted MP4

    # ----------------------------------------------------
    #  Step 2: Normal media loading
    # ----------------------------------------------------
    try:
        self.image_view.setText(f'{PREVIEW["Media"]["Prepare"][self.language]}')
        self.image_view.setAlignment(Qt.AlignCenter)
        self.preview_top.setCurrentWidget(self.image_view)
        self.player.setSource(QUrl.fromLocalFile(filepath))
        self.player.setPosition(0)
        reset_media_ui(self, enabled=True)

    except Exception:
        self.play_button.setText(LABELS[self.language]["Play"])
        self.image_view.setText(f'{PREVIEW["Media"]["Failed"][self.language]}')
        self.image_view.setAlignment(Qt.AlignCenter)
        self.preview_top.setCurrentWidget(self.image_view)


# ============================================================
# Existing functions (unchanged)
# ============================================================

def media_play_or_pause(self):
    if self.player.playbackState() == QMediaPlayer.PlayingState:
        media_state(self, STATES["Playing"])
        self.player.pause()
    else:
        media_state(self, STATES["Paused"])
        self.player.play()

#--------------------------------------------------------------
def media_stop(self):
    reset_media_ui(self)
#-------------------------------------------------------------

def on_volume_changed(self, value):
    normalized = value / MAX_VOL
    volume = min(1.0, normalized ** 1.5)
    self.audio_output.setVolume(volume)
#-------------------------------------------------------------
#-------------------------------------------------------------
def toggle_mute(self, checked):
    if checked:
        media_state(self, STATES["Muted"])
    else:
        media_state(self, STATES["Unmuted"])

#-------------------------------------------------------------
def on_slider_pressed(self):
    self.is_seeking = True
    self.was_playing = (self.player.playbackState() == QMediaPlayer.PlayingState)
    self.player.pause()

#-------------------------------------------------------------
def on_slider_released(self):
    self.is_seeking = False
    self.player.setPosition(self.seek_slider.value())
    if self.was_playing:
        self.player.play()
#-------------------------------------------------------------

def on_duration_changed(self, duration):
    self.seek_slider.setRange(0, duration)
    self.seek_slider.setEnabled(True)
#-------------------------------------------------------------

def format_time(self, ms):
    s = ms // 1000
    return f"{s//60:02d}:{s%60:02d}"
#-------------------------------------------------------------

def update_time_label(self, position):
    cur = format_time(self, position)
    total = format_time(self, self.player.duration())
    self.timer.setText(f"{cur} / {total}")
#-------------------------------------------------------------

def on_position_changed(self, pos):
    if self.is_seeking:
        return
    self.seek_slider.setValue(pos)
    update_time_label(self, pos)

#-------------------------------------------------------------
def show_media_thumbnail(self, filepath):
    base, ext = os.path.splitext(filepath)
    for candidate_ext in (".jpg", ".jpeg", ".png", ".bmp"):
        candidate = base + candidate_ext
        if os.path.exists(candidate):
            pix = QPixmap(candidate)
            self.image_view.setPixmap(
                pix.scaled(
                    max(1, self.preview_top.width()),
                    max(1, self.preview_top.height()),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )
            self.preview_top.setCurrentWidget(self.image_view)
            return

    self.text_view.setText(f"[Media file]\n{os.path.basename(filepath)}")
    self.preview_top.setCurrentWidget(self.text_view)
#-------------------------------------------------------------

def reset_media_ui(self, enabled=True):
    if self.player.playbackState() != QMediaPlayer.StoppedState:
        self.player.stop()
    
    self.play_button.setText(LABELS[self.language]["Play"])
    self.mute_button.setText(LABELS[self.language]["Mute"])
    self.mute_button.setChecked(False)

    self.seek_slider.setEnabled(False)
    self.seek_slider.setValue(0)
    self.timer.setText("00:00 / 00:00")

    try:
        self.player.setVideoOutput(None)
        self.player.setVideoOutput(self.video_widget)
    except Exception:
        pass

    self.play_button.setEnabled(enabled)
    self.stop_button.setEnabled(enabled)
    self.mute_button.setEnabled(enabled)
    self.volume_slider.setEnabled(enabled)
    self.seek_slider.setEnabled(enabled)

#-------------------------------------------------------------
def media_state(self, state=0, enabled=True):
    if state == STATES["Selected"]:
        pass
    elif state == STATES["Playing"]:
        self.play_button.setText(LABELS[self.language]["Play"])
    elif state == STATES["Paused"]:
        self.play_button.setText(LABELS[self.language]["Paused"])
    elif state == STATES["Stopped"]:
        self.play_button.setText(LABELS[self.language]["Stop"])
        reset_media_ui(self, enabled=False)
    elif state == STATES["Muted"]: 
        self.audio_output.setMuted(True)
        self.mute_button.setText(LABELS[self.language]["Unmute"])
    elif state == STATES["Unmuted"]:
        self.audio_output.setMuted(False)
        self.mute_button.setText(LABELS[self.language]["Mute"])
