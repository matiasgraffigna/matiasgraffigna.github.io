# matiasgraffigna
Pagina de Matias Graffigna

## Getting started

Check quickstart from Github pages: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll

Install Jekyll: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll#prerequisites

Clone the repo:

```bash
$ git clone https://github.com/matiasgraffigna/matiasgraffigna.github.io.git
```

Navigate to `docs/` and run:

```bash
$ bundle install
```

To run a local instance with your changes:

```bash
$ bundle exec jekyll serve
```

## Update

The repo updates manually from https://github.com/alshedivat/al-folio.
Run the updater:

```sh
$ python3 update.py
```

The configuration is stored in `config.ini`, you can modify what files you want to copy from there. Watch out for these edge cases:

* `about.liquid`: Spanish translations.
* `_config.yml`: Check updated plugins.