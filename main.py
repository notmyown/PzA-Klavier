def on_pin_touch_p1():
    if input.button_is_pressed(Button.A):
        music.play_tone(440, music.beat(BeatFraction.HALF))
    else:
        music.play_tone(294, music.beat(BeatFraction.HALF))
input.on_pin_touch_event(TouchPin.P1, input.button_event_down(), on_pin_touch_p1)

def on_button_b():
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_pin_touch_p0():
    if input.button_is_pressed(Button.A):
        music.play_tone(392, music.beat(BeatFraction.HALF))
    else:
        music.play_tone(262, music.beat(BeatFraction.HALF))
input.on_pin_touch_event(TouchPin.P0, input.button_event_down(), on_pin_touch_p0)

def on_pin_touch_p2():
    music.play_tone(330, music.beat(BeatFraction.HALF))
input.on_pin_touch_event(TouchPin.P2, input.button_event_down(), on_pin_touch_p2)

def on_pin_touch_p3():
    music.play_tone(349, music.beat(BeatFraction.HALF))
input.on_pin_touch_event(TouchPin.P3, input.button_event_down(), on_pin_touch_p3)
