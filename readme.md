# Exercises in serverless computing

These exercises use the Chalice serverless framework supported by AWS to aid in the creation of serverless computing artifacts. Serverless computing has several different use cases and meanings but generally supports short well defined tasks that can be accessed through a REST endpoint. 

The Chalice framework handles and automates the details of publishing local code to the AWS Lambda server, it also supports processing events from within the AWS environment. For example a function may be triggered by addition of data to the S3 data store or Amazon SQS service.

If you are familiar with anonymous functions, you can consider AWS as anonymous functions for the web.

It is assumed that the evaluator has full understanding of the configuration and deployment of Chalice code, the actual endpoints used will be dependent on the evaluators account and other issues.


# Transform public data 

*To access this function: (since this is a get function you may access it from a browser) 
 https://YOUR_API_URL_HERE/api/authors/{author_last_name}*

The goal of this activity is grab and process information from any publicly available REST endpoint. To remove any authentication issues, an endpoint that does not require authentication was used. I selected the Random House database of authors, works and books. The list is robust, but not complete and contains ‘dirty’ data.

Given an author’s last name, the function I created returns all authors in the database with that last name and a count of the works attributed to that author. 

Due to the dirtiness of the data, the same author may show up multiple times. The function takes the list of authors and does an exact match of the firstname and lastname of the author and counts all the works attributed to that name. For example ‘Aldous Huxley’ and ‘A Huxley’ are treated as different authors even though they are likely the same author.

Possible improvements to this function would access more than one database of books and would solve or ameliorate the naming problem listed above.


# Upload PNG file

*To access this function:  (you may use curl function or Postman to access)
curl -X PUT https://YOUR_API_URL_HERE/upload/mypic.png --upload-file mypic.png --header "Content-Type:application/octet-stream"*

The goal of this activity is to post a PNG file to AWS S3 storage and return the URL associated with the PNG image.

The filtering to determine if the image is a PNG file is fairly basic and depends on string functions as opposed to OS functions.

You will have to change the S3 bucket name in the code to a bucket you have access to. You may also have to add the security policy that permits your AWS Lambda code to access to the S3 resources.


# API Status

This function has not been implemented.

Given the time constraints on this evaluation and the lack of concrete definition, I chose not to implement this function.
