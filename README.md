# relpy
I know, sounds like dog's name.  [Reinforcement Learning](www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)

Also [this paper](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Applications_files/dyna2.pdf)

## The Idea

Let's build a half dozen autonomous robots that learn how to interact with each other.  Why?  Because it's cool.  Most of this is not novel, so should be acheivable.  It's really to get used to teaching robots how to do things in the hopes that some bigger, cooler project will present itself.  For instance, we'll have to start thinking in terms of sensors and using ROS for simulation.

The intial task is to play a variant of "tag".  The robots will be in a small arena.  They (will) have the following abilities.

1. They can move
1. They can keep track of each other
1. They communicate with an off-board brain
1. They can shoot some kind of "lazer" or gun at each other.
1. They can defend against a certain direction to reduce the damage from a hit.

I want to teach them using some variants of Reinforcement Learning.  In this repo I have a couple of notebooks where I noodle out one piece at a time.
