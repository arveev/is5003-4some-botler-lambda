""" 
Notes:
* This activity requires Python 3.7 runtime
* Set timeout to 30s
* Note: this activity requires the bleach library which isn't provided in AWS console
* Therefore, to replicate this function, you can consider following the steps below in AWS cloud9
Steps to include bleach library in your own lambda function within AWS Cloud9
1. create a folder to contain all the files we need
2. create a file called lambda_function.py (the name has to be lambda_function)
3. navigate to the directory in terminal / command prompt and run pip install bleach -t . (-t . installs bleach to current folder)
4. zip up the contents of the folder (don't zip up the folder itself but just the contents)
5. create a new lambda function in AWS
6. then in "code entry type" dropdown box which says "edit code inline", select "upload a .zip file"
7. upload your zip file
"""

import json
import re
import signal
import itertools
    
def lambda_handler(event, context):
    
    method = event.get('httpMethod',{}) 
        
    indexPage="""
<html>
    <head>
    <meta charset="utf-8">
    <meta content="width=device-width,initial-scale=1,minimal-ui" name="viewport">
    <link rel="stylesheet" href="https://unpkg.com/vue-material@beta/dist/vue-material.min.css">
    <link rel="stylesheet" href="https://unpkg.com/vue-material@beta/dist/theme/default.css">
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic">
    <link rel="stylesheet" href="//fonts.googleapis.com/icon?family=Material+Icons">
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-147552064-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        
        gtag('config', 'UA-147552064-1');
    </script>
    <title>Make your BOTler: Creating a digital assistant</title>
    </head>
    <body>
        <h1>Make your own BOTler</h1>
        <div style="padding-left:10px;"><small><i>Botler: /bɒtlə/ noun</i>, a robot or autonomous program that serves faithfully upon command</small></div>
        <hr>
        <div style="padding-left:10px;">
            Learn how to create your own BOTler by saying 'Hi!' to TeacherBot below.
            <br>This tutorial (and many more!) may also be accessed through the <a href="https://achievements-prod.firebaseapp.com/#/paths/-LqGVE3kx8b7ehId37O4">NUS ALSET Achievements Platform</a>.
        </div>
        <hr>
        <div id="botFrame" class="column">
            <iframe allow="microphone;" frameborder="0" style="height:80%;" height="100%" width="100%" src="https://console.dialogflow.com/api-client/demo/embedded/is5003teacherbot"> </iframe>
        </div>
        <div id="panelFrame" class="column">
            <div id="app2" style="overflow-y: scroll; height:100%;">
                <md-tabs md-sync-route>
                    <md-tab id="tab-home" md-label="ACTIVITIES" to="/components/tabs" exact>
                        <div style="overflow-y: scroll; height:auto">
                            <md-steppers md-vertical>
                                <md-step v-for="question in questions" :key=question.name v-bind:md-label=question.name+question.status>
                                    <doctest-activity v-bind:layout-things=question.layoutItems v-bind:question-name=question.name  @questionhandler="toggleQuestionStatus"/>
                                </md-step>
                            </md-steppers>
                        </div>
                    </md-tab>

                    <md-tab id="tab-pages" md-label="BOT PREVIEW" to="/components/tabs/pages">
                        Enter here:
                        <div id="botPreviewFrame">
                            <form method="post" target="browser">
                                <input id="txtUrl" style="width:82%;" placeholder="Enter your Dialogflow Web Demo Agent URL here" name="url" type="text" />
                                <input style="width:8%;" type="button" value="Go" onclick="setBrowserFrameSource(); return false;"/>
                            </form>
                            <iframe id="browser" name="browser" style="height:300px;" height="auto" width="100%" src=""></iframe>
                        </div>
                    </md-tab>
                </md-tabs>
            </div>
        </div>
        
    <script src="https://unpkg.com/vue"></script>
    <script src="https://unpkg.com/vue-material@beta"></script>
    <script type="text/javascript">
        function setBrowserFrameSource(){
            var browserFrame = document.getElementById("browser");
            browserFrame.src= "https://console.dialogflow.com/api-client/demo/embedded/" + document.getElementById("txtUrl").value;
        }
    </script>
    
    <script>
        Vue.use(VueMaterial.default)

        Vue.component('doctest-activity', {
            props: ['layoutThings', 'questionName'],
            data: 
                function () {
                    return {
                        answer:{jsonFeedback:'',htmlFeedback:'',textFeedback:'',isComplete:false},
                        layoutItems: this.layoutThings
                    }
                },

            methods: {
            postContents: function () {
                // comment: leaving the gatewayUrl empty - API will post back to itself
                this.$set(this, 'answer', {jsonFeedback:'',htmlFeedback:'',textFeedback:'',isComplete:false});
                const gatewayUrl = '';
                fetch(gatewayUrl, {
                method: "POST",
                headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
                },
            body: JSON.stringify({shown:{0:this.layoutItems[1].vModel},editable:{0:this.layoutItems[2].vModel}})
            }).then(response => {
            return response.json()
            }).then(data => {
            this.answer = JSON.parse(JSON.stringify(data))
            return this.$emit('questionhandler',{data, questionName:this.questionName})
            })
            }
        },
        template: 
            `<div class="md-layout  md-gutter">
            <div id="cardGroupCreator" class="md-layout-item md-size-100">
                        <div class="md-title">{{layoutItems[0].header}}</div>
                        <div class="md-subhead">{{layoutItems[0].subHeader}}</div>
                        <div v-html="layoutItems[0].vModel"></div>
            <md-card>
                <md-card-header>
                    <md-card-header-text>
                        <div class="md-title">{{layoutItems[2].header}}</div>
                        <div class="md-subhead">{{layoutItems[2].subHeader}}</div>
                    </md-card-header-text>
                        <md-card-media>
                            <md-button class="md-raised md-primary" v-on:click="postContents">Submit</md-button>
                        </md-card-media>
                </md-card-header>
                <md-card-content>
                    <md-field>
                        <md-textarea v-model="layoutItems[2].vModel"></md-textarea>
                    </md-field>
                    <md-field>
                        <div v-html="answer.htmlFeedback"></div>
                    </md-field>
                </md-card-content>
            </md-card>
        </div>
    </div>
    `
    })

    new Vue({
        el: '#app2',
        data: function () {
            return {
            questions:[
                {name:"Code Activity #1", layoutItems: [
                {header:"Sending your first automated reply", subHeader:'', vModel:"Let's say we want our BOTler to reply with the phrase 'Hello World!' to any messages it receives, modify the code below to:<ul><li>Assign the value 'Hello World!' to the 'message' string variable; and</li><li>Add the message variable as one of the agent's responses</li></ul>"},
                {header:"", subHeader:'', vModel:"const greeting = request => {return agent => {let message = `Hello World!`;agent.add(message);};};"},
                {header:"", subHeader:'Modify the code below', vModel:"const greeting = request => {return agent => {let message = ``;agent.add();};};"}
                ], status:" 🔴"},
                {name:"Code Activity #2", layoutItems: [
                {header:"Handling fallbacks", subHeader:'', vModel:"They say nobody is perfect; not even our BOTler! There will be instances when our bot wouldn't recognize a user's response or command. Make sure that your bot handles fallbacks so it knows what to do when it happens."},
                {header:"", subHeader:'', vModel:"const greeting = request => {return agent => {let message = `Hello World!`;agent.add(message);};};"},
                {header:"", subHeader:'Modify the code below', vModel:"<h2>Todos</h2><ol><li>Meet 🎅</li></ol"}
                ], status:" 🔴"},
                {name:"Q3", layoutItems: [
                {header:"Showing quick reply buttons", subHeader:'', vModel:'Follow this <a href="https://blog.dnsimple.com/2016/09/how-dns-works/">link</a> to find out more about the DNS webcomic'},
                {header:"", subHeader:'', vModel:"const greeting = request => {return agent => {let message = `Hello World!`;agent.add(message);};};"},
                {header:"", subHeader:'Modify the code below', vModel:"Follow this <a https://blog.dnsimple.com/2016/09/how-dns-works/> to find out more about the DNS webcomic"}
                ], status:" 🔴"},
                {name:"Q4", layoutItems: [
                {header:"Sending image replies", subHeader:'', vModel:'<form action="#" method="post"><input type="text" placeholder="name" name="user_name"/><input placeholder="email" type="email" name="user_mail"/><div class="button"><button type="submit">Send your message</button></div></form>'},
                {header:"", subHeader:'', vModel:"const greeting = request => {return agent => {let message = `Hello World!`;agent.add(message);};};"},
                {header:"", subHeader:'Modify the code below', vModel:'<form action="#" method="post"><input type="text" placeholder="name" name="user_name"/><input placeholder="" type="email" name="user_mail"/><div class="button"><button type="submit">Send your message</div></form>'}
                ], status:" 🔴"},
                {name:"Q5", layoutItems: [
                {header:"Putting entities into context", subHeader:'', vModel:'<table><thead><tr><th>Actual Name</th><th>Hero Name</th></tr></thead><tbody><tr><td>Peter Parker</td><td>Spiderman</td></tr><tr><td>Bruce Banner</td><td>The Hulk</td></tr></tbody></table>'},
                {header:"", subHeader:'', vModel:"const greeting = request => {return agent => {let message = `Hello World!`;agent.add(message);};};"},
                {header:"", subHeader:'Modify the code below', vModel:'<table><thead><tr><th>Actual Name</th><th>Hero Name</th></tr></thead><tbody><tr><td>Peter Parker</td><td>Spiderman</td></tr></tbody></table>'}
                ], status:" 🔴"}
            ]
        }
        },
         methods: {
            toggleQuestionStatus (response) {
                const {data, questionName} = response
                if (data.htmlFeedback) {
                    const searchText = data.htmlFeedback
                    searchText.search(/b2d8b2/) !== -1 ?
                        searchText.search(/#ff9999/) == -1 ?
                        this.questions.find(item => item.name === questionName).status = " ✔️"
                        :
                        this.questions.find(item => item.name === questionName).status = " 🤨"
                    :
                    this.questions.find(item => item.name === questionName).status = " 🔴"
                }
            }
        }
      })
    </script>
        
    <style lang="scss" scoped>
    .md-card {
        width: 90%;
        margin: 20px;
        display: inline-block;
        vertical-align: top;
        min-height:200px
    }
    .md-card-content {
        padding-bottom: 16px !important;
    }
    button {
        margin: 10px;
        width:150px;
        height:40px
    }
    #cardGroupCreator {
        display:flex;
        flex-direction:column;
        padding-right: 0px
    }
    #cardGroupPreview .md-card {
        width: 90%;
    }
    #cardGroupPreview{
        padding-left: 0px
    }
    #cardGroupPreview .md-tab{
        height:100%
    }
    textarea {
        font-size: 1rem !important;
    }
    .md-tabs{
        width:100%;
    }
    .md-tab{
        overflow-x: scroll;
    }
    .md-tab::-webkit-scrollbar {
        width: 0px;
    }
    html {
        width:95%;
        margin:auto;
        mix-blend-mode: darken
    }
    h1{
        background: #2c3e50;
        color: #ecf0f1;
        text-shadow: 1px 1px #7f8c8d;
        padding:10px;
        height:auto;
        margin:auto;
        text-align: left
    }
    .md-content{
        min-height:300px
    }
    .md-tabs-container, .md-tabs-container .md-tab textarea, .md-tabs-content{
        height:100% !important
    }
    .md-field{
        margin:0px;
        padding:0px
    }
    .md-tabs-navigation{
        justify-content:center !important
    }
    .md-card-media{
        width:400px !important
    }
    .md-button{
        margin:10px !important;
        width:50% !important;
        display:block
    }
    .md-field:after{
        height:0px
    }
    .column {
      float: left;
      width: 50%;
      height: 100%;
    }
    .row:after {
      content: "";
      display: table;
      clear: both;
    }
    table{
        border-collapse:collapse
    }
    td {
        border:1px solid black
    }
    </style>
</html>
    """
    
    
    
    if method == 'GET':
        return {
            "statusCode": 200,
            "headers": {
            'Content-Type': 'text/html',
            },
            "body": indexPage
        }
        
    if method == 'POST':
        bodyContent = event.get('body',{}) 
        parsedBodyContent = json.loads(bodyContent)
        testCases = parsedBodyContent["shown"]["0"] 
        solution = parsedBodyContent["editable"]["0"] 

        # sanitise HTML input
        import bleach
        otherTags = ['h1','h2','h3', 'h4', 'h5', 'h6', 'blockquote', 'p', 'a', 'ul', 'ol',
        'nl', 'li', 'b', 'i', 'strong', 'em', 'strike', 'code', 'hr', 'br', 'div',
        'table', 'thead', 'caption', 'tbody', 'tr', 'th', 'td','p', 'span', 'button' ,'input']
        attrs = {
            '*': ['class'],
            'a': ['href', 'rel'],
            'img': ['alt'],
        }
        
        # Setup variables for printing results on the UI
        tableContents = ""
        textBackgroundColor = "#ffffff"
        expectedText = ""
        receivedText = ""
        textResults = ""
        overallResults = "<font color='green'>Congratulations! You passed this activity!</font>"
        
        timeout = False
        # handler function that tell the signal module to execute
        # our own function when SIGALRM signal received.
        def timeout_handler(num, stack):
            print("Received SIGALRM")
            raise Exception("processTooLong")

        # register this with the SIGALRM signal    
        signal.signal(signal.SIGALRM, timeout_handler)
        
        # signal.alarm(10) tells the OS to send a SIGALRM after 10 seconds from this point onwards.
        signal.alarm(10)

        # After setting the alarm clock we invoke the long running function.
        try:
            for (tst, sln) in zip(testCases, solution):
                sln = sln.replace('\'','`')
                if tst == sln:
                    continue
                else:
                    overallResults = "<font color='red'>Oops, sorry. There seems to be something wrong with your code. Try again.</font>"
                    break
        
        
        except Exception as ex:
            if str(ex) == "processTooLong":
                timeout = True
                print("processTooLong triggered")
        # set the alarm to 0 seconds after all is done
        finally:
            signal.alarm(0)
        
        htmlResults="""
            <html>
                <head>
                    <meta charset="utf-8">
                    <meta content="width=device-width,initial-scale=1,minimal-ui" name="viewport">
                </head>
                <body>
                        <p class="class="md-subheading">{0}</p>
                </body>         
            </html>
            """.format(overallResults, tableContents, solution)
        return {
            "statusCode": 200,
            "headers": {
            "Content-Type": "application/json",
                },
            "body":  json.dumps({
                "isComplete":overallResults == "<font color='green'>Congratulations! You passed this activity!</font>",
                "jsonFeedback": json.dumps(overallResults),
                "htmlFeedback": htmlResults,
                "textFeedback": overallResults + "\n" + textResults
            })
            }