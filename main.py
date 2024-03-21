from machine import Pin, PWM
import time

# Define os pinos do buzzer e da LED
buzzer = PWM(Pin(26))
led_pin = Pin(14, Pin.OUT)

# Define as frequências das notas
A3 = 220
A4 = 440
A5 = 880
Ab3 = 208
Ab4 = 415
Ab5 = 831
B2 = 123
B3 = 247
B4 = 494
Bb2 = 116
Bb3 = 233
Bb4 = 466
C3 = 130
C4_middle = 261
C5 = 523
C6 = 1046
Db3 = 139
Db4 = 277
Db5 = 554
Db6 = 1109
D3 = 147
D4 = 294
D5 = 587
D6 = 1175
E3 = 165
E4 = 330
E5 = 659
Eb3 = 156
Eb5 = 622
F3 = 175
F4 = 349
F5 = 698
Gb3 = 185
Gb5 = 740
G3 = 196
G4 = 392
G5 = 784
G6 = 1568

# Define as durações das notas
quarter_note = 0.25
half_note = 0.5
eighth_note = 0.125
sixteenth_note = 0.0625
whole_note = 1

# Fator de escala para aumentar a velocidade
scale_factor = 0.5  # Reduzindo a duração das notas para aumentar a velocidade

# Define a função para tocar uma nota
def play_note(note_freq, duration):
    buzzer.freq(note_freq)
    buzzer.duty(512)  # Define a intensidade do som
    time.sleep(duration)
    buzzer.duty(0)  # Desliga o som
    time.sleep(0.05)  # Pausa entre as notas

# Define a função para piscar a LED de acordo com o ritmo
def flash_led(duration):
    led_pin.value(1)
    time.sleep(duration)
    led_pin.value(0)

# Define a melodia
melody = [
    # Introdução
    
    (D4, eighth_note * scale_factor), (D4, eighth_note * scale_factor), (D5, half_note * scale_factor), (A4, 0.375 * scale_factor),
    (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor), (D4, eighth_note * scale_factor), (F4, eighth_note * scale_factor),
    (G4, eighth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor), (D5, half_note * scale_factor),
    (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor), (D4, eighth_note * scale_factor),
    (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (B3, eighth_note * scale_factor), (B3, eighth_note * scale_factor),
    (D5, half_note * scale_factor), (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor),
    (D4, eighth_note * scale_factor), (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (D5, half_note * scale_factor), (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor),
    (D4, eighth_note * scale_factor), (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (Bb3, sixteenth_note * scale_factor),
    (Bb3, sixteenth_note * scale_factor), (Bb3, sixteenth_note * scale_factor), (Bb3, sixteenth_note * scale_factor), (D5, half_note * scale_factor),
    (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor), (D4, eighth_note * scale_factor),
    (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor), (D5, half_note * scale_factor),
    (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor), (D4, eighth_note * scale_factor),
    (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (B3, eighth_note * scale_factor), (B3, eighth_note * scale_factor),
    (D5, half_note * scale_factor), (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor),
    (D4, eighth_note * scale_factor), (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (D5, half_note * scale_factor), (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor),
    (D4, eighth_note * scale_factor), (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (Bb3, sixteenth_note * scale_factor),
    (Bb3, sixteenth_note * scale_factor), (Bb3, sixteenth_note * scale_factor), (Bb3, sixteenth_note * scale_factor), (D5, half_note * scale_factor),
    (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor),
    (D4, eighth_note * scale_factor), (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (D5, half_note * scale_factor), (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor),
    (D4, eighth_note * scale_factor), (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (B3, eighth_note * scale_factor), (B3, eighth_note * scale_factor),
    (D5, half_note * scale_factor), (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor),
    (D4, eighth_note * scale_factor), (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor), (C4_middle, sixteenth_note * scale_factor),
    (D5, half_note * scale_factor), (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor),
    (D4, eighth_note * scale_factor), (F4, eighth_note * scale_factor), (G4, eighth_note * scale_factor), (Bb3, sixteenth_note * scale_factor),
    (Bb3, sixteenth_note * scale_factor), (Bb3, sixteenth_note * scale_factor), (Bb3, sixteenth_note * scale_factor), (D5, half_note * scale_factor),
    (A4, 0.375 * scale_factor), (Ab4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor),

    # Tema Principal (Parte 1)

    (D5, eighth_note * scale_factor), (D5, eighth_note * scale_factor), (D6, half_note * scale_factor), (A5, 0.325 * scale_factor),
    (Ab5, 0.25 * scale_factor), (G5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (D5, eighth_note * scale_factor), (F5, eighth_note * scale_factor),
    (G5, eighth_note * scale_factor), (C5, eighth_note * scale_factor), (C5, eighth_note * scale_factor), (D6, half_note * scale_factor),
    (A5, 0.325 * scale_factor), (Ab5, 0.25 * scale_factor), (G5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (D5, eighth_note * scale_factor), (F5, eighth_note * scale_factor), (G5, eighth_note * scale_factor), (B4, eighth_note * scale_factor), (B4, eighth_note * scale_factor),
    (D6, half_note * scale_factor), (A5, 0.325 * scale_factor), (Ab5, 0.25 * scale_factor), (G5, 0.25 * scale_factor), (F5, 0.25 * scale_factor),
    (D5, eighth_note * scale_factor), (F5, eighth_note * scale_factor), (G5, eighth_note * scale_factor), (C5, eighth_note * scale_factor),
    (C5, eighth_note * scale_factor), (D6, half_note * scale_factor), (A5, 0.325 * scale_factor), (Ab5, 0.25 * scale_factor), (G5, 0.25 * scale_factor),
    
    # Tema Principal (Parte 2)

    (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor),
    (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (D5, 0.25 * scale_factor), (D5, 0.625 * scale_factor),
    (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (G5, 0.25 * scale_factor),
    (Ab5, 0.25 * scale_factor), (G5, 0.042 * scale_factor), (Ab5, 0.042 * scale_factor), (G5, 0.042 * scale_factor),
    (F5, 0.125 * scale_factor), (D5, 0.125 * scale_factor), (F5, 0.125 * scale_factor), (G5, 0.375 * scale_factor),
    (F5, 0.25 * scale_factor), (F5, 0.125 * scale_factor), (F5, 0.125 * scale_factor), (G5, 0.25 * scale_factor),
    (Ab5, 0.25 * scale_factor), (A5, 0.25 * scale_factor), (C6, 0.25 * scale_factor), (A5, 0.375 * scale_factor),
    (D6, 0.25 * scale_factor), (D6, 0.25 * scale_factor), (D6, 0.125 * scale_factor), (A5, 0.125 * scale_factor),
    (D6, 0.125 * scale_factor), (C6, 0.625 * scale_factor), (G6, 0.5 * scale_factor),

    # Construção (Parte 1)

    (A5, 0.25 * scale_factor), (A5, 0.125 * scale_factor), (A5, 0.125 * scale_factor), (A5, 0.25 * scale_factor),
    (A5, 0.25 * scale_factor), (G5, 0.25 * scale_factor), (G5, 0.625 * scale_factor), (A5, 0.25 * scale_factor),
    (A5, 0.125 * scale_factor), (A5, 0.125 * scale_factor), (A5, 0.25 * scale_factor), (A5, 0.25 * scale_factor),
    (G5, 0.125 * scale_factor), (A5, 0.25 * scale_factor), (D6, 0.125 * scale_factor), (A5, 0.125 * scale_factor),
    (G5, 0.25 * scale_factor), (D6, 0.25 * scale_factor), (A5, 0.25 * scale_factor), (G5, 0.25 * scale_factor),
    (F5, 0.25 * scale_factor), (C6, 0.25 * scale_factor), (G5, 0.25 * scale_factor), (F5, 0.25 * scale_factor),
    (E5, 0.25 * scale_factor), (Bb4, 0.25 * scale_factor), (C5, 0.125 * scale_factor), (D5, 0.125 * scale_factor),
    (F5, 0.25 * scale_factor), (C6, 0.25 * scale_factor), (G6, 0.125 * scale_factor),

    # Construção (Parte 2)

    (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor),
    (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (D5, 0.25 * scale_factor), (D5, 0.625 * scale_factor),
    (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (F5, 0.25 * scale_factor), (G5, 0.25 * scale_factor),
    (Ab5, 0.25 * scale_factor), (G5, 0.042 * scale_factor), (Ab5, 0.042 * scale_factor), (G5, 0.042 * scale_factor),
    (F5, 0.125 * scale_factor), (D5, 0.125 * scale_factor), (F5, 0.125 * scale_factor), (G5, 0.375 * scale_factor),
    (F5, 0.25 * scale_factor), (F5, 0.125 * scale_factor), (F5, 0.125 * scale_factor), (G5, 0.25 * scale_factor),
    (Ab5, 0.25 * scale_factor), (A5, 0.25 * scale_factor), (C6, 0.25 * scale_factor), (A5, 0.375 * scale_factor),
    (D6, 0.25 * scale_factor), (D6, 0.25 * scale_factor), (D6, 0.125 * scale_factor), (A5, 0.125 * scale_factor),
    (D6, 0.125 * scale_factor), (C6, 0.625 * scale_factor), (G6, 0.5 * scale_factor),
    (F4, 0.25 * scale_factor), (G4, 0.25 * scale_factor), (A4, 0.25 * scale_factor), (F5, 0.25 * scale_factor),
    (E5, 0.5 * scale_factor), (D5, 0.5 * scale_factor), (E5, 0.5 * scale_factor), (F5, 0.5 * scale_factor),
    (G5, 0.5 * scale_factor), (E5, 0.5 * scale_factor), (A5, 1.0 * scale_factor),
    (A5, 0.125 * scale_factor), (Ab5, 0.125 * scale_factor), (G5, 0.125 * scale_factor), (Gb5, 0.125 * scale_factor),
    (F5, 0.125 * scale_factor), (E5, 0.125 * scale_factor), (Eb5, 0.125 * scale_factor), (D5, 0.125 * scale_factor),
    (Db5, 0.1 * scale_factor), (Eb5, 0.1 * scale_factor),

    # Clímax

    (Bb3, 0.15 * scale_factor), (F4, 0.5 * scale_factor), (E4, 0.1 * scale_factor), (D4, 0.1 * scale_factor),
    (F4, 0.1 * scale_factor), (Bb3, 0.15 * scale_factor), (F4, 0.5 * scale_factor), (E4, 0.1 * scale_factor),
    (D4, 0.1 * scale_factor), (D4, 0.1 * scale_factor), (D4, 0.083 * scale_factor), (Db4, 0.083 * scale_factor),
    (C4_middle, 0.083 * scale_factor), (B3, 0.083 * scale_factor), (Bb3, 0.083 * scale_factor),
    (A3, 0.083 * scale_factor), (Ab3, 0.083 * scale_factor), (G3, 0.083 * scale_factor), (Gb3, 0.083 * scale_factor),
    (F3, 0.083 * scale_factor), (E3, 0.083 * scale_factor), (Eb3, 0.083 * scale_factor), (D3, 0.2 * scale_factor),
    (Bb3, 0.15 * scale_factor), (F4, 0.5 * scale_factor), (E4, 0.10 * scale_factor), (D4, 0.10 * scale_factor),
    (F4, 0.2 * scale_factor), (B2, 0.125 * scale_factor), (G3, 0.125 * scale_factor), (F4, 0.125 * scale_factor),
    (D4, 0.125 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.125 * scale_factor),
    (C4_middle, 0.125 * scale_factor), (D4, 0.125 * scale_factor), (C4_middle, 0.25 * scale_factor),
    (A3, 0.25 * scale_factor), (G3, 0.125 * scale_factor), (C4_middle, 0.125 * scale_factor),
    (Bb3, 0.15 * scale_factor), (F4, 0.5 * scale_factor), (E4, 0.1 * scale_factor), (D4, 0.1 * scale_factor),
    (D3, 0.125 * scale_factor), (D3, 0.125 * scale_factor), (F4, 0.25 * scale_factor), (E4, 0.25 * scale_factor),
    (C4_middle, 0.125 * scale_factor), (E4, 0.25 * scale_factor), (B3, 0.25 * scale_factor),
    (G3, 0.125 * scale_factor), (A3, 0.125 * scale_factor), (C4_middle, 0.125 * scale_factor),
    (D3, 0.125 * scale_factor), (D3, 0.125 * scale_factor), (F4, 0.25 * scale_factor), (E4, 0.25 * scale_factor),
    (C4_middle, 0.125 * scale_factor), (E4, 0.25 * scale_factor), (B3, 0.25 * scale_factor),
    (G3, 0.125 * scale_factor), (A3, 0.125 * scale_factor), (C4_middle, 0.125 * scale_factor),

    # Desdobramento

    (Bb3, 0.25 * scale_factor), (Bb3, 0.25 * scale_factor), (Bb2, 0.125 * scale_factor), (Bb3, 0.25 * scale_factor),
    (Bb3, 0.25 * scale_factor), (Bb3, 0.25 * scale_factor), (Bb2, 0.125 * scale_factor), (Bb2, 0.125 * scale_factor),
    (Bb2, 0.125 * scale_factor), (Bb3, 0.25 * scale_factor), (C4_middle, 0.25 * scale_factor),
    (C4_middle, 0.25 * scale_factor), (C3, 0.125 * scale_factor), (C4_middle, 0.25 * scale_factor),
    (C4_middle, 0.25 * scale_factor), (C4_middle, 0.25 * scale_factor), (C3, 0.125 * scale_factor),
    (C3, 0.125 * scale_factor), (C3, 0.125 * scale_factor), (C4_middle, 0.25 * scale_factor),
    (D4, 0.25 * scale_factor), (D4, 0.25 * scale_factor), (D3, 0.125 * scale_factor), (D4, 0.25 * scale_factor),
    (Db4, 0.25 * scale_factor), (Db4, 0.25 * scale_factor), (Db3, 0.125 * scale_factor), (Db3, 0.125 * scale_factor),
    (Db3, 0.125 * scale_factor), (Db4, 0.25 * scale_factor), (C4_middle, 0.25 * scale_factor),
    (C4_middle, 0.25 * scale_factor), (C3, 0.125 * scale_factor), (C4_middle, 0.25 * scale_factor),
    (B3, 0.25 * scale_factor), (B3, 0.25 * scale_factor), (B2, 0.125 * scale_factor), (B2, 0.125 * scale_factor),
    (B2, 0.125 * scale_factor), (B3, 0.25 * scale_factor), (Bb3, 0.25 * scale_factor), (Bb3, 0.25 * scale_factor),
    (Bb2, 0.125 * scale_factor), (Bb3, 0.25 * scale_factor), (Bb3, 0.25 * scale_factor), (Bb3, 0.25 * scale_factor),
    (Bb2, 0.125 * scale_factor), (Bb2, 0.125 * scale_factor), (Bb2, 0.125 * scale_factor), (Bb3, 0.25 * scale_factor),
    (C4_middle, 0.25 * scale_factor), (C4_middle, 0.25 * scale_factor), (C3, 0.125 * scale_factor),
    (C4_middle, 0.25 * scale_factor), (C4_middle, 0.25 * scale_factor), (C4_middle, 0.25 * scale_factor),
    (C3, 0.125 * scale_factor), (C3, 0.125 * scale_factor), (C3, 0.125 * scale_factor), (C4_middle, 0.25 * scale_factor),
    (D4, 0.25 * scale_factor), (D3, 0.125 * scale_factor), (D4, 0.25 * scale_factor), (A3, 0.125 * scale_factor),
    (D4, 0.25 * scale_factor), (D4, 0.25 * scale_factor), (D4, 0.25 * scale_factor), (F3, 0.25 * scale_factor),
    (D3, 0.125 * scale_factor), (D4, 0.125 * scale_factor), (G3, 0.125 * scale_factor), (D4, 0.125 * scale_factor),
    (D3, 0.125 * scale_factor), (D4, 0.25 * scale_factor), (A3, 0.125 * scale_factor), (D4, 0.25 * scale_factor),
    (D4, 0.25 * scale_factor), (D4, 0.25 * scale_factor), (F3, 0.25 * scale_factor), (D3, 0.125 * scale_factor),
    (D4, 0.125 * scale_factor), (G3, 0.125 * scale_factor),

    # Conclusão

    (D4, 0.125 * scale_factor), (D4, 0.125 * scale_factor), (D5, 0.25 * scale_factor), (A4, 0.375 * scale_factor),
    (Ab4, 0.125 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor), (D4, 0.125 * scale_factor),
    (F4, 0.125 * scale_factor), (G4, 0.125 * scale_factor), (C4_middle, 0.0625 * scale_factor),
    (C4_middle, 0.0625 * scale_factor), (C4_middle, 0.0625 * scale_factor), (C4_middle, 0.0625 * scale_factor),
    (D5, 0.25 * scale_factor), (A4, 0.375 * scale_factor), (Ab4, 0.125 * scale_factor), (G4, 0.25 * scale_factor),
    (F4, 0.25 * scale_factor), (D4, 0.125 * scale_factor), (F4, 0.125 * scale_factor), (G4, 0.125 * scale_factor),
    (B3, 0.125 * scale_factor), (B3, 0.125 * scale_factor), (D5, 0.25 * scale_factor), (A4, 0.375 * scale_factor),
    (Ab4, 0.125 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor), (D4, 0.125 * scale_factor),
    (F4, 0.125 * scale_factor), (G4, 0.125 * scale_factor), (Bb3, 0.0625 * scale_factor), (Bb3, 0.0625 * scale_factor),
    (Bb3, 0.0625 * scale_factor), (Bb3, 0.0625 * scale_factor), (D5, 0.25 * scale_factor), (A4, 0.375 * scale_factor),
    (Ab4, 0.125 * scale_factor), (G4, 0.25 * scale_factor), (F4, 0.25 * scale_factor), (D4, 0.125 * scale_factor),
    (F4, 0.125 * scale_factor), (G4, 0.125 * scale_factor), (C4_middle, 0.0625 * scale_factor),
    (C4_middle, 0.0625 * scale_factor), (C4_middle, 0.0625 * scale_factor), (C4_middle, 0.0625 * scale_factor),
    (D5, 0.25 * scale_factor), (A4, 0.375 * scale_factor), (Ab4, 0.125 * scale_factor), (G4, 0.25 * scale_factor),
    (F4, 0.25 * scale_factor), (D4, 0.125 * scale_factor), (F4, 0.125 * scale_factor), (G4, 0.125 * scale_factor)]

# Reproduz a melodia e pisca o LED
for note in melody:
    flash_led(note[1])
    play_note(note[0], note[1])
