<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FLSandell/XGQuinoa">
    <img src="images/BOKU-Logo-150-Institut-ICB-kl.png" alt="Logo" width="138" height="45">
  </a>

<h3 align="center">BetaVulgaris_RandomForests</h3>

  <p align="center">
    Variation analysis employing machine learning reveals domestication patterns and breeding trends in sugar beet
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

Cultivated beets (Beta vulgaris) are important crops, and several studies explored genomic variation in the species. Here, we applied an advanced machine learning method, random forests, on published data and find genomic variants that distinguish wild beets from domesticated beets at an accuracy of 100%. The associated genes were involved in sugar accumulation and transport, nematode resistance, and root growth. Modern breeding lines provided by leading seed companies were recognised at an accuracy of 98.5% showing a strong signal associated with resistance to fungal infection. Wild beets from a narrow region in Italy had the same variation pattern pointing to the origin of this resistance trait. We successfully differentiated accessions by company revealing genes under selection. Analyses of admixture profiles addressed genomic history, provenance, and dispersal of wild beets. Our findings provide exciting possibilities for targeted breeding and show remarkable advances of variation analysis using machine learning.



<!-- GETTING STARTED -->
## Getting Started

The code is available in three parts. The first script (FULL_RF.py) is examplary for how the models where trained. The second script (42Forests.py) is examplary for running the models with different train/test splits and the final script (sliding_window_script.ipynb) showcases how we summed up feature importances using sliding windows in order to identify signal. The code was designed to predict various traits based on sequencing data. The input file is a 0|1|2 matrix, where 0 denotes a homozygous reference position, 1 a heterozygous alternative position, and 2 a homozygous alternative position in the sugar beet reference assembly RefBeet-1.2.

The code can readily be modified to construct a predictive model for any other trait that can be inferred from sequencing data. To generate a similar input matrix for new data, a VCF file can be converted by using vcftools with the "--012" flag.


### Prerequisites

python3

jupyter (optional, to view Colours_Quinoa_Code.ipynb)

The following python modules:

xgboost

pandas

numpy


sklearn

matplotlib

<!-- Information about our group -->
## About the ICB

If you are interested in our work you can find more information [here](https://bvseq.boku.ac.at/) and on our [twitter](https://twitter.com/ICBboku).


<!-- LICENSE -->
## License

Copyright (c) 2024 Felix Sandell

Distributed under the MIT License. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Felix Leopold Sandell - [@flwasch](https://twitter.com/flwasch) - felix.sandell@boku.ac.at


<p align="right">(<a href="#readme-top">back to top</a>)</p>
