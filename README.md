<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FLSandell/XGQuinoa">
    <img src="images/BOKU-Logo-150-Institut-ICB-kl.png" alt="Logo" width="138" height="45">
  </a>

<h3 align="center">BetaVulgaris_RandomForests</h3>

  <p align="center">
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

Analysis of genomic variants using random forests. 


<!-- GETTING STARTED -->
## Getting Started

TThe code is available in three parts. The first script (RF.py) is examplary for how the models where trained. The second script (RF_input_iterations.py) is examplary for running the models with different train/test splits, and the final script (windows.py) showcases how feature importances were summarized using sliding windows. The code was designed to determine genetic regions that are decisive for separating two phenotypic groups based on variant calls.. The input file is a 0|1|2 matrix generated from a VCF file using vcftools with the "--012" flag, where 0 denotes a homozygous reference position, 1 a heterozygous position, and 2 a homozygous alternative position.

The code can readily be modified to construct models that distinguish any two groups of phenotypes as long as their differentiation can be inferred from genomic variants.

### Prerequisites

* python3

The following python modules:

* pandas

* numpy

* sklearn

* matplotlib

<!-- Information about our group -->
## About the ICB

If you are interested in our work you can find more information [here](https://bvseq.boku.ac.at/) and on [X(twitter)](https://twitter.com/ICBboku).


<!-- LICENSE -->
## License

Copyright (c) 2024 Felix Sandell

Distributed under the MIT License. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Felix Leopold Sandell  felix.sandell@boku.ac.at


<p align="right">(<a href="#readme-top">back to top</a>)</p>
