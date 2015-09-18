Title: A Review of Transitland by Mapzen
Date: 2015-09-17
Tags: computer language, Python
slug: transitland_review
Summary: Another sweet tool from Mapzen's suite of tools

Recently I built [Transit Tally](https://github.com/srthurman/TransitTally), a small data visualization of transit options available within the DC metro area. To get the GTFS data I used the awesome [Transitland](https://transit.land/) by [Mapzen](https://mapzen.com/). Transitland is, in its own words:

> A community-run and -edited timetable and map of public transit service around the world.

At present, transit data are fetched from a GTFS zip archive, and related back to other sources. Pretty cool, right? Right.

Transitland is available to use as an API (the datastore), through a Python or Ruby client, or by way of the in-browser [Playground](https://transit.land/playground/). While developing Transit Tally, I explored the Transitland API and Python client. This post is a review of what worked well, and what might benefit from some tweaks.

###Expand Documentation
The Python client documentation gets you up and running, but it doesn't tell you the methods and variables available. The code is well written, as are the tests, so it's not too difficult to read and play around to figure out how to use it. At the same time, it's nice to be able to jump right into using a product without going having to go through the code base first.

For documentation models, the [Leaflet documentation](http://leafletjs.com/reference.html) is very well written and organized. Having something similar for the Transitland Python client would be a big help.

###Loading Large Datasets
I used the [Python client](https://github.com/transitland/transitland-python-client#working-with-a-feed) to load DC's transit feed (WMATA) and attempted to call the `load_gtfs` method. After a few failed tries, I closed out all other programs and timed it. ~25 minutes later everything was loaded.

I was able to have more success using the `mzgtfs preload` method directly, cutting down load time to a couple of minutes. However, after talking with a Mapzen team member and looking through the Python client code, I learned using `mzgtfs` isn't going to give the same capabilities as using the `transitland` package directly.

###API for Public Use
The API is great, and the endpoints are pretty self explanatory. The documentation on running locally is much appreciated for those of us who like to tinker with moving parts--for fun or as part of the learning process.

Looking at it from the perspective of someone trying to get up and running quickly, it would be nice if there was a public version that made all the data currently in the feed registry available. An access token and/or a free use limit tier is certainly reasonable, as long as it means the API is fully populated.

###Getting GTFS to JSON is a Breeze
Getting transit agencies' data is very simple using both the API and the Python client. Here's all it took to get the data for WMATA:

```python
import transitland.registry
import mzgtfs.feed
import json

#initial setup - only do once
registry = transitland.registry.FeedRegistry('../transitland-feed-registry')
feed = registry.feed('f-dqc-wmata')
feed.download('wmata-current-gtfs.zip')

#Main processing
wmata = mzgtfs.feed.Feed('wmata-current-gtfs.zip')
wmata.preload()
metro = wmata.agency('MET')

with open('wmata_metro.json','w') as outfile:
	json.dump(metro.json(),outfile)
```

In addition to the regularly scheduled JSON, the API can also return certain endpoints directly as GEOJSON. That alone is worth its weight in CSV files.

###Linking Data Sources - Brilliant!
More goodies: Transitland also "serves as a 'crosswalk' between different identifiers for the same feeds and agencies". Having one place to reference the feeds for an agency is helpful. Best of all, at least to me, stops are linked to OpenStreetMap (OSM) ways! Mighty useful for areas that don't currently have much transit data in OSM. Gets me thinking about possible methodologies for designating transit routes.

Transitland is a useful and fun tool, and I'm excited to see how it continues to grow. If you haven't tried it for yourself, check it out, along with Mapzen's plethora of other awesome tools.

**Resources**:

- [Transitland](https://transit.land/)
- [Mapzen](https://mapzen.com/)
- [Playground](https://transit.land/playground/)
- [Transit Tally](https://github.com/srthurman/TransitTally)
- [Leaflet documentation](http://leafletjs.com/reference.html)