[![forthebadge](https://forthebadge.com/images/badges/made-with-c-plus-plus.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Sudoku_Vision
This C++ code can solve a 9x9 sudoku puzzle using Backtracking Algorithm! <br>
For the Telegram bot refer to [this](https://github.com/Mastermind0100/Telegram-Sudoku-Solver) repository!

![Screenshot from 2019-05-07 21-40-20](https://user-images.githubusercontent.com/36446402/57315344-04c65400-7111-11e9-939c-fce34eb7ceea.png)


## **Backtracking Algorithm**

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, that incrementally builds candidates to the solutions, and abandons each partial candidate (“backtracks”) as soon as it determines that the candidate cannot possibly be completed to a valid solution.
Abandoning a candidate typically results in visiting a previous stage of the problem-solving-process. This is what it means to “backtrack” — visit a previous stage and explore new possibilities from thereon.

Backtracking is a systematic way of trying out different sequences of decisions until we find one that "works."

---

## Pseudocode
```cpp
function backtrack(position){
    if (isEndOfGrid == true){ // Empty cells filled. Solution found. Abort
        return true;
    }
 
    foreach (x from 1 ... 9){
        grid[position] = x;
        if (gridIsValid == true){ // Check for collisions
            if (backtrack(nextPosition) == true){ // Move to next empty cell
                return true; // Empty cells filled. Solution found. Abort.
            }
        }
    }
    grid[position] = NULL; // Empties cell
    return false; //Solution not found. Backtrack.
}
```
## Sudoku Problem
Given a, possibly, partially filled grid of size 9x9, completely fill the grid with number between 1 and 9.

A fully filled grid is a solution if:

- Each row has all numbers form 1 to 9.
- Each column has all numbers form 1 to 9.
- Each sub-grid (if any) has all numbers form 1 to 9.
---
## Cloning
```bash
$ git clone https://github.com/7enTropy7/Sudoku_Vision.git
```

## Dependencies
```bash
$ pip3 install -r requirements.txt
```
## Directory Contents
```bash
$ cd Sudoku_Vision
$ tree
.
├── a.out
├── app.py
├── fmodelwts.h5
├── main.py
├── README.md
├── requirements.txt
├── square.png
├── sudoku.cpp
├── test2.jpg
├── test_images
│   └── 2020-02-04_01-22-40.png
├── testing123.png
├── test.jpeg
└── unsolved.txt

1 directory, 13 files
```
---
## Image Processing
### Image Input
![test2](https://user-images.githubusercontent.com/36445600/73818844-3e4cfc80-4814-11ea-90c1-9984e0e747dd.jpg)

### Processed Image
![square](https://user-images.githubusercontent.com/36445600/73818744-09d94080-4814-11ea-95fe-8ace558b2422.png)

## Backtracking Algorithm

![m6e1QyV](https://user-images.githubusercontent.com/36446402/72595594-2f1f1100-3930-11ea-88b1-380db6fa5048.gif)


## Authors
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Unnikrishnan-teal.svg)](https://www.linkedin.com/in/unnikrishnan-menon-aa013415a/) [![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Atharva-orange.svg)](https://www.linkedin.com/in/atharva-hudlikar/)

* [**Unnikrishnan Menon**](https://github.com/7enTropy7)
* [**Atharva Hudlikar**](https://github.com/Mastermind0100)


## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat)](http://badges.mit-license.org)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
