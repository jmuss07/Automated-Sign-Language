# Automated Sign Language

## Table of Contents

- [Goals and Planning](#Goals-and-Planning)
- [Research](#Research)
- [About Us](#About-Us)

## Goals and Planning

Phase 1

**Description**: A robotic, anthropomorphic hand that can display the ASL alphabet and basic one-handed gestures.

**Test of Success**: Through the hand, using the ASL alphabet, a word can be transmitted, received, and interpreted in under two minutes.

**Proof of Concept**: [ASLAN robot](https://www.hubs.com/blog/theres-not-enough-sign-language-translators-so-these-students-3d-printed-a-humanoid-robot/) made by Uni. of Antwerp students.

Components of Antwerp:

- 16 servos
- 25 3D printed parts (139 hour print time)
- 3 motor controllers
- Arduino Due
- 10 hour assembly time
- Access to global database

| Recreatable                                 | Unrealistic                                                        |
| ------------------------------------------- | ------------------------------------------------------------------ |
| Arm is 3D printed                           | 16 servos                                                          |
| Roughly human size                          | Able to learn                                                      |
| Multiple parts that assemble into the whole | Access to constantly updated local network of global signs         |
| Finger and arm joints move individually     | Network connected users can send messages that the hand interprets |

### What We Don't Know

- How to make a moveable finger joint.
- Typed input into letters, into hand sign. What's the process? (Library of servo movements? for each letter?).
- Turn speech into text that can be then inputted.
- Some signs and gestures require either unnatural movement, or a more complex process.
  - The signs for "z" and "j" require excessive movement of the arm.
  - Thumbs-up and thumbs-down require arm rotation.
  - etc.

### What We Need to Learn

- How to take audio (of speech), and turn it into a string interpretable by a microcontroller.
  - Speech-to-text (on raspberry pi?)
  - Parse and turn text into individual letters.
  - Turn the individual letters into commands for each part of the hand.
- How a synthetic joint can be controlled by a servo motor.
  - Finger joint(s)
  - Wrist! It has multiple directions of movement irl!
- How to use a raspberry pi (as a speech-to-text server) in coordination with an arduino (as a microcontroller).
  - USB out on raspi (raspberry pi) to arduino?
  - Pins on raspi to arduino?
  - etc?

### Work Delegation

| Category               | Josie | Henry |
| ---------------------- | ----- | ----- |
| Speech-to-text         | 65%   | 35%   |
| Finger & Wrist control | 35%   | 65%   |

_Note: These numbers and divisions are pretty arbitrary._

### Timeline

| Date  | Goal                                                                                       |
| ----- | ------------------------------------------------------------------------------------------ |
| 12/17 | Planning finished, box & arm modeled, hand & stt (speech-to-text) started                  |
| 1/7   | Box finished, arm in final revisions, servo/hand issue solved, rudimentary stt established |
| 1/14  | Arm finished, hand being developed with servos, stt able to trigger servo                  |
| 1/21  | Hand being printed/in final revisions, full project assembled, stt finished                |
| 1/28  | Physical project finished, troubleshooting                                                 |
| 2/4   | Final documentation finished, project submitted                                            |

### Estimated Cost

| Item                        | Cost per Item | Quantity                  | Total Cost |
| --------------------------- | ------------- | ------------------------- | ---------- |
| Servo                       | $5.95         | 8                         | $47.60     |
| 3D Printer Model Material   | $2.43 / in³   | 8 in³                     | $19.44     |
| 3D Printer Support Material | $4.76 / in³   | 1.5 in³                   | $7.14      |
| 1/8" Acrylic Sheet          | $2.65 / ft²   | 9.5 ft²                   | $25.18     |
| Wire                        | $0.08 / ft    | 6 ft                      | $0.48      |
| Panel-mount SPDT Switch     | $0.95         | 1                         | $0.95      |
| LED (Green or Red)          | $0.16         | 1                         | $0.16      |
| Arduino Uno/Metro           | $24.95        | 1                         | $24.95     |
| Arduino Prototyping Shield  | $11.49        | 1                         | $11.49     |
| Raspberry Pi                | $35.00        | 1                         | $35.00     |
|                             |               | **Final Estimated Cost**: | $172.39    |

Yes, this estimated cost is rather high. However, a lot of these materials are readily available already in the Sigma Lab, and can be re-used for future projects. If need be, $75 is available to purchase extra materials.

_Thanks to [Sigma Lab Wiki](http://wiki.chssigma.com/index.php?title=Sigma_Lab_Equipment_Costs) for the numbers._

### Parts and Uses

| Part         | Use                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------- |
| Microphone   | To pick up speech as audio.                                                                                         |
| Raspberry Pi | To run a speech-to-text server, and turn the audio into strings, and the strings into commands sent to the arduino. |
| Arduino      | To control the servos.                                                                                              |
| Switch       | To turn the whole unit on and off.                                                                                  |
| Arm Servos   | To rotate the arm, and bend the wrist.                                                                              |
| Hand Servos  | To control the individual fingers on the hand.                                                                      |
| Elastic      | To let the hand servos bend/extend the fingers on the hand.                                                         |

### Safety

- The base box will be made of acrylic, and have the weight of the arm on it. If any point has too much stress, the acrylic could break. This would cause sharp edges, so there's **danger of cuts**.
- If the whole arm will be able to rotate, and the fingers/wrist move quick, then there will be a lot of fast movement. If parts are not secured properly, there could be a **risk of parts flying off and hurting someone**.
- As the physical interaction with the arm would be minimal, the **risk for electrical shock is low**.
  **soldering**
- We will need to solder various wires, which has the **risk of fire and burns** if the soldering iron is not used correctly.

### Images

A basic sketch for how the tension of the front of the arm may look...

![FrontOfArm](https://github.com/jmuss07/Automated-Sign-Language/blob/dec5cf5b68dd28cdcd7ed98c64007a657ec023e3/Images/Planning/FrontOfArm.png?raw=true)

...And a similar sketch for the back of the arm!

![BackOfArm](https://github.com/jmuss07/Automated-Sign-Language/blob/5fbd7c9bcdf45daa6b4d2411afcacc0b252cb9f5/Images/Planning/BackOfArm.png?raw=true)

_Credit to [Benton House](https://github.com/jhouse53) for the arm._

## Research

Phase 2

[Open Bionics Lab](https://openbionicslabs.com/downloads)

The OpenBionics Lab's ADA v1.1 hand has designs for exactly what we're doing. But, it's designed for different servos, and a custom PCB. If we use anything from it, adaptations need to be made.

Below, is documentation of a single makeshift finger. Designed with minimal 3D printing, so manufacturing time is low. Overall, the only 3D-printed parts are the dowels, which take all of 10 minutes.

## About Us

### **Josie Muss**

Hey there! I'm Josie, and I'm a member of Charlottesville High School's class of 2023! You can find more of my projects on my [Github](https://github.com/jmuss07). Any questions for me on either this project or any of others that I've worked on can be sent to me at [jmuss07@charlottesvilleschools.org](mailto:jmuss07@charlottesvilleschools.org)

### **Henry Heisig**

Hi! I'm Henry, a class of 2024 student at Charlottesville High School. You can contact me at [hheisig51@charlottesvilleschools.org](mailto:hheisig51@charlottesvilleschools.org) or [henrycheisig+github@gmail.com](mailto:henrycheisig+github@gmail.com), or find my work on [Github](https://github.com/hheisig51)
