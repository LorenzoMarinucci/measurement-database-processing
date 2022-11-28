<h1>Measurements database processing</h1>

<h2>GUI params</h2>

When the file to be processed is chosen (MANDATORY), check the necessary params for processing the chosen dataset:

* <b>Start date:</b> start date for dataset processing. If missing, the dataset is processed from the first day. Format: YYYY-mm-dd
* <b>End date:</b> end date for dataset processing. If missing, the dataset is processed until the last day. Format: YYYY-mm-dd
* <b>Start hour:</b> start hour for dataset day's processing. If missing, each day is processed from the first hour. Format: hh:mm:ss
* <b>End hour:</b> end hour for dataset day's processing. If missing, each day is processed until the last hour. Format: hh:mm:ss
* <b>Standard deviation:</b> number of standard deviations for outlier detection. If missing, defaults to 3.

<h2>Additional information</h2>

* <b>Datenum to python date</b>: http://sociograph.blogspot.com/2011/04/how-to-avoid-gotcha-when-converting.html
* <b>Boxplot</b>: https://medium.com/@agarwal.vishal819/outlier-detection-with-boxplots-1b6757fafa21