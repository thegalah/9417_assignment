# 9417_assignment
##Readme
There are two parts to the code base:

* vocab.py - generates vocabulary from the training set.
  * Training set path must be set (relative to the vocab.py script)
* learn.py - implements the algorithm described above
  * Training set path must be set (relative to the learn.py script)
  * Validation set path must be set (relative to the learn.py script)
  
The scripts must be invoked using `python2 vocab.py`, `python2 learn.py`
Neither of the scripts will run if there are hidden or empty directories in either the training set path
