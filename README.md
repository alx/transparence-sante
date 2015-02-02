# French Transparency Dataset in the Health sector

This is a first try at extracting the data from [transparence.sante.gouv.fr](http://transparence.sante.gouv.fr)

The resulting files are in data/:

- avantages.csv for the direct donations from the companies
- conventions.csv for the "conventions"

### Scraping yourself

- install the dependencies: `pip install -r requirements.txt`
- launch `python sante.py` for a single-threaded scraping
- launch `python machinegun.py <number of threads>` to have multiple scraping processes in parrallel

Scraping is segmented via postal code and I'm missing some postal codes, feel free to do it in another way.



