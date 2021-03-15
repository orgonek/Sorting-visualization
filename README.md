# SortingAlgorithmsVisualization
## Description

A console application, written using Python language. The project contains implementation of various sorting algorithms.
Scripts allow the user to see an animation of sorting a list of numbers using a specific algorithm and data type.

### Available algorithms
- bubble_sort
- quick_sort
- merge_sort
- insertion_sort
- selection_sort


### Built With

* [Matplotlib](https://matplotlib.org/)
* [Click](https://click.palletsprojects.com/en/7.x/)
## Installation

1. Clone this repository
```console
$ git clone https://github.com/orgonek/Sorting-visualization.git
```
2. Change directory
```console
$ cd Sorting-visualization/
```
3. Install required packages
```console
$ pip install -r requirements.txt 
```

## Usage
To run tests
```console
$ pytest 
```
To run scripts
```console
$ cd src
$ python main.py [algorithm-name]
```

### Options 
```console
--data [type]
```
**random** - generates array with random values

**reversed** - creates a reverse-ordered array

**partsorted** - generates a partially ordered array




