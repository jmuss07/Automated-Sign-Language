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

![FrontOfArm](https://github.com/jmuss07/Automated-Sign-Language/blob/dec5cf5b68dd28cdcd7ed98c64007a657ec023e3/Images/Planning/FrontOfArm.png?raw=true)

![back-of-arm](https://github.com/jmuss07/Automated-Sign-Language/blob/main/Images/Planning/back-of-arm.png?raw=true)

## About Us

### **Henry Heisig**

Hi! I'm Henry, a class of 2024 student at Charlottesville High School. You can contact me at [hheisig51@charlottesvilleschools.org](mailto:hheisig51@charlottesvilleschools.org) or [henrycheisig+github@gmail.com](mailto:henrycheisig+github@gmail.com), or find my work on [Github](https://github.com/hheisig51)
