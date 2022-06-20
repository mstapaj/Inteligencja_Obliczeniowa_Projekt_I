## Nonogram Project

A project in which nonogram puzzles are solved using genetic algorithms and swarm intelligence. The project compares the
performance and quality of different solutions for different sizes of nonograms. The program was written in python using
the pygad and pyswarms packages. The project was made for a Computer Intelligence course at the University of Gdańsk.

## Project Status

Project completed on 21 April 2022

## Project Report

[PDF with project report (Polish language)](./Projekt_1___Inteligencja_obliczeniowa.pdf)

## Technologies Used

- numpy
- pygad
- pyswarms

## Installation and Setup Instructions

#### Example:

Clone down this repository.

Installation:

`pip install -r requirements.txt`

To Run Project:

`python main.py`

## Functionalities

- The application allows you to solve the nonogram using genetic algorithms or swarm intelligence.
- You can add your own nonograms to solve them.
- You can easily set different parameters for different algorithms (genetic algorithms or swarm intelligence).
- You can measure how good a solution is. You can display:
  - the average generation (when the correct solution was reached)
  - the average time
  - the average value returned by the fitenss function
  - the percentage of correct solutions.