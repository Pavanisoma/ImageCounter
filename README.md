# ImageCounter


Both Server and client containers are hosted in public docker hub


### Steps:

1. docker run -d --name server -p 5000:5000 pavanidocid/counterserver:final

2. docker run -d --name client -p 8081:8080 pavanidocid/countertypescript:final

3. Open your browser to http://localhost:8081 and you should see the app



### Features:


1.Able to upvate or downvote the image score


2. Retrieve image score when application is running


3.Storing images in AWS S3 bucket and fetching images through REST API call


