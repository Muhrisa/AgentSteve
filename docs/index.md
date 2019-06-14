---
layout: default
title:  Home
---
## Video Summary
<iframe width="560" height="315" src="https://www.youtube.com/embed/Dd0KOZKiN7k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Project Summary
ArchitectSteve is a tool that takes a 2D image provided by the user and constructs a replica of the building in Minecraft but in 3D form. Steve, our intelligent “agent” as we call our tool takes the image and processes that image into a series of what we loosely will call coordinates, making it easier to work in Malmo Minecraft, but can be seen as the list of vertices that determine the shape of the object. This subroutine is made possible using the external OpenCV shape detection resource from the pyimagesearch website. The result is a 3D diamond block replica, in the Minecraft world environment, of the 2D building image that was “uploaded” to ArchitectSteve. Of course, due to the height restriction of 256 blocks that exists in Minecraft due to the fact that the Minecraft world is made of 16x16x256 'chunks’, we would resize the image so that the replicated structure would not be cutoff. The 2D building-view image also gets translated in order for the resulting replica to be perceived as having depth in Minecraft, thus having a 3D pop-up structure.

## Who is Steve?
Steve had spent his whole life as a successful maze critic. Day after day, Steve spent his time running from maze to maze, occasionally spending time on his hobbies of crafting and street fighting, but it was never long before he was forced to go off and review the next maze. No matter how many times he made it through to the finish line or got stuck inside, it seemed that there was never a shortage of people eager to have Steve test out their mazes.

![Vacation](https://user-images.githubusercontent.com/15114273/58365866-f4d3a180-7e7e-11e9-8a94-949d6c45ac7c.png)

One day, Steve had had enough and he decided to run off and  take his very first vacation. Steve was so excited to be free from the mazes he had not even considered the world that awaited him. When he arrived, he was amazed that there wasn’t a hedge or stone-walled path as far as the eye could see. He was in awe. This was the first time Steve had ever seen such amazing and intricate buildings! 

![School](https://user-images.githubusercontent.com/15114273/58365864-f0a78400-7e7e-11e9-942b-1c4997a41c39.png)

Enamored with the sights of the city, Steve new that there was only one thing to do. He walked straight into the top architecture school in the city and took the first open seat. Steve devoted his time towards learning everything that he could about architecture and he began dreaming of the day when he could build his very own beautiful maze-less buildings.

![Career](https://user-images.githubusercontent.com/15114273/58365863-e9807600-7e7e-11e9-8276-6d79936eca94.png)

Steve barely graduated from school before he landed a job at the top architecture firm in the city. He was very excited to be done with judging mazes but he still wanted more. After building a rather impressive portfolio, it was time for Steve to go out on his own and realize his new dream of running his own practice
 
![Architect](https://user-images.githubusercontent.com/15114273/58365867-f8672880-7e7e-11e9-9e14-473272830693.png)

Finally, after a lot of hard work and patience, Steve had made it! He began his own architecture office in the city overlooking the beautiful skyline and he never reviewed another maze again!

## Source Code: 
https://github.com/muhrisa/ArchitectSteve

## Other Resources Used
Python Programming Language: it's easy to learn and use Python. https://www.python.org/downloads/

Malmo: a platform for Artificial Intelligence experimentation and research built on top of Minecraft. An essential part of this project so you don't have to build or install platform dependent code.
https://github.com/Microsoft/malmo

