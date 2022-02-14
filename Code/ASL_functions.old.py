import board
import time
import neopixel
import pwmio
import servo

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

def full_up(servoToActuate):
    servoToActuate.angle = 0
def full_down(servoToActuate):
    servoToActuate.angle = 180
def half_fold(servoToActuate):
    servoToActuate.angle = 90
def full_palm():
    print("placeholder")
def half_palm():
    print("placeholder")
def pointed_out():
    print("placeholder")
def half_out():
    print("placeholder")

pwm1 = pwmio.PWMOut(board.D3, duty_cycle=2**15, frequency=200)
pwm2 = pwmio.PWMOut(board.D4, duty_cycle=2**15, frequency=200)
pwm3 = pwmio.PWMOut(board.D5, duty_cycle=2**15, frequency=200)
pwm4 = pwmio.PWMOut(board.D6, duty_cycle=2**15, frequency=200)
pwm5 = pwmio.PWMOut(board.D7, duty_cycle=2**15, frequency=200)

thumb = servo.Servo(pwm1)
pointer_finger = servo.Servo(pwm2)
middle_finger = servo.Servo(pwm3)
ring_finger = servo.Servo(pwm4)
pinky = servo.Servo(pwm5)

def neutral():
    full_up(pointer_finger)
    full_up(middle_finger)

def sign_a():
    full_down(pointer_finger)

def sign_b():
    print("Placeholder to sign the letter 'B'.")


def sign_c():
    print("Placeholder to sign the letter 'C'.")


def sign_d():
    print("Placeholder to sign the letter 'D'.")


def sign_e():
    print("Placeholder to sign the letter 'E'.")


def sign_f():
    print("Placeholder to sign the letter 'F'.")


def sign_g():
    print("Placeholder to sign the letter 'G'.")


def sign_h():
    print("Placeholder to sign the letter 'H'.")


def sign_i():
    print("Placeholder to sign the letter 'I'.")


def sign_j():
    print("Placeholder to sign the letter 'J'.")


def sign_k():
    print("Placeholder to sign the letter 'K'.")


def sign_l():
    print("Placeholder to sign the letter 'L'.")


def sign_m():
    print("Placeholder to sign the letter 'M'.")


def sign_n():
    print("Placeholder to sign the letter 'N'.")


def sign_o():
    print("Placeholder to sign the letter 'O'.")


def sign_p():
    print("Placeholder to sign the letter 'P'.")


def sign_q():
    print("Placeholder to sign the letter 'Q'.")


def sign_r():
    print("Placeholder to sign the letter 'R'.")


def sign_s():
    print("Placeholder to sign the letter 'S'.")


def sign_t():
    print("Placeholder to sign the letter 'T'.")


def sign_u():
    print("Placeholder to sign the letter 'U'.")


def sign_v():
    print("Placeholder to sign the letter 'V'.")


def sign_w():
    print("Placeholder to sign the letter 'W'.")


def sign_x():
    print("Placeholder to sign the letter 'X'.")


def sign_y():
    print("Placeholder to sign the letter 'Y'.")


def sign_z():
    print("Placeholder to sign the letter 'Z'.")


def sign_0():
    print("Placeholder to sign the letter '0'.")


def sign_1():
    print("Placeholder to sign the letter '1'.")


def sign_2():
    print("Placeholder to sign the letter '2'.")


def sign_3():
    print("Placeholder to sign the letter '3'.")


def sign_4():
    print("Placeholder to sign the letter '4'.")


def sign_5():
    print("Placeholder to sign the letter '5'.")


def sign_6():
    print("Placeholder to sign the letter '6'.")


def sign_7():
    print("Placeholder to sign the letter '7'.")


def sign_8():
    print("Placeholder to sign the letter '8'.")


def sign_9():
    print("Placeholder to sign the letter '9'.")


asl_dict = {
    "a": sign_a,
    "b": sign_b,
    "c": sign_c,
    "d": sign_d,
    "e": sign_e,
    "f": sign_f,
    "g": sign_g,
    "h": sign_h,
    "i": sign_i,
    "j": sign_j,
    "k": sign_k,
    "l": sign_l,
    "m": sign_m,
    "n": sign_n,
    "o": sign_o,
    "p": sign_p,
    "q": sign_q,
    "r": sign_r,
    "s": sign_s,
    "t": sign_t,
    "u": sign_u,
    "v": sign_v,
    "w": sign_w,
    "x": sign_x,
    "y": sign_y,
    "z": sign_z,
    "0": sign_0,
    "1": sign_1,
    "2": sign_2,
    "3": sign_3,
    "4": sign_4,
    "5": sign_5,
    "6": sign_6,
    "7": sign_7,
    "8": sign_8,
    "9": sign_9,
}
