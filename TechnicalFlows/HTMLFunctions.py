
import sys
from time import sleep
from bs4 import BeautifulSoup

def InitializeHTMLReport():
    file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Reports\\frontend_html_results.html","w")
    file.write(
               '''

               <html>
<head>
<title>
            Test Report
        </title>
<style type="text/css">

        .test-result-table {

            border: 1px solid black;
            width: 800px;
        }

        .test-result-table-header-cell {

            border-bottom: 1px solid black;
            background-color: silver;
        }

        .test-result-step-command-cell {

            border-bottom: 1px solid gray;
        }

        .test-result-step-description-cell {

            border-bottom: 1px solid gray;
        }

        .ICON_Color {

            border-bottom: 1px solid gray;
            border-right: 1px solid black;
        }


        .test-result-step-result-cell-ok {

            border-bottom: 1px solid gray;
            background-color: green;
        }

        .test-result-step-result-cell-failure {

            border-bottom: 1px solid gray;
            background-color: red;
        }

        .test-result-step-result-cell-not-shown {

            border-bottom: 1px solid gray;
            background-color: yellow;
        }

        .test-result-step-result-cell-notperformed {

            border-bottom: 1px solid gray;
            background-color: white;
        }
        
        .ICON_Passed {
            border-right: 1px solid gray;
            font-weight: bold;
            border-bottom: 1px solid gray;
            background-color:  green;
        }
        .ICON_Failed {
            border-right: 1px solid gray;
            font-weight: bold;
            border-bottom: 1px solid gray;
            background-color: red;
        }
        .ICON_Warning {
            border-right: 1px solid gray;
            font-weight: bold;
            border-bottom: 1px solid gray;
            background-color:  yellow;
        }

        .test-result-describe-cell {
            background-color: tan;
            font-style: italic;
        }

        .test-cast-status-box-ok {
            border: 1px solid black;
            float: left;
            margin-right: 10px;
            width: 45px;
            height: 25px;
            background-color: green;
        }

        </style>
</head>
<body style="background-color:#dddddd">
<h1 class="test-results-header">
            Test Report
        </h1>
<table cellspacing="0" class="test-result-table">
<thead>
<tr>
<td class="test-result-table-header-cell">
                        Test Case
                    </td>
<td class="test-result-table-header-cell">
                        Description
                    </td>
<td class="test-result-table-header-cell">
                        Status
                    </td>
<td class="test-result-table-header-cell">
                        Result
                    </td>
</tr>
</thead>
<tbody>





</tbody>
</table>
</body>
</html>

               
               ''')


def AddHTMLResults(Title,Message,Status):
    
    if "pass" in Status.lower() or "success" in Status.lower() or "passed" in Status.lower():
    
        content ='''<tr class="test-result-step-row test-result-step-row-altone">
                    <td class="test-result-step-command-cell">
                                            %s
                                        </td>
                    <td class="test-result-step-description-cell">
                                            %s
                                        </td>
                    <td class="ICON_Passed">
                            <span> &#10003;</span>
                                        </td>
                    <td class="test-result-step-result-cell-ok">
                                            SUCCESS
                                        </td>

                    </tr>'''%(Title,Message)
    
    elif "fail" in Status.lower() or "failed" in Status.lower():
    
        content ='''<tr class="test-result-step-row test-result-step-row-altone">
                    <td class="test-result-step-command-cell">
                                            %s
                                        </td>
                    <td class="test-result-step-description-cell">
                                            %s
                                        </td>
                    <td class="ICON_Failed">
                                            <span> &#9747;</span>

                    </td>
                    <td class="test-result-step-result-cell-failure">
                                            FAIL
                                        </td>
                    </tr>'''%(Title,Message)
                        
    elif "not shown" in Status.lower() or "not" in Status.lower() or "shown" in Status.lower():
        
        content ='''
                    <tr class="test-result-step-row test-result-step-row-altone">
                    <td class="test-result-step-command-cell">
                                            %s
                                        </td>
                    <td class="test-result-step-description-cell">
                                            %s
                                        </td>
                    <td class="ICON_Warning">
                                            <span> &#9888;</span>
                                        </td>
                    <td class="test-result-step-result-cell-not-shown">
                                            NOT SHOWN
                                        </td>
                '''%(Title,Message)

    
    
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Reports\\frontend_html_results.html",encoding="utf8") as html:

        soup=BeautifulSoup(html,"html.parser")
    div = soup.select_one("tbody")
    # print(div)


    div.append(BeautifulSoup(content,'html.parser'))

    # print(div)
    # print(soup)
    # print (soup)

    # with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Reports\\frontend_html_results.html", 'w') as html:
    #     html.

    file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Reports\\frontend_html_results.html","w",encoding="utf8")
    file.write(str(soup))
    file.close()

def GenerateReport():
    t=6
    count=1
    print("Please wait, generating your report...",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

    sleep(3)
    print("Reports generated successfully, in order to access them please click 'More Info' button above!! ",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

 