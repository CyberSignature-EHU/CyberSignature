<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

  <p align="left">
    <a href="https://www.youtube.com/watch?v=CaVNFbvKQgo&t=14s">View Demo</a>
    ·
    <a href="https://github.com/CyberSignature-EHU/CyberSignature/issues">Report Bug</a>
  </p>

<!-- PROJECT LOGO -->

<div align="left">
  <h1 align="left">CyberSignature</h1>
  A demo software for online payment authentication

</div>

</br>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#cite">How to cite</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

CyberSignature was born out of curiousity to use behavioural biometrics to create unique digital identities 
that can be used during online card transactions to distinguish legitimate users from fraudsters. The tool 
is implemented in Python, with a machine learning algorithm at its core. It receives user input data entries 
from a graphical user interface, similar to an online payment form, and transforms them into unique digital identities.
The home screen is shown below:

<p align="left">
  <img width="430" height="400" src="https://github.com/CyberSignature-EHU/CyberSignature/blob/main/images/screenshot.png">
</p>

### Built With

This section lists any major frameworks/libraries used to bootstrap the project. 

* [![Python][Python]][Python-url]
* [![Numpy][Numpy]][Numpy-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Kivy][Kivy]][Kivy-url]
* [![Scikit-learn][Scikit-learn]][Scikit-learn-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This documentation assumes that the user has Python 3 installed on their machine and also know how to setup a python environment for a project locally.
To get a local copy of CyberSignature up and running follow these simple example steps.

### Prerequisites

_You must install the following Python packages to run the software._

  ```sh
  Package         Version
  ------------    ------------
  python          3.8.8
  numpy           1.21.5
  pandas          1.4.4
  kivy            2.0.0
  scikit-learn    1.1.1
  ```

### Installation

_Below is an example of how you can download the CyberSignature project from Github and execute the application locally._

1. Clone the repo
   ```sh
   git clone https://github.com/CyberSignature-EHU/CyberSignature.git
   ```
2. create a Python environment for the CyberSignature project called `project/`, which has the following directory tree.
   ```sh
   project/
   |
   |_ false_data/
   |_ saved_models/
   |_ application.py
   |_ cs_logo.png
   |_ ehu_logo.png
   
   ```
3. Install  prerequisite packages above
4. Run the `application.py` file to open the application

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

_For an example of how to use the application, please view the demonstrator video [here](https://www.youtube.com/watch?v=CaVNFbvKQgo&t=14s)._

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CITE -->
## How to cite

N. Nnamoko, J. Barrowclough, M. Liptrott, and I. Korkontzelos, “CyberSignature: a user authentication tool based on behavioural biometrics,” Elsevier Softw. Impacts, 2022.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. 
Don't forget to give the project a star! Thank you!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the [![MIT][MIT-shield]][MIT-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Name: Nonso Nnamoko
<br />
e-mail: nnamokon@edgehill.ac.uk

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][Twitter-shield]][Twitter-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

The <a href="https://ktn-uk.org/projects/cybersignature/">CyberSignature</a> Project received two rounds of funding from 
<a href="https://www.ukri.org/councils/innovate-uk/">Innovate UK</a> under 
<a href="https://ktn-uk.org/programme/cyberasap/">CyberASAP</a> with Project Reference No. <a href="https://gtr.ukri.org/projects?ref=10017354">10017354</a> and 
<a href="https://gtr.ukri.org/projects?ref=10002115">10002115</a>. Special thanks to 
<a href="https://ktn-uk.org/">KTN</a> who facilitated the project delivery and to the Computer Science Department at 
<a href="https://www.edgehill.ac.uk/departments/academic/computerscience/">Edge Hill University</a>, for providing time and resources
to complete the project. The authors would also like to acknowledge participants who contributed KMT
dynamics dataset for the software development and validation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/CyberSignature-EHU/CyberSignature.svg?style=for-the-badge
[contributors-url]: https://github.com/CyberSignature-EHU/CyberSignature/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/CyberSignature-EHU/CyberSignature.svg?style=for-the-badge
[forks-url]: https://github.com/CyberSignature-EHU/CyberSignature/network/members

[stars-shield]: https://img.shields.io/github/stars/CyberSignature-EHU/CyberSignature.svg?style=for-the-badge
[stars-url]: https://github.com/CyberSignature-EHU/CyberSignature/stargazers

[issues-shield]: https://img.shields.io/github/issues/CyberSignature-EHU/CyberSignature.svg?style=for-the-badge
[issues-url]: https://github.com/CyberSignature-EHU/CyberSignature/issues

[license-shield]: https://img.shields.io/github/license/CyberSignature-EHU/CyberSignature.svg?style=for-the-badge
[license-url]: https://github.com/CyberSignature-EHU/CyberSignature/blob/main/LICENSE

[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/nnamokon/

[Twitter-shield]: https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white
[Twitter-url]: https://twitter.com/nonsonnamoko

[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://python.org/


[Numpy]: https://img.shields.io/badge/numpy-000000?style=for-the-badge&logo=numpy&logoColor=blue
[Numpy-url]: https://numpy.org/

[Pandas]: https://img.shields.io/badge/pandas-000000?style=for-the-badge&logo=pandas&logoColor=4FC08D
[Pandas-url]: https://pandas.pydata.org/

[Kivy]: https://img.shields.io/badge/Kivy-000000?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAA9lBMVEU9Pj89Pz89P0A%2BP0A%2BQEE%2FQEE%2FQUJHSUpISUpISktJSktJS0xKS0xSVFVTVFVUVlZUVldVVldVV1hdX2BeX2BeYGFgYWJhYmNoamtpamtsbW5zdXZ3eXl4eXl4eXp%2BgICDhIWEhYaJi4uUlZaUlpabm5ybnJyfoKGnqamoqqqpq6upq6yqq6yqrKyur6%2Bys7O0tre1tre%2Bv7%2B%2FwcG%2FwcLKysvKzMzV1tbV19fW1tbg4uLh4uLi5OTj5eXk5ubl5%2Bfm6Ojn6eno6eno6urp6%2Bvq6%2Bvq7Ozr7Ozr7e3s7e3t7e3t7u7v8PDx8vLz8%2FP29vb3%2BPj5%2Bfka34LwAAAE60lEQVR42uzPMQ0AAAACIC%2F7R7aHgwakJ0RERERERERERERERERERERERERERERERERERERERERERERERERERERExpxdLjmOBEEcn2tV9zIzM%2FPuMDOT3%2F9lbiCPr6x%2FK8Kuya8Drl%2BkJVWHhgSxm1baY%2Fcsn21ITtt3DUDefkt2piGWekTSvOkBSShkpNcmESRYAiBtEkGCJQDSJhEkWAIgQCJIpARAgESQWAmASAIgQBIHARJBgCQSAiSCAEkkBEgEAZJICJAIAiSRECARBEgiIUAiCJBEQoBEECCJhACJIEASCQESQYAkEgIkggBJJARIBAGSSAiQCAIkkRAgEQRIIiFAIsjQJDl3gQCJIIOW5GxHaZp0FKuHuBIA4RI2%2F%2Fn791%2B9%2Bj46uTnd1EOIRJB6CZt%2F5MH9l68%2Bj45v%2FpnRDhBXctEARJJqwMn8t%2B8%2Fe%2FVO8%2F8j4%2BetG8QZEUAkqSlg5Or9R0fz%2F9p0M37OSj3Ez8UMIJKA%2Bc8fzf9qdHTaB7Q4OkMeGoJI4s%2BvC1hBjhiIJCL8%2FQL%2BBOYHjoFCHIndefBMNyAe5ugOuZF9iCexLx0BwNEVMpYKgUgycqrO6fOAHN0hDw1BlK8jpjcunwbi6A553uQayML7xCXcwSGuI8nBILvzq5%2B4hDs4xHVYqYHML61vcgl3cEh%2FRzYG2Zpf3dzkEu7gkL4Ou%2FTUCORwfmV9s17CHRjiOC5MvUWQnYUjR72EOzDEcUz03jSCtBSyqXAJd3CI72CQVRXCJdyBIf0dCHIwq0K4hDswpL8DQVRIvYQ7OMRxEIgKqZdwB4d4DgJZWlQhXMIdHOI7IGT%2F5FlYL%2BEODvEdALK8tL5ZL%2BEODvEdBKJC6iXcgSGOA0C0LdZLuINDfAeB7KqQegl3cIjnABAVUi%2FhDg7xHACiQuol3MEhngNADudUSL2EOzjEcQDIzoIKqZdwB4Y4DgDR%2Bl4v4Q4OcR0AovNUvYQ7OMRzAMiBCqmXcAeF5NTfIYi9Aes7l3AHh9iLxnX8DfKQrO9Uwh0MIklxHX%2BDXO%2F9N2ta32sl3MEhiu8QJKeZ%2F26LcyqkUsIdGAIcgpTm23%2FPU3oWMkmW5Et3B4DYxalef4g9cdZ3mFdN1je5qXdwSBrrtUBy2nbOUzBXus%2FPIfaw1wL573drT4XQvGuGAfnWDrFrzvoOM57y4CHNWDukpDFnfYc5MxB7CAqJhvwEkJK%2B%2Fet1SFWmhwGx5wRi17f%2F9TqkJj%2BGcrFf3AaQ0jx31neS%2BzYESLHHAKIvl85TlRlNZRiQkp4TiEmyUV3I%2BHkbDsTScwCRhK7v%2FBzFIVDSApFkjRfCHRzCJR5EkoO5lRgHgEgCICX%2F9mFlPcgBIJIASMnpY5SDQCQBEB1YIxwIIgmASBLgYBBJAIRLuINDsARAmESOAIgkAEIkcoRAJAEQIJEjBiIJgACJHDEQSQBEEuCIgUgCIJIARwxEEgCRBDhiIJIAiCTAEQORBEAkAY4YiCQAIglwxEAkARBJgCMGIgmASAIcMRBJAEQS4IiBSAIgkgBHEESSt1ZqJKPnrQRAgARAiqVnkyeMyWeJOIYPKdkuZ%2FRr6daz189uJcvlbEIqxEfpzoD5vZ07FgAAAAAQ5m%2FdH8MymED2hiAgICAgICAgICAgICAgIAsEBAQEBAQEBAQEBAQEBAQEBAQkhWekCqDk8ggAAAAASUVORK5CYII%3D&logoColor=white
[Kivy-url]: https://kivy.org/

[Scikit-learn]: https://img.shields.io/badge/scikit-learn-000000?style=for-the-badge&logo=scikit-learn&logoColor=4FC08D
[Scikit-learn-url]: https://scikit-learn.org/stable/

[MIT-shield]: https://img.shields.io/badge/License-MIT-blue.svg
[MIT-url]: https://github.com/CyberSignature-EHU/CyberSignature/blob/main/LICENSE

