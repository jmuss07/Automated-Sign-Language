# Automated Sign Language

## Table of Contents

- [Goals and Planning](#Goals-and-Planning)
- [About Us](#About-Us)

## Goals and Planning

**Description**: A robotic, anthropomorphic hand that can display the ASL alphabet and basic one-handed gestures.

**Test of Success**: Through the hand, using the ASL alphabet, a word can be transmitted, received, and interpreted in under two minutes.

**Proof of Concept**: [ASLAN robot](https://www.hubs.com/blog/theres-not-enough-sign-language-translators-so-these-students-3d-printed-a-humanoid-robot/) made by Uni. of Antwerp students.

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
- How a synthetic joint can be controlled by a servo motor.
- How to use a raspberry pi (as a speech-to-text server) in coordination with an arduino (as a microcontroller).

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

| Item                        | Cost per Item          | Quantity                  | Total Cost |
| --------------------------- | ---------------------- | ------------------------- | ---------- |
| Servo                       | $5.95                  | 8                         | $47.60     |
| 3D Printer Model Material   | $2.43 / in<sup>3</sup> | 8 in<sup>3</sup>          | $19.44     |
| 3D Printer Support Material | $4.76 / in<sup>3</sup> | 1.5 in<sup>3</sup>        | $7.14      |
| 1/8" Acrylic Sheet          | $2.65 / ft<sup>2</sup> | 9.5 ft<sup>2</sup>        | $25.18     |
| Wire                        | $0.08 / ft             | 6 ft                      | $0.48      |
| Panel-mount SPDT Switch     | $0.95                  | 1                         | $0.95      |
| LED (Green or Red)          | $0.16                  | 1                         | $0.16      |
| Arduino Uno/Metro           | $24.95                 | 1                         | $24.95     |
| Arduino Prototyping Shield  | $11.49                 | 1                         | $11.49     |
| Raspberry Pi                | $35.00                 | 1                         | $35.00     |
|                             |                        | **Final Estimated Cost**: | $172.39    |

Yes, this estimated cost is rather high. However, a lot of these materials are readily available already in the Sigma Lab, and can be re-used for future projects. If need be, _$40_ is available to purchase extra materials.

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

### Images

A basic sketch for how the tension of the front of the arm may look...

![FrontOfArm](https://github.com/jmuss07/Automated-Sign-Language/blob/dec5cf5b68dd28cdcd7ed98c64007a657ec023e3/Images/Planning/FrontOfArm.png?raw=true)

...And a similar sketch for the back of the arm!

![BackOfArm](https://github.com/jmuss07/Automated-Sign-Language/blob/5fbd7c9bcdf45daa6b4d2411afcacc0b252cb9f5/Images/Planning/BackOfArm.png?raw=true)

_Credit to [Benton House](https://github.com/jhouse53) for the arm._

## About Us

### **Josie Muss**

Hey there! I'm Josie, and I'm a member of Charlottesville High School's class of 2023! You can find more of my projects on my [Github](https://github.com/jmuss07). Any questions for me on either this project or any of others that I've worked on can be sent to me at [jmuss07@charlottesvilleschools.org](mailto:jmuss07@charlottesvilleschools.org)

### **Henry Heisig**

Hi! I'm Henry, a class of 2024 student at Charlottesville High School. You can contact me at [hheisig51@charlottesvilleschools.org](mailto:hheisig51@charlottesvilleschools.org) or [henrycheisig+github@gmail.com](mailto:henrycheisig+github@gmail.com), or find my work on [Github](https://github.com/hheisig51)

## What Mr H needs from us

### Your project's criteria and constraints

(Henry needs to do this)
Criteria: Specific goals, including what each part will do, and the basic needs (power led, switch, batteries, etc)

Constraint: THIS IS BIG

- Time: Not only the due date (feb 1st is the goal), but you need to break this project into more managable chunks, What will be done before xmas break?
- Budget: Good material cost list, but what I need to know is "if we need to purchase materials beyond what the lab supplies, we are OK with spending up to $XX, each, if need be"
- Safety: I know you're going to be safe, thats not the point of this. I need you to put in writing, your considerations of the possuble and expected risks associated with this project. Will there be soldering? could acrylic break? Can this hand hurt you? How many volts? How can this hurt you??
- KNOWLEDGE: You have stated this elsewhere, but move it here and make it crystal clear: What do you need to learn, in order to be successful at thisn project?

### A shortlist of possible solutions your team considered.

- Backup Plan: Expand on those ideas, but have them correlate more closely to the main project idea
- Antwerp Version: Pros and cons of the advanced college one. What can we recreate? What's way to advanced and should be cut in order to simplify?
- Beware the scope-drift
- Expand on the list of challenges we have ("What We Don't Know" section); we know what we don't know, but what are some possible solutions

#### The solution you picked, and why

- How are we planning to actually solve the issues presentred (project modifications, smaller scale, etc)
- Why did we choose these solutiuons

### Design sketches/images captioned and very detailed

(Josie is taking this)
You did start this, but are lacking enough detail for how the arm will articulate, and how it will display each letter,

###

I've been told that we should each come up with a sub design (such as servo ”in thumb versus with the other ones with a long string, smaller design features like that),so the project itself is the same its more just individual solution and more specified design features.
