**Problem**

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years.

Because of this we are asked as data engineers to analyze past years data and calculate metrics such as: Top 10 Occupations and Top 10 States both for certified visa applications. 

**Approach**

To approach this problem we first need to import and clean the data then we can take the data of interest and put it into an ideal data format for processing the Top 10s and relevant percentage metric.

Importing and cleaning the data: 
	Importhing the data is done by reading the h1b_input data file line by line and splitting on the ';' character to pull out information from the csv format. Each line was placed into a list. This creates a list of lists which we can search through. And if the elements of the first row are known they can be used as a header to get information from the rest of the array.

	Once the data has been imported we needed to clean the data by processing only the certified applications. We look at the CASE_STATUS column and pop rows which don't have 'CERTIFIED' as the entry.

Calculating Top 10s:
	To collect the top 10s I created one function which would have the column title as an argument so that it could be easily adapted if future Top 10 calculations were desirable. The methodology includes using a deafaultdict(list) to capture the counting while retaining the job_title information. The defaultdict(list) format is useful because after counting we can append the percentage statistic without creating a new list or dictionary. Once the counting and percentages have been generated they are written to file.

**Run**

To run please place the input data into a csv format delimited by the ';' character. Rename this file to 'h1b_input.csv' and place it in the input folder.

Then run the program using the run.sh as follows
````
chmod +x run.sh
./run.sh
````
