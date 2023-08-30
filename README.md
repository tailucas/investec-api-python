<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- ABOUT -->
## About The Project

A simple Python client library to interact with the [Investec Bank API][investec-api-products-url], one of a number of existing client [implementations][investec-open-api-url] which are also mentioned in the acknowledgement section below. This client has a few noteworthy features:

1. No runtime dependencies outside of the Python built-in functionality.
2. A single client interface `InvestecOpenApiClient` which inherits function definitions for all supported API scopes.
3. Full support for switching to API sandbox endpoints with a single client parameter `use_sandbox`.
4. Additional HTTP headers can be specified to optimize client performance, such as `{'Accept-Encoding': 'gzip, deflate, br'}`.
5. Full separation of implementation between API scope implementations for ease of extensions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LIMITATIONS -->
### Limitations

1. At the time of writing, API support is limited to the [account scope][investec-open-api-docs-url] and limited [card scope][investec-open-api-docs-card-url]. Pull requests are welcome.
2. Although Investec Bank publish their API schema as an Open API specification, I had [specific][openapi3-python-path-url] difficulty in generating a client from only the JSON schema files using a few [options][openapi-generator-url]. More experimentation is needed to obviate the need to write a client from first principles.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SETUP -->
## Setup

Get the package on [PyPi][pypi-project-url].

I recommend the use of [Poetry][python-poetry-url] for dependency and runtime management. Follow the instructions on the Poetry site [here][python-poetry-install-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- EXAMPLE -->

## Example Usage

For an example of how this library works, check out this simple [sample application][investec-pb-app-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Additional well-established Python clients built by the Investec Programmable Banking [community][investec-open-api-url]:

* [ipb-python-wrapper][ipb-python-wrapper-url]
* [investec-open-api-python][investec-open-api-python-url]
* [investec-openbanking-python][investec-open-banking-url]

Investec Open API:

* [Investec Open API][investec-api-products-url]
* [Built with Investec Open API][investec-open-api-url]

This project benefits from these supporting projects:

* [All the Shields](https://github.com/progfay/shields-with-icon)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftailucas%2Finvestec-api-python&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visits&edge_flat=true)](https://hits.seeyoufarm.com)

[contributors-shield]: https://img.shields.io/github/contributors/tailucas/investec-api-python.svg?style=for-the-badge
[contributors-url]: https://github.com/tailucas/investec-api-python/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tailucas/investec-api-python.svg?style=for-the-badge
[forks-url]: https://github.com/tailucas/investec-api-python/network/members
[stars-shield]: https://img.shields.io/github/stars/tailucas/investec-api-python.svg?style=for-the-badge
[stars-url]: https://github.com/tailucas/investec-api-python/stargazers
[issues-shield]: https://img.shields.io/github/issues/tailucas/investec-api-python.svg?style=for-the-badge
[issues-url]: https://github.com/tailucas/investec-api-python/issues
[license-shield]: https://img.shields.io/github/license/tailucas/investec-api-python.svg?style=for-the-badge
[license-url]: https://github.com/tailucas/investec-api-python/blob/master/LICENSE

[python-poetry-url]: https://python-poetry.org/
[python-poetry-install-url]: https://python-poetry.org/docs/#installation

[investec-pb-app-url]: https://github.com/tailucas/investec-pb-app

[investec-api-products-url]: https://developer.investec.com/za/api-products
[investec-open-api-docs-url]: https://developer.investec.com/za/api-products/documentation/SA_PB_Account_Information
[investec-open-api-docs-card-url]: https://developer.investec.com/za/api-products/documentation/SA_Card_Code
[investec-open-api-url]: https://gitlab.com/offerzen-community/investec-programmable-banking/command-center#built-with-investec-open-api

[ipb-python-wrapper-url]: https://github.com/GoosenA/ipb-python-wrapper
[investec-open-api-python-url]: https://github.com/devinpearson/investec-open-api-python/tree/main
[investec-open-banking-url]: https://gitlab.com/vchegwidden/investec-openbanking-python/-/tree/master/

[openapi3-python-path-url]: https://github.com/Dorthu/openapi3/blob/60fb34c6c3a35ebb9fa17d2dca51b010a6aa05ae/openapi3/paths.py#L284
[openapi-generator-url]: https://github.com/OpenAPITools/openapi-generator/tree/master

[pypi-url]: https://pypi.org/
[pypi-project-url]: https://pypi.org/project/investec-api-python/
