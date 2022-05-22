
<h3 align="center">Sample GCP Cloud Function Webhook Receiver</h3>

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
    <li><a href="deployment">Deployment</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This repo contains a sample Google Cloud Function written for Python 3.8 that catches Github Organization webhook events. This sample looks for 'Repository Created" events specifically and automates creating a first issue and enabling branch protection for the default branch. The main.py file exposes a single python function which is confiured to receive JSON formatted webhook data as a built-in Flask request object. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)
* [Requests](https://docs.python-requests.org/en/latest/)
* [Google Cloud Functions](https://cloud.google.com/functions/docs/calling)
* [Google Cloud Python Runtime](https://cloud.google.com/functions/docs/concepts/python-runtime)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- DEPLOYMENT -->
## Deployment
The easiest way to deploy is to use the gcloud CLI. Install and configure the gcloud CLI for your OS: [GCloud install](https://cloud.google.com/sdk/docs/install). Then run the following from within the project root directory:
```
gcloud functions deploy github_weboook \
--runtime python38 --trigger-http --allow-unauthenticated
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png

