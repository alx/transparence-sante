# French Health Actors Transparency Dataset

**Explore the datasets interactively: [avantages.csv](https://www.google.com/fusiontables/data?docid=11BJThx1meiBhbToJB80QJOc2phX-Hot9gX6qFhj1) and [conventions.csv](https://www.google.com/fusiontables/data?docid=1Sob9ToXKtZwlDcEvXLKevA2y3hLeKn330jrNZKIY)**

This is a first try at extracting the data from [transparence.sante.gouv.fr](http://transparence.sante.gouv.fr)

The resulting files are in data:

- **avantages.csv** for the direct donations from the companies
- **conventions.csv** for the "conventions"

### Scraping yourself

- Install the dependencies: `pip install -r requirements.txt`
- Launch `python sante.py` for a single-threaded scraping
- Launch `python machinegun.py <number of threads>` to have multiple scraping processes in parrallel

Scraping is segmented via postal code and I'm missing some postal codes, feel free to do it in another way.

**TODO Better cleaning of the dataset, code cleaning and better doc**

