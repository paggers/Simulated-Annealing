# Simulated Annealing with Statistical Analysis
## As part of UC Berkeley's Algorithms class we learn how to cope with NP-HARD and NP-Complete problems

tl;dr we are trying to find a correct permutation given a set of restrictions in the following manner:
Given the restriction "A B C" we know that C cannot be between A and B in the resultant permutation.

Initially we tryed solving with a simple hill climbing algorithm, and when it failed we upgraded to a (parallelized) Simulated Annealing to generate a more robust and efficient solver. Finally, in order to give it a higher likelihood of success, we analyzed the restrcitions to determine likely neighbors and generated starting points accordingly.


## To read the full report go to the [project_writeup.pdf](https://github.com/paggers/Simulated-Annealing/blob/master/project_writeup.pdf)
