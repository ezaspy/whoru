<!-- PROJECT LOGO -->
<p align="center">
  <h1 align="center">whoru</h1>
  <p align="center">
    Query multiple IP addresses or domains for whois records.
    <br><br>
    <a href="https://mit-license.org">
    <img src="https://img.shields.io/badge/license-MIT-black.svg" alt="License: MIT">
    </a>
    <a href="https://github.com/whoru/issues">
    <img src="https://img.shields.io/github/issues/markdown-templates/markdown-snippets.svg" alt="Issues">
    </a>
    <a href="https://github.com/whoru/forks">
    <img src="https://img.shields.io/github/forks/markdown-templates/markdown-snippets.svg" alt="Forks">
    <a href="https://github.com/ezaspy/whoru/stargazers">
    <img src="https://img.shields.io/github/stars/markdown-templates/markdown-snippets.svg" alt="Stars">
    </a>
    <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/language-python-yellow" alt="Python">
    </a>
    <img src="https://img.shields.io/badge/subject-DFIR-red" alt="Subject">
    <a href="https://github.com/whoru/forks">
    <img src="https://img.shields.io/github/last-commit/ezaspy/whoru" alt="Last Commit">
    </a>
    <br><br>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)


<br><br>
<!-- ABOUT THE PROJECT -->
## About The Project

whoru has been created to help fellow digitial forensicators with identifying whois records for multiple IP addresses and/or domains. This has been created form the need to query multiple IOCs during incidents.
Please ensure each IOC (IP address or domain) is seperated by the new line (\n) character.
<br><br>


<!-- Prerequisites -->
## Prerequisites

`python3 -m pip install python-whois`
<br><br>


<!-- USAGE EXAMPLES -->
## Usage
`python3 whoru.py [-h] <file_of_IOCs>`
### Example
`python3 whoru.py IOC_list.txt`
### Support
See the [support](https://github.com/ezaspy/whoru/issues) for a list of commands and additional third-party tools to help with preparing images or data for whoru.
<br><br>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
<br><br>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
<br><br>


<!-- CONTACT -->
## Contact

ezaspy - ezaspython@gmail.com

Project Link: [https://github.com/ezaspy/whoru](https://github.com/ezaspy/whoru)
<br><br>


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [python-whois](https://pypi.org/project/python-whois/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ezaspy/whoru.svg?style=flat-square
[contributors-url]: https://github.com/ezaspy/whoru/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ezaspy/whoru.svg?style=flat-square
[forks-url]: https://github.com/ezaspy/whoru/network/members
[stars-shield]: https://img.shields.io/github/stars/ezaspy/whoru.svg?style=flat-square
[stars-url]: https://github.com/ezaspy/whoru/stargazers
[issues-shield]: https://img.shields.io/github/issues/ezaspy/whoru.svg?style=flat-square
[issues-url]: https://github.com/ezaspy/whoru/issues
[license-shield]: https://img.shields.io/github/license/ezaspy/whoru.svg?style=flat-square
[license-url]: https://github.com/ezaspy/whoru/master/LICENSE.txt
