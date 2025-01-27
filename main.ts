input.onPinTouchEvent(TouchPin.P1, input.buttonEventDown(), function () {
    if (input.buttonIsPressed(Button.A)) {
        music.playTone(440, music.beat(BeatFraction.Half))
    } else {
        music.playTone(294, music.beat(BeatFraction.Half))
    }
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(294, music.beat(BeatFraction.Half))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(330, music.beat(BeatFraction.Whole))
    music.playTone(330, music.beat(BeatFraction.Whole))
    music.playTone(294, music.beat(BeatFraction.Half))
    music.playTone(294, music.beat(BeatFraction.Half))
    music.playTone(294, music.beat(BeatFraction.Half))
    music.playTone(294, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Whole))
})
input.onPinTouchEvent(TouchPin.P0, input.buttonEventDown(), function () {
    if (input.buttonIsPressed(Button.A)) {
        music.playTone(392, music.beat(BeatFraction.Half))
    } else {
        music.playTone(262, music.beat(BeatFraction.Half))
    }
})
input.onPinTouchEvent(TouchPin.P2, input.buttonEventDown(), function () {
    music.playTone(330, music.beat(BeatFraction.Half))
})
input.onPinTouchEvent(TouchPin.P3, input.buttonEventDown(), function () {
    music.playTone(349, music.beat(BeatFraction.Half))
})
