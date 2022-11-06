<h1>Measurements database processing</h1>

<h2>Console params</h2>

* <b>-f</b> [filename]: specifies the .csv file to use [MANDATORY]. Files are saved in the datasets folder.
* <b>-ds</b> [date]: start date for dataset processing. If missing, the dataset is processed from the first day. Format: YYYY-mm-dd
* <b>-de</b> [date]: end date for dataset processing. If missing, the dataset is processed until the last day. Format: YYYY-mm-dd
* <b>-hs</b> [hour]: start hour for dataset day's processing. If missing, each day is processed from the first hour. Format: hh:mm:ss
* <b>-he</b> [hour]: end hour for dataset day's processing. If missing, each day is processed until the last hour. Format: hh:mm:ss
* <b>-sd</b> [standard_deviation]: number of standard deviations for outlier detection. If missing, defaults to 3. 

<h2>Additional information</h2>

* <b>Datenum to python date</b>: http://sociograph.blogspot.com/2011/04/how-to-avoid-gotcha-when-converting.html
* <b>Boxplot</b>: https://medium.com/@agarwal.vishal819/outlier-detection-with-boxplots-1b6757fafa21