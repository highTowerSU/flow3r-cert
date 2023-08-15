from st3m.application import Application, ApplicationContext
from st3m.ui.colours import PUSH_RED, GO_GREEN, BLACK
from st3m.goose import Dict, Any
from st3m.input import InputState
from ctx import Context
import bl00mbox
import leds
import audio
import json
import math


class CertApp(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)
        self._state = 0
        self._time = 0
        self._wait_time = 100
        


    def draw_blue(self, ctx: Context) -> None: 
        ctx.rgb(0, 0, 255).rectangle(-120, -120, 240, 240).fill()
        leds.set_all_rgb(0, 0, 255)
        leds.update()
        
    def draw_black(self, ctx: Context) -> None:
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        leds.set_all_rgb(0, 0, 0)
        leds.update()

    def draw(self, ctx: Context) -> None:
        audio.speaker_set_volume_dB(audio.speaker_get_maximum_volume_dB())
        
        if self._state % 2 == 1 :
            self.draw_black(ctx)
        else:
            self.draw_blue(ctx)
        

        leds.update()
        # ctx.fill()

    def on_exit(self) -> None:
        leds.set_all_rgb(0, 0, 0)
        leds.update()

    def think(self, ins: InputState, delta_ms: int) -> None:
        self._time += delta_ms
        if self._time > self._wait_time :
            self._time = 0
            self._state += 1
            self._wait_time = 100
            
            
            if self._state == 5 :
                self._wait_time = 500
            if self._state > 5 :
                self._state = 0
        
        super().think(ins, delta_ms)
        