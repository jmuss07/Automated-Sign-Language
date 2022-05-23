import board
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
def full_palm(servoToActuate):
    servoToActuate.angle = 180
def half_palm(servoToActuate):
    servoToActuate.angle = 90
def pointed_out(servoToActuate):
    servoToActuate.angle = 0
def half_out(servoToActuate):
    servoToActuate.angle = 45

pwm1 = pwmio.PWMOut(board.D3, duty_cycle=2**15, frequency=200)
pwm2 = pwmio.PWMOut(board.D4, duty_cycle=2**15, frequency=200)
pwm3 = pwmio.PWMOut(board.D5, duty_cycle=2**15, frequency=200)
pwm4 = pwmio.PWMOut(board.D6, duty_cycle=2**15, frequency=200)
pwm5 = pwmio.PWMOut(board.D7, duty_cycle=2**15, frequency=200)

thumb = servo.Servo(pwm1)
pointer = servo.Servo(pwm2)
middle = servo.Servo(pwm3)
ring = servo.Servo(pwm4)
pinky = servo.Servo(pwm5)

def neutral():
    full_up(thumb)
    full_up(pointer)
    full_up(middle)
    full_up(ring)
    full_up(pinky)

def sign_a():
    full_up(thumb)
    full_down(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("A")

def sign_b():
    full_palm(thumb)
    full_up(pointer)
    full_up(middle)
    full_up(ring)
    full_up(pinky)
    print("B")

def sign_c():
    half_out(thumb)
    half_fold(pointer)
    half_fold(middle)
    half_fold(ring)
    half_fold(pinky)
    print("C")

def sign_d():
    full_palm(thumb)
    full_up(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("D")

def sign_e():
    full_palm(thumb)
    half_fold(pointer)
    half_fold(middle)
    half_fold(ring)
    half_fold(pinky)
    print("E")

def sign_f():
    half_fold(thumb)
    half_fold(pointer)
    full_up(middle)
    full_up(ring)
    full_up(pinky)
    print("F")

def sign_g():
    full_up(thumb)
    full_up(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("G")

def sign_h():
    full_up(thumb)
    full_up(pointer)
    full_up(middle)
    full_down(ring)
    full_down(pinky)
    print("H")

def sign_i():
    half_fold(thumb)
    full_down(pointer)
    full_down(middle)
    full_down(ring)
    full_up(pinky)
    print("I")

def sign_j():
    half_fold(thumb)
    full_down(pointer)
    full_down(middle)
    full_down(ring)
    full_up(pinky)
    print("J")

def sign_k():
    full_up(thumb)
    full_up(pointer)
    full_up(middle)
    full_down(ring)
    full_down(pinky)
    print("K")

def sign_l():
    pointed_out(thumb)
    full_up(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("L")

def sign_m():
    full_palm(thumb)
    half_fold(pointer)
    half_fold(middle)
    half_fold(ring)
    full_down(pinky)
    print("M")

def sign_n():
    full_palm(thumb)
    half_fold(pointer)
    half_fold(middle)
    full_down(ring)
    full_down(pinky)
    print("N")

def sign_o():
    half_fold(thumb)
    half_fold(pointer)
    half_fold(middle)
    half_fold(ring)
    half_fold(pinky)
    print("O")

def sign_p():
    full_up(thumb)
    full_up(pointer)
    half_fold(middle)
    full_down(ring)
    full_down(pinky)
    print("P")

def sign_q():
    full_up(thumb)
    full_up(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("Q")

def sign_r():
    half_palm(thumb)
    full_up(pointer)
    full_up(middle)
    full_down(ring)
    full_down(pinky)
    print("R")

def sign_s():
    half_palm(thumb)
    full_down(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("S")

def sign_t():
    full_up(thumb)
    half_fold(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("T")

def sign_u():
    half_palm(thumb)
    full_up(pointer)
    full_up(middle)
    full_down(ring)
    full_down(pinky)
    print("U")

def sign_v():
    half_palm(thumb)
    full_up(pointer)
    full_up(middle)
    half_fold(ring)
    full_down(pinky)
    print("V")

def sign_w():
    half_palm(thumb)
    full_up(pointer)
    full_up(middle)
    full_up(ring)
    full_down(pinky)
    print("W")

def sign_x():
    full_palm(thumb)
    half_fold(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("X")

def sign_y():
    pointed_out(thumb)
    full_down(pointer)
    full_down(middle)
    full_down(ring)
    full_up(pinky)
    print("Y")

def sign_z():
    full_palm(thumb)
    full_up(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("Z")

def sign_0():
    half_out(thumb)
    half_fold(pointer)
    half_fold(middle)
    half_fold(ring)
    half_fold(pinky)
    print("0")

def sign_1():
    pointed_out(thumb)
    full_down(pointer)
    full_down(middle)
    full_down(ring)
    full_down(pinky)
    print("1")

def sign_2():
    full_palm(thumb)
    full_up(pointer)
    full_up(middle)
    full_down(ring)
    full_down(pinky)
    print("2")

def sign_3():
    pointed_out(thumb)
    full_up(pointer)
    full_up(middle)
    full_down(ring)
    full_down(pinky)
    print("3")

def sign_4():
    full_palm(thumb)
    full_up(pointer)
    full_up(middle)
    full_up(ring)
    full_up(pinky)
    print("4")

def sign_5():
    pointed_out(thumb)
    full_up(pointer)
    full_up(middle)
    full_up(ring)
    full_up(pinky)
    print("5")

def sign_6():
    full_palm(thumb)
    full_up(pointer)
    full_up(middle)
    full_up(ring)
    full_down(pinky)
    print("6")

def sign_7():
    full_palm(thumb)
    full_up(pointer)
    full_up(middle)
    half_fold(ring)
    full_up(pinky)
    print("7")

def sign_8():
    full_palm(thumb)
    full_up(pointer)
    half_fold(middle)
    full_up(ring)
    full_up(pinky)
    print("8")

def sign_9():
    half_fold(thumb)
    half_fold(pointer)
    full_up(middle)
    full_up(ring)
    full_up(pinky)
    print("9")


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
