# W205-Exercise-2

This repository uses Storm, Twitter API, and Postgres to stream twitter data, parse each word, and display the word count. Serving scripts can be run in real-time on the streaming data. View [architecture](/Architecture.pdf) documentation for a more detailed overview.

## Environment and Tool Setup
If running an AWS UCB AMI, ensure your environment is setup correctly (mount external disc to /data and start postgres):
```
mount -t ext4 /dev/xvdf /data
/data/start_postgres.sh
```

Clone the repo in your desired location:
```
git clone https://github.com/jrosenfeld13/W205-Exercise-2.git
cd W205-Exercise-2/
```

Ensure all package dependencies are installed. We will be using packages like tweepy and psycopg2. Run the following code to install all necessary packages:
```
pip install -r requirements.txt
```

Twittercredentials.py

## Streaming
In order to run the Storm cluster and streamparse application, run the following:
```
python setup_db.py

cd /extweetwordcount
sparse run
```
![streamparse application](/screenshots/screenshot-setup.png)

##### Output
![streamparse application](/screenshots/screenshot-twitterStream.png)

## Serving scripts
We can query the continuously updating postgresql data table with the following scripts:
### finalresults.py
```
python finalresults.py
```
##### Output
![finalresults output](/screenshots/screenshot-finalresults1.png)

or with an optional search argument
```
python finalresults.py Trump
```
##### Output
![finalresults output](/screenshots/screenshot-finalresults.png)


#### histogram.py
```
python histogram.py
```
##### Output
![histogram output](/screenshots/screenshot-histogram.png)

#### barplot_png.py
barplot_png.py is an optional script included to create a matplotlib bar chart of the top 20 words with their counts and save it as a .png.
```
python barplot_png.py
```

##### Output
![finalresults output](/Plot.png)
