Scrapy Price Monitor
====================

This is a simple price monitor built with [Scrapy](https://github.com/scrapy/scrapy)
and [Scrapy Cloud](https://www.zyte.com/scrapy-cloud/). It is an updated version of 
[this sample](https://github.com/scrapinghub/sample-projects/tree/master/scrapy_price_monitor/_scrapy_price_monitor_OLD).

It is basically a Scrapy project with one spider for each online retailer that
we want to monitor prices from. In addition to the spiders, there's a Python
Script that is scheduled to run periodically on Scrapy Cloud, checking whether
the latest prices are the best ones in a given time span. If so, the monitor
sends an email alerting you about the price drops.


## Including Products to Monitor

There's a `resources/urls.json` file that lists the URLs from the products that
we want to monitor. If you just want to include a new product to monitor from
the already supported retailers, just add a new key for that product and add
the URL list as its value, such as:

    {
        "NewProduct": [
            "http://url.for.retailer.x",
            "http://url.for.retailer.y",
            "http://url.for.retailer.z"
        ]
    }


## Supporting Further Retailers

To add a retailer, just create a spider to handle the product pages from it.
To include a spider for fake-website.com, you could run:

    $ scrapy genspider fake-website.com fake-website.com

And then you can open the newly created `fake_website_com.py` file in your IDE to edit the file.

Have a look at the sample books.toscrape.com spider and implement the new ones using the same
structure, subclassing `BaseSpider` instead of `scrapy.Spider`. This way, your
spiders will automatically read the URLs list from `resources/urls.json`.


## Customizing the Price Monitor

The price monitor script uses an `send_alert` function in the `price_monitor/bin/alert.py` 
file to send an alert.  The current sample sends an email using Amazon SES 
service, so to run it you  have to set both `AWS_ACCESS_KEY` and `AWS_SECRET_KEY` 
variables in the file, along with details for the email sender and intended recipient.
If you want to use another email service or another form of alert altogether,
you can rewrite this file and include an equivalent `send_alert` function.

The price monitor can be further customized via parameters to the
`price_monitor/bin/monitor.py` script. We will dig on those parameters
later when showing how to schedule the project on Scrapy Cloud.


## Installing and Running

1. Clone this repo:

        $ git clone git@github.com:scrapinghub/sample-projects.git

2. Enter the folder and install the project dependencies:

        $ cd scrapy_price_monitor
        $ pip install -r requirements.txt

3. Create an account on Zyte:  
https://app.zyte.com/

4. Scroll to Scrapy Cloud Projects, select Creat Project take note of the project ID in the new project's url.

5. Install [Scrapinghub command line tool (shub)](https://github.com/scrapinghub/shub):

        $ pip install shub

6. Authenticate using your Scrapinghub API key:

        $ shub login

7. Finally, deploy the local project to your Scrapy Cloud project:

        $ shub deploy <your_project_id_here>

This video also explains how to deploy a Scrapy project to Scrapy Cloud:
https://youtu.be/JYch0zRmcgU


## How to Schedule on Scrapy Cloud

After you have deployed the project to Scrapy Cloud, it's time to schedule its
execution on Scrapy Cloud.

This project has two main components:

- the [**spiders**](https://github.com/scrapinghub/sample-projects/blob/master/scrapy_price_monitor/price_monitor/spiders) that collect prices from the retailers' websites
- the [**price monitor script**](https://github.com/scrapinghub/sample-projects/blob/master/scrapy_price_monitor/bin/monitor.py) that checks whether there's a new deal in the latest prices

You have to schedule both the spiders and the monitor to run periodically on
Scrapy Cloud. It's a good idea to schedule all the spiders to run at the same
time and schedule the monitor to run about 15 minutes after the spiders.

Take a look at this video to learn how to schedule periodic jobs on Scrapy Cloud:
https://youtu.be/JYch0zRmcgU?t=1m51s


### Parameters for the Monitor Script

The monitor script takes these parameters and you can pass them via the parameters box in the
scheduling dialog:

- `--days`: how many days of data we want to compare with the scraped prices.
- `--threshold`: a margin that you can set to avoid getting alerts from minor price changes. For example, if you set it to 1.0, you will only get alerts when the price drop is bigger than $1.00.
- `--apikey`: your Scrapy Cloud API key. You can get it in: https://app.scrapinghub.com/account/apikey.
- `--project`: the Scrapy Cloud project where the monitor is deployed (you can grab it from your project URL at Scrapy Cloud).


## Running in a Local Environment

You can run this project on Scrapy Cloud or on your local environment. The only dependency
from Scrapy Cloud is the [Collections API](https://doc.scrapinghub.com/api/collections.html),
but the spiders and the monitor can be executed locally.

To do that, first add your Scrapy Cloud project id to [settings.py `SHUB_PROJ_ID` variable](https://github.com/scrapinghub/sample-projects/blob/master/scrapy_price_monitor/price_monitor/settings.py#L11).

Then run the spiders via command line:

    $ scrapy crawl books.toscrape.com

This will run the spider named as `books.toscrape.com` and store the scraped data into
a Scrapy Cloud collection, under the project you set in the last step.

You can also run the price monitor via command line:

    $ python bin/monitor.py --apikey <SCRAPINGHUB_KEY> --days 2 --threshold 1 --project <PROJ_ID>
