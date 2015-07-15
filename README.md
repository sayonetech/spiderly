# spiderly
## Setup the environment

<b>Step 1: Scrapy installation</b><br>
	      Scrapy requirements:<br>
		                       Python 2.7<br>
	                      	Works on Linux, Windows, Mac OSX, BSD<br>
	    <p> There are different ways to install scrapy<br>
	       * pip install Scrapy (make sure python is installed in your system)<br>
	       * Download and install an official release.<br>
         * Installing with easy_install<br></p>



<b>Step 2: Create Project</b><br>
Once installed, open your terminal and create a Scrapy project by navigating to the directory you'd like to store your project in and then running the following command:<br><br>
scrapy startproject test_sample


Item Class: Open the items.py within the ~test_sample\craigslist_sample directory. Edit the items.py file to define the fields that you want contained with the Item. 

spider must define these attributes:<br>

name: the spider's unique identifier<br>
start_urls: URLs the spider begins crawling at<br>
parse: method that parses and extracts the scraped data, which will be called with the downloaded Response object of each start URL

<b>Step 2: Test</b><br>
while in the root directory of your Scrapy project, run the following command to output the scraped data to the screen:

scrapy crawl craig

