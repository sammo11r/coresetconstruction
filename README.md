# Range-Centric Coresets in Dynamic Geometric Streams

This repository contains the code and databases used for the experimental analysis of the ranged k-median algorithm presented in the master thesis "Range-Centric Coresets in Dynamic Geometric Streams".

## Table of Contents
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Datasets](#datasets)
- [License](#license)
- [Contact](#contact)

## Overview
This repository implements the ranged k-median algorithm presented in the master thesis "Range-Centric Coresets in Dynamic Geometric Streams". The experiments are conducted on three datasets: blobs, Twitter, and Gowalla.

## Repository Structure
```plaintext
CoresetConstruction/
├── README.md
├── LICENSE
├── requirements.txt
├── src/
│   ├── CoresetConstruction.py
│   ├── PreProcessing.py
│   ├── RangedCoresetConstruction.py
│   ├── blobs.py
│   ├── cell.py
│   ├── gowalla.py
│   ├── kmedian.py
│   ├── twitter.py
│   └── visualize.py
├── datasets/
    ├── Gowalla/
    └── Twitter/
```

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies using requirements.txt

## Datasets

The experiments are conducted on the following datasets:

- Blobs: Synthetic data generated using Gaussian blobs.
- Twitter: Real-world Twitter data.
- Gowalla: Real-world Gowalla check-in data.

The datasets are stored in the datasets/ directory.

## License

This project is licensed under the MIT license. See the LICENSE file for more details.

## Contact

For any questions or inquiries, please contact Sam Nijsten.
