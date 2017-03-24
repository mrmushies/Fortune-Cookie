#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    #list of possible fortunes
    fortunes = [
        "You will win the lottery the day before you die.",
        'You will get pulled over because of your "license plate light".',
        "Someone will make you mad today!"
    ]
    #randomly select one of the fortunes
    index = random.randint(0,2)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fort_sent = "Your fortune: " + fortune
        fort_para = "<p>" + fort_sent + "</p>"

        lucky_num = "<strong>" + str(random.randint(1,100)) + "</strong>"
        num_sent = "Your lucky number: " + lucky_num
        num_para = "<p>" + num_sent + "</p>"

        new_cookie = "<a href='.'><button>New Cookie</button></a>"



        content = header + fort_para + num_para + new_cookie

        self.response.write(content)





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
