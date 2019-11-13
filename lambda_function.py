import json
import re
import signal
import itertools

def lambda_handler(event, context):
    
    method = event.get('httpMethod',{}) 
        
    indexPage="""
    <html>
    <head>
      <!--Authors: Arvee Vergara, Ho Ren Sen, Jason Low, Wilson Wong-->
      <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
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
      <div id="app" style="height:100%;">
    
      <v-app id="inspire">
            <v-toolbar app dark>
         <v-toolbar-title class="change-font">
        Make your own BOTler
         </v-toolbar-title>
      </v-toolbar>
        <div>
          <v-carousel
            height="240"
            v-model="model"
            show-arrows-on-hover
            hide-delimiters
            cycle="cycle"
          >
            <v-carousel-item>
              <v-sheet
                color="secondary"
                height="100%"
                tile
              >
                <v-row
                  class="fill-height"
                  align="center"
                  justify="center"
                >
                  <div class="display-3"><v-img src="https://i.ibb.co/YcHs2ym/slide1.png" max-height="200" contain></v-img></a></div>
                </v-row>
              </v-sheet>
            </v-carousel-item>
                    <v-carousel-item>
              <v-sheet
                color="primary"
                height="100%"
                tile
              >
                <v-row
                  class="fill-height"
                  align="center"
                  justify="center"
                >
                  <div class="display-3"><v-img src="https://i.ibb.co/tqsp5hh/slide2.png" max-height="200" contain></v-img></a></div>
                </v-row>
              </v-sheet>
            </v-carousel-item>
                            <v-carousel-item>
              <v-sheet
                color="yellow darken-2"
                height="100%"
                tile
              >
                <v-row
                  class="fill-height"
                  align="center"
                  justify="center"
                >
                  <div class="display-3"><v-img src="https://i.ibb.co/Hx5RF5h/slide3.png" max-height="200" contain></v-img></a></div>
                </v-row>
              </v-sheet>
            </v-carousel-item>
                    </v-carousel-item>
                            <v-carousel-item>
              <v-sheet
                color="red"
                height="100%"
                tile
              >
                <v-row
                  class="fill-height"
                  align="center"
                  justify="center"
                >
                  <div class="display-3"><v-img src="https://i.ibb.co/TkRPhRd/slide4.png" max-height="200" contain></v-img></a></div>
                </v-row>
              </v-sheet>
            </v-carousel-item>
                                    <v-carousel-item>
              <v-sheet
                color="orange"
                height="100%"
                tile
              >
                <v-row
                  class="fill-height"
                  align="center"
                  justify="center"
                >
                  <a href="https://achievements-prod.firebaseapp.com/#/paths/-LqGVE3kx8b7ehId37O4" target="_blank"><div class="display-3"><v-img src="https://i.ibb.co/0Jj170p/slide5.png" max-height="200" contain></v-img></a></div>
                </v-row>
              </v-sheet>
            </v-carousel-item>
          </v-carousel>
        </div>
        <div style="height:100%;">
          <div id="botFrame" class="column">
                <iframe allow="microphone;" style="border:0; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);" height="80%" width="100%" src="https://console.dialogflow.com/api-client/demo/embedded/is5003teacherbot"> </iframe>
            </div>
            
            <div id="activityFrame" class="column">
            <v-tabs
            v-model="tab"
            background-color="#2b313f"
            dark
            fixed-tabs
            >
            <v-tab>Code Activities</v-tab>
            <v-tab-item>
                <v-expansion-panels focusable>
          <v-expansion-panel v-for="question in questions" :key=question.name>
            <v-expansion-panel-header>{{ question.name }} {{ question.status }}</v-expansion-panel-header>
            <v-expansion-panel-content>
              <doctest-activity v-bind:layout-things=question.layoutItems v-bind:question-name=question.name  @questionhandler="toggleQuestionStatus"/>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
        </v-tab-item>
        <v-tab>Bot Preview</v-tab>
        <v-tab-item>
        <div id="botPreviewFrame" style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
        Enter here:
                            
                                <form method="post" target="browser">
                                    <input id="txtUrl" style="width:82%;" placeholder="Enter your Dialogflow Web Demo Agent URL here" name="url" type="text" />
                                    <input style="width:8%;" type="button" value="Go" onclick="setBrowserFrameSource(); return false;"/>
                                </form>
                                <iframe id="browser" name="browser" height="60%" width="100%" style="border:0;" src=""></iframe>
                            </div>
        </v-tab-item>
        <v-tab>Bot Share</v-tab>
        <v-tab-item>
        <div id="botPreviewFrame" style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); height:65%">
        <v-row align="center" justify="center">
        <p class="font-weight-medium">Finished working on your own Botler?</p>
        </v-row>
        <v-row align="center" justify="center">
        <p class="font-weight-black">Share your chatbot on our Bot Share Platform!</p>
        </v-row>
        <v-row align="center" justify="center">
        <img style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);" width="350px" src="https://i.ibb.co/kyWMPFz/botshare.jpg"></img>
        </v-row>
        &nbsp;
        <v-row align="center" justify="center">
        <p class="font-weight-medium">Show what your chatbot can do, or get your next bot inspiration from dozens of submissions.</p>
        <v-btn href="https://zi92jie9.wixsite.com/mysite-5" target="_blank">Go to the Bot Share Website</v-btn>
        </v-row>
        </div>
        </v-tab-item>
        </div>
        </div>
                <v-footer
            absolute
            dark
          >
            <v-col
              class="text-center font-weight-light caption"
              cols="12"
            >
              <p @click.stop="about = true"><a>Created by the awesome 4some guys. ©2019</a></p>
                    <v-dialog
            v-model="about"
            max-width="450px"
          >
            <v-card>
              <v-card-title class="headline">NUS MComp IS5003 - 4some</v-card-title>
      
              <v-card-text>
              <v-row align="center" justify="center">
                <img width=90% style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);" src="https://i.ibb.co/5k3cvxb/photo6210709322506283308.jpg"></img>
                4some group members: Ho Ren Sen, Jason Low Zi Jie, Arvee Vergara, Wilson Wong Wei
              </v-row>
              </v-card-text>
      
              <v-card-actions>
                <v-spacer></v-spacer>
      
                <v-btn
                  color="green darken-1"
                  text
                  @click="about = false"
                >
                  Awesome
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
            </v-col>
          </v-footer>
      </v-app>
      </div>
    
      <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
          <script type="text/javascript">
            function setBrowserFrameSource(){
                var browserFrame = document.getElementById("browser");
                browserFrame.src= "https://console.dialogflow.com/api-client/demo/embedded/" + document.getElementById("txtUrl").value;
            }
        </script>
      <script>
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
                              <p class="font-weight-black">{{layoutItems[0].header}}
                              {{layoutItems[0].subHeader}}</p>
                              <div v-html="layoutItems[0].vModel"></div>
                              &nbsp;
                              <p class="font-weight-light">{{layoutItems[2].subHeader}}</p>
                          <v-field>
                              <v-textarea solo v-model="layoutItems[2].vModel"></v-textarea>
                              <v-btn class="ma-2" v-on:click="postContents" color="success">Submit</v-btn>
                              <div v-html="answer.htmlFeedback"></div>
                          </v-field>
                      
                  
              </div>
          </div>
          `
          })
          
          new Vue({
            el: '#app',
            vuetify: new Vuetify(),
            data () {
          return {
            about: false,
            colors: [
              'secondary',
              'primary',
              'yellow darken-2',
              'red',
              'orange',
            ],
            model: 0,
            showArrows: true,
            hideDelimiters: false,
            cycle: false,
            questions:[
                      {name:"Code Activity #1", layoutItems: [
                      {header:"Sending your first automated reply", subHeader:'', vModel:"Let's say we want our BOTler to reply with the phrase <b>'Hello World!'</b> to any messages it receives, modify the code below to:<ul><li>Assign the value <code>'Hello World!'</code> to the <code>message</code> string variable; and</li><li>Add the <code>message</code> variable as one of the agent's responses</li></ul>"},
                      {header:"", subHeader:'', vModel:"const greeting = request => {\\nreturn agent => {\\nlet message = `Hello World!`;\\nagent.add(message);\\n};\\n};"},
                      {header:"", subHeader:'Modify the code below:', vModel:"const greeting = request => {\\nreturn agent => {\\nlet message = ``;\\nagent.add();\\n};\\n};"}
                      ], status:" 🔴"},
                      {name:"Code Activity #2", layoutItems: [
                      {header:"Handling fallbacks", subHeader:'', vModel:"They say nobody is perfect; not even our BOTler! There will be instances when our bot wouldn't recognize a user's response or command. Make sure that your bot handles fallbacks so it knows what to do when it happens. Modify the code below to allow our BOTler to respond with the phrase <code>'Try again.'</code> in case of a fallback."},
                      {header:"", subHeader:'', vModel:"const defaultFallback = request => {\\nreturn agent => {\\nagent.add(`Try again.`);\\n};\\n}"},
                      {header:"", subHeader:'Modify the code below:', vModel:"const defaultFallback = request => {\\nreturn agent => {\\nagent.add(``);\\n};\\n}"}
                      ], status:" 🔴"},
                      {name:"Code Activity #3", layoutItems: [
                      {header:"Showing quick reply buttons", subHeader:'', vModel:"Lesson 4 showed us how rich responses can make interactions with your bot more visually engaging with the users. One rich response element is called suggestions or quick reply buttons. Quick reply buttons are pre-defined responses that the user can click or select to eliminate the need for us to list down response options, and to give users a faster option to respond to our bot especially if you're expecting a specific response. Now that you know how bot suggestions or quick reply buttons work, edit the code below to add 3 new suggestions: <ul><li>Yes</li><li>No</li><li>Maybe</li></ul>"},
                      {header:"", subHeader:'', vModel:"agent.add(new Suggestion(`Yes`));\\nagent.add(new Suggestion(`No`));\\nagent.add(new Suggestion(`Maybe`));"},
                      {header:"", subHeader:'Modify the code below:', vModel:"agent.add(new Suggestion(''));\\nagent.add(new Suggestion(''));\\nagent.add(new Suggestion(''));"}
                      ], status:" 🔴"},
                      {name:"Code Activity #4", layoutItems: [
                      {header:"Sending image replies", subHeader:'', vModel:"Another rich response element are image replies. From the name itself, it allows us to serve embedded images to our bot's responses. Edit the code below to allow our bot to reply with the NUS logo by: <ul><li>Assigning the NUS logo URL (http://www.nus.edu.sg/images/default-source/base/logo.png) to the <code>imageUrl</code> string variable</li></ul>"},
                      {header:"", subHeader:'', vModel:"const imageUrl = `http://www.nus.edu.sg/images/default-source/base/logo.png`;\\nagent.add(new Image(imageUrl));"},
                      {header:"", subHeader:'Modify the code below:', vModel:"const imageUrl = ``;\\nagent.add(new Image());"}
                      ], status:" 🔴"},
                      {name:"Code Activity #5", layoutItems: [
                      {header:"Putting entities into context", subHeader:'', vModel:"In Dialogflow, contexts are similar to the natural language context. If a person says to you 'I liked it very much', you need context in order to understand what they are referring to. Think of it as our bot's memory capacity for the conversation. There are 3 fundamental parts in setting a context:<ul><li>Context name: Name of the context</li><li>Context lifespan: Number of conversational turns to be stored in context</li><li>Context parameters: Optional parameters, in our case, we'll attach the entity we created earlier on</li></ul> Modify the code below to adjust our bot's <code>TravelBooking</code> context lifespan to <code>10</code> conversational turns instead of the value shown in the video."},
                      {header:"", subHeader:'', vModel:"agent.setContext({\\nname: `TravelBooking`,\\nlifespan: 10,\\nparameters: { Travel_Motivation }\\n});"},
                      {header:"", subHeader:'Modify the code below:', vModel:"agent.setContext({\\nname: `TravelBooking`,\\nlifespan: 7,\\nparameters: { Travel_Motivation }\\n});"}
                      ], status:" 🔴"}
                  ]
              }
            },
            methods: {
                      toggleQuestionStatus (response) {
                          const {data, questionName} = response
                          if (data.htmlFeedback) {
                              const searchText = data.htmlFeedback
                              searchText.search(/047404/) !== -1 ?
                                  searchText.search(/a91616/) == -1 ?
                                  this.questions.find(item => item.name === questionName).status = " ✔️"
                                  :
                                  this.questions.find(item => item.name === questionName).status = " 🤨"
                              :
                              this.questions.find(item => item.name === questionName).status = " ❌"
                          }
                      }
                  }
              })
          </script>
        </body>
        <style lang="scss" scoped>
        html {
                width:100%;
                height:100%;
                margin:auto;
                mix-blend-mode: darken
            }
        .column {
              float: left;
              width: 50%;
              height: 100%;
                padding: 20px;
                
            }
        .change-font {
            font-weight: bold;
            margin: auto;
            text-shadow: 2px 2px 4px #000000;
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
        
        # Setup variables for printing results on the UI
        tableContents = ""
        textBackgroundColor = "#ffffff"
        expectedText = ""
        receivedText = ""
        textResults = ""
        overallResults = "<font color='#047404'>Congratulations! You passed this activity!</font>"
        
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
                    overallResults = "<font color='#a91616'>Oops, sorry. There seems to be something wrong with your code. Try again.</font>"
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
                "isComplete":overallResults == "<font color='#047404'>Congratulations! You passed this activity!</font>",
                "jsonFeedback": json.dumps(overallResults),
                "htmlFeedback": htmlResults,
                "textFeedback": overallResults + "\n" + textResults
            })
            }