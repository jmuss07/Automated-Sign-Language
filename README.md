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

### Work Delegation

| Category               | Josie | Henry |
| ---------------------- | ----- | ----- |
| Speech-to-text         | 65%   | 35%   |
| Finger & Wrist control | 35%   | 65%   |

_Note: These numbers and divisions are pretty arbitrary._

### Timeline

| Date         | Goal                                                                                    |
| ------------ | --------------------------------------------------------------------------------------- |
| Winter Break | <ul><li>Hand modeled </ul> <ul><li>Finger control (base)</ul><ul><li>Text-to-chain</ul> |
| End of Q2    | <ul><li>Hand control prototyped</ul> <ul><li> Framework for signs</ul>                  |

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

Yes, this estimated cost is rather high. However, a lot of these materials are readily available already in the Sigma Lab, and can be re-used for future projects.

_Thanks to [Sigma Lab Wiki](http://wiki.chssigma.com/index.php?title=Sigma_Lab_Equipment_Costs) for the numbers._

### Images

A basic sketch for how the tension of the front of the arm may look...

![FrontOfArm](https://github.com/jmuss07/Automated-Sign-Language/blob/dec5cf5b68dd28cdcd7ed98c64007a657ec023e3/Images/Planning/FrontOfArm.png?raw=true)


...And a similar sketch for the back of the arm!

![BackOfArm](https://github.com/jmuss07/Automated-Sign-Language/blob/5fbd7c9bcdf45daa6b4d2411afcacc0b252cb9f5/Images/Planning/BackOfArm.png?raw=true)

*Credit to [Benton House](https://github.com/jhouse53) for the arm.*

## About Us

### **Henry Heisig**

Hi! I'm Henry, a class of 2024 student at Charlottesville High School. You can contact me at [hheisig51@charlottesvilleschools.org](mailto:hheisig51@charlottesvilleschools.org) or [henrycheisig+github@gmail.com](mailto:henrycheisig+github@gmail.com), or find my work on [Github](https://github.com/hheisig51)



## What Mr H needs from us
### Your project's criteria and constraints
(Henry needs to do this) 
Criteria:  Specific goals, including what each part will do, and the basic needs (power led, switch, batteries, etc)

Constraint: THIS IS BIG
* Time:  Not only the due date (feb 1st is the goal), but you need to break this project into more managable chunks,  What will be done before xmas break?
* Budget: Good material cost list, but what I need to know is "if we need to purchase materials beyond what the lab supplies, we are OK with spending up to $XX, each, if need be"
* Safety:   I know you're going to be safe, thats not the point of this.  I need you to put in writing, your considerations of the possuble and expected risks associated with this project.   Will there be soldering?  could acrylic break?   Can this hand hurt you?   How many volts?  How can this hurt you??
* KNOWLEDGE:  You have stated this elsewhere, but move it here and make it crystal clear:  What do you need to learn, in order to be successful at thisn project?

### A shortlist of possible solutions your team considered.

#### The solution you picked, and why

### Design sketches/images captioned and very detailed

(Josie is taking this)
You did start this, but are lacking enough detail for how the arm will articulate, and how it will display each letter,
