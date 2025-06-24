<div style="overflow: auto;">
    <figure style="float: left; margin-right: 10px; width:10%;">
      <img src="media/me_and_friends.png" alt="Image" style="width:100%;" />
      <figcaption style="font-size: small; text-align: center;">Guess who's me</figcaption>
   </figure>
    <div>
        <strong>Welcome to my personal website!</strong>
        <div>
            <li>I am a Robotics Engineer in love with the field.</li>
            <li>I hold a M.Sc. in Autonomous Systems from the Technical University of Denmark.</li>
            <li>The code to some of my projects can be found <a href="https://github.com/ionymikler">here</a>.</li>
            <li>Here are my <a href="https://drive.google.com/drive/folders/1JZU4Mqzy72IL_R7KR-ndILqpjZupWLtq?usp=drive_link">CV</a> and my <a href="https://www.linkedin.com/in/jonathanmikler/">LinkedIn</a> profile</li>
        </div>
    </div>
</div>

<div>
<hr style="visibility:hidden; margin: 6px 0;" />
</div>

This website is (**always**) a work in progress...
This place serves a double purpose.
1. As an archive of work I've done before, for now with the purpose of showing potential employers what I've done.
2. As a place to share some of the things I've learned and found interesting.

# Professional Background
Please check my [CV](https://drive.google.com/drive/folders/1JZU4Mqzy72IL_R7KR-ndILqpjZupWLtq?usp=drive_link) for a more detailed description of my professional background.

Here are some highlights:
1. **Robotics Engineer** @ [AgriRobot](https://agrirobot.ai/) 2023 - 2025
   
   **Highlight:** Robotic software testing framework
   * I co-developed a testing framework enabling ROS-based systems to test any subset of their architecture, from individual nodes to complete systems.
   * This framework turned to be so effective that the company chose to open-source it. I’m currently working on the first public release.

   **Highlight:** Speed Dependent Safety Zone Module @ Agrirobot
   * I implemented the prototype of a critical safety subsystem that dynamically calculates obstacle detection zones based on robot speed and size to ensure safe stopping distances.
   * Built the initial prototype from theoretical modeling through to a 2D dynamic simulator, accounting for kinematic effects. The end results is the calculation of detection areas that allow the robot to operate safely.

2. **Robotics Engineer** @ [Blue White Robotics](https://www.bluewhite.co/) 2020-2022
   
   **Highlight:** Autonomous Tractor project:
   
   * Took part in the core development as part of a 3-person team, building the first prototype for the autonomous tractor project. Implemented path-tracking, path-planning, and mission handling modules with basic hardware (depth camera, Arduino, GPS). 
   * The internal demo was succesful and managed to convince upper management, who were skeptical that the project could be done in-house, to shift from subcontractors to in-house development, scaling the team from 3 to 15 developers.
   * The role involved extensive field testing to validate the system, which became the company's main product with original implementations still in production use today.

   **Highlight:** Dev-support engineer:
   * For about half a year, I joined the dev-support team troubleshoot the robots deployed on the field in USA. I worked entirely remotly and Oversaw operating issues, with a team of 3 handled with over 40 tickets/month.
   * Part of this role involved developing diagnostic tools for triaging operation faults, for it to be used both by technical and non-technical people. This tool ended being very crucial for everyday operation.


# Academic Background
## I've taken some interesting courses so far:
1. [Advanced Deep Learning for Computer Vision](https://kurser.dtu.dk/course/02501)

   Main project: Detection Transformer for Monocular 3D Object Detection. Check the poster [here](courses/adlcv/adlcv_poster.pdf). The code is available [here](https://github.com/esquivelrs/MonoDETR) and notes are [here](https://ludicrous-camel-09d.notion.site/MonoDETR-d3569c480d4e44159c68b9c1c27461ff)
      * Partially disconnecting the depth-estimator lead to better performance and lower variance during training.
      * Proposing use of *disentangled* losses to improve kearning (inspired by Cube R-CNN).
      * Replaced the visual encoder with a faster one from RT-DETR to explore real-time usage.
      * Reduced Backbone size to compare performance and speed.

   Other projects:
   1. Visual Transformer for Image Classification
   2. Diffusion Models to Generate (guided and not) 16x16 game sprites.
   3. Novel View Generation with NeRFs (my favourite)

2. [Artificial Intelligence for Multi-Agent Systems](https://kurser.dtu.dk/course/02285)
   
   Main Project: Windowed Hierarchichal Cooperative A* Multi-Agent Planning.[video](), [Code](https://github.com/ionymikler/MultiAgentPlanner)
      * Developed a multi-agent planner that uses a windowed hierarchical approach to solve cooperative pathfinding problems.
      * Uses a hierarchical approach to solve the problem, where a high-level planner assigns subgoals to agents and an agent-level planner solves the pathfinding problem.
      * To solve conflicts, the planner uses a windowed approach, where agents are allowed to replan their paths within a time frame if they collide with other agents.

3. [Advanced Image Analysis Learning](https://kurser.dtu.dk/course/02506)
   
   Main Project: Probabilistic Deformable Models for Image Segmentation. [Poster](courses/adv_img_analysis/AdvImgAnalysis_Poster.pdf)
4. [Perception for Autonomous Systems](https://kurser.dtu.dk/course/34759)
5. [Logical Theories for Uncertainty and Planning](https://kurser.dtu.dk/course/02287)

   Main Project: Epistemic Logic for Reinforcement Learning. [Report](courses/logicalTheories/del-marl.pdf)

6. On the topic of RL: I'm currently studying how Reinforcement Learning works in Multi-Agent Systems, on a special course dedicated to the subject. Nothing too crazy yet, but I'm sure I'll have something to share (hopefully).

## Here are some blog posts related to the topics I've studied:
1. On the topic of Logic: I studied how epistemic logic could be used to help in the learning process of reinforcement learning agents. This was the final work of that class. The work is available [here](courses/logicalTheories/del-marl.pdf) and was done together with [Elle McFarlane](https://github.com/ellemcfarlane) a great AI engineer if you need one.
2. [A Midsummer's Bayesian Dream](bayesian/midSummer_Bayesian.md): Something cool I learned in a logical theories class (Under process...)

## Other projects:
I develop on a need-to-have basis this `shell` toolboxes:
1. Generic Shell Toolbox: [Shell Toolbox](https://github.com/ionymikler/generic_shell_toolbox)

