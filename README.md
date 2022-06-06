# Automated Sign Language

## Table of Contents

- [Phase 1](#phase-1)
- [Phase 2](#phase-2)
- [Phase 3](#phase-3)
- [About Us](#about-us)

## Phase 1

Goals, Planning, etc.

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

![FrontOfArm](Images/FrontOfArm.png)

...And a similar sketch for the back of the arm!

![BackOfArm](Images/BackOfArm.png)

_Credit to [Benton House](https://github.com/jhouse53) for the arm._

## Phase 2

Milestone work (From research, to final work)

The OpenBionics Lab's ADA v1.1 hand has designs for exactly what we're doing. But, it's designed for different servos, and a custom PCB. If we use anything from it, adaptations need to be made.

[ADA v1.1 Datasheet](Images/Ada_v1_1_Datasheet.pdf)

[Open Bionics Lab](https://openbionicslabs.com/downloads)

Below, is documentation of a single makeshift finger. Designed with minimal 3D printing, so manufacturing time is low. Overall, the only 3D-printed parts are the dowels, which take all of 10 minutes.

https://user-images.githubusercontent.com/71345201/172168732-d8e445a4-d9d3-42a7-b983-bf6e3092c325.mp4

https://user-images.githubusercontent.com/71345201/172168760-eeb97748-df77-4b64-b599-513adac0ddce.mp4

<figure class="video_container">
  <video width="320" height="240" controls="true" allowfullscreen="true">
    <source src="Videos\2022-02-09_Finger-mp4.mp4" type="video/mp4">
  </video>
</figure>


Now, it's time to move onto the design of the final hand. The ADA v1.1 hand is made of a lot of Ninjaflex, too much for our project's budget. The final phase 2 goal is to cut this down.

So, it seems that the files provided by Open Bionics Labs were meshes, which Onshape does not support the editing of. The next best option is to either print the entire hand as-is, or re-design the fingers. The re-design would use the original .stl files as reference.

<figure class="video_container">
  <video width="320" height="240" controls="true" allowfullscreen="true">
    <source src="Videos\2022-02-25_MeshIssues-mp4.mp4" type="video/mp4">
  </video>
</figure>

<figure class="video_container">
  <video controls="true" allowfullscreen="true">
    <source src="https://github.com/jmuss07/Automated-Sign-Language/blob/main/Videos/2022-02-25_MeshIssues-mp4.mp4" type="video/mp4">
  </video>
</figure>

## Phase 3

Phase 3 is the combination and culmination of our work on the hand, string interpretation, and multi-servo control. As of now, this will not be achieved by the February 25th deadline. February 25th 2022, which at the time of writing, is today.

That was written over 2 months ago. Now, work starts again. At the moment, we have the fingers printed! Turns out, the Blender files (included with the ADA v1.1 download) were editable. This means a much higher chance of completing this project.

![Printed Fingers](/Images/PrintedFingers.png)

_Update 2022-05-13_: I (Henry) am currently trying to design a frame for the hand, to replace what we cut off of the model in Blender.

_2022-06-03_: It's been a minute, or two, or almost a month since the last update. It's been rough.

### Henry's Reflection

So, this is the last day of Engineering for the 2021-2022 school year. I have some things to say.

- Despite not finishing, I am _extremely_ proud of what I did this year. Last year, my project was nowhere near this finished.

- I made this design way too small and detailed. Half of the laser-cut pieces (the frame) snapped, and half of the 3D printed pieces (the finger joints) printed incorrectly.

- Bad documentation hurts you when you need to come back to the project after a break.

- Problem solving really helps, problem avoiding never does.

- When something's going wrong, and you just want to quit: Do it. Take a break, calm down, and come back at a different angle.

## About Us

### **Josie Muss**

Hey there! I'm Josie, and I'm a member of Charlottesville High School's class of 2023! You can find more of my projects on my [Github](https://github.com/jmuss07). Any questions for me on either this project or any of others that I've worked on can be sent to me at [jmuss07@charlottesvilleschools.org](mailto:jmuss07@charlottesvilleschools.org).

### **Henry Heisig**

Hi! I'm Henry, a class of 2024 student at Charlottesville High School. You can contact me at [hheisig51@charlottesvilleschools.org](mailto:hheisig51@charlottesvilleschools.org) or [henry+github@eheisig.com](mailto:henry+github@eheisig.com), or find my work on [Github](https://github.com/hheisig51).
