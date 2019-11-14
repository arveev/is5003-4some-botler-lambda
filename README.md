
# Botler Lambda

A serverless application project in IS5003 Platform Design & Economy - *by Team 4some*

### Technology stack

 - **Frontend:** [Vuetify.js](https://vuetifyjs.com/en/getting-started/quick-start) - A simple and clean framework for Vue.js that is based on Google's Material Design language
 - **Backend:** Python 3.6 binaries and libraries running on AWS Lambda
 - **Others:** [Dialogflow](https://cloud.google.com/dialogflow/docs/) - The chatbot (known as Professor Botler) is developed using Dialogflow, a conversational NLP platform

This application uses the Vuetify.js framework
### Requirements
1. AWS Account - to host and run the serverless application on Lambda
2. Because the entire application is based on a Single HTML file deployment, that is everything you need!

### Steps for deployment
**Creating a Lambda Function**
1. Download ```lambda_function.py```.
2. Navigate to AWS [Lambda](https://ap-southeast-1.console.aws.amazon.com/lambda/home?region=ap-southeast-1#/functions).
3. Create a new serverless function. Enter a function name and choose Python 3.7 runtime. 
4. Copy the Python code from ```lambda_function.py``` and paste it into the Lambda editor.
5. You may also give the handler a name such as ```lambda_function.lambda_handler```.
6. Under Basic settings, change the timeout setting to 30 seconds.
7. Click Save.

**Creating an API Endpoint**
1. Click on Add trigger and select **API Gateway**.
2. Look and select for your Lambda function name.
3. Under Security, choose the Open option.
4. An API endpoint in a form of an AWS URL will be generated. Navigate to this URL to view the changes.

### Authors
- [arveev](https://github.com/arveev)
- [excitedlybored](https://github.com/excitedlybored)
- [horensen](https://github.com/horensen)
- [wilsonwordsofwisdom](https://github.com/wilsonwordsofwisdom)
