from processing import *



mouseBtn = 0

storyBtns = {}
currStory = "first"

currentPosition = 0

word = ""
currentIndex = 1



firstList = [["input the noun(plural): ", "input the adjective: "],
        ["are"], 
        ["", ""]]
secondList = [["input the name: ", "input the adjective: ", "input the noun: "], 
             ["Please excuse ", "who is far too ", "to attend ", "class."],
             ["", "", ""]]
thirdList = [["input the name: ", "input the part of the body: ", 
              "input the type of fluid", "input a substance: "],
            ["is sick with the ", "flu. Drink more ", "and take ", "as needed."],
            ["", "", "", ""]]
fourthList = [["input the name: ", "input the place: ", "input the noun: "],
             ["is authorized to be at", "instead of ", "class"],
             ["", "", ""]]

fifthList = [["input the name: ", "input the noun: ", "input the event: "],
            ["is too cool for", "class. \n Instead, she/he will be \n attending the"],
            ["", "", ""]]
list = firstList

class Story:
    def __init__(self, list_hint, list_original, list_replace, currentPosition, word, before):
        self.list_hint = list_hint
        self.list_original = list_original
        self.list_replace = list_replace
        self.currentPosition = currentPosition
        self.word = word
        self.replaceBefore = before
        
    def draw(self):
        for x in range(len(self.list_hint)):
            fill(0, 0, 0)
            textSize(20)
            text(self.list_hint[x], 10, 30 * (x + 1))
    
    def composite(self):
        if len(self.list_original) == len(self.list_replace) + 1:
            for x in range(0, len(self.list_replace)) :
                self.word = self.word + " " + self.list_original[x] + " " + self.list_replace[x] + '\n'
            self.word = self.word + self.list_original[len(self.list_original) - 1]
        elif len(self.list_original) == len(self.list_replace) - 1:
            for x in range(0, len(self.list_original)) :
                self.word = self.word + " " + self.list_replace[x] + " " + self.list_original[x] + '\n'
            self.word = self.word + " " + self.list_replace[len(self.list_replace) - 1]
        else :
            if self.replaceBefore :
                for x in range(0, len(self.list_original)) :
                    self.word = self.word + " " + self.list_replace[x] + " " + self.list_original[x] + '\n'
            else :
                for x in range(0, len(self.list_original)) :
                    self.word = self.word + " " + self.list_original[x] + " " + self.list_replace[x] + '\n'
    def clear(self):
        
        for x in range(0, len(self.list_replace)) :
            self.list_replace[x] = ""
    
class Button:
    def __init__(self, words, x, y, w, wordx, wordy):
        self.words = words
        self.selected = False
        self.inUse = False
        self.x = x
        self.y = y
        self.width = w
        self.height = 25
        self.wordx = wordx
        self.wordy = wordy
        
    def draw(self):
        if self.selected:
            stroke(255, 153, 0)
            fill(255, 153, 0)
            rect(self.x, self.y, self.width, self.height)
            stroke(0, 0, 0)
            fill(0, 0, 0)
        else:
            stroke(0, 0, 0)
            fill(0, 0, 0)
            rect(self.x, self.y, self.width, self.height)
            stroke(255, 255, 255)
            fill(255, 255, 255)
        textSize(20)
        text(self.words, self.wordx, self.wordy)
        
    def toggle(self):
        if self.selected:
            self.selected = False
        else:
            self.selected = True
            
    def checkSelected(self, mouseX, mouseY):
        if mouseX >= self.x and mouseX <= self.x + self.width:
            if mouseY >= self.y and mouseY <= self.y + self.height:
                return True
            else:
                return False
        else:
            return False
    
        

def setup():
    global storyButton, storyBtns, currentStory
    size(550, 500)
    background(255, 255, 255)
    storyButton = Button("Start", 480, 10, 70, 490, 30) # 320 － 480
    
    firstBtn = Button("Story 1", 110, 110, 70, 115, 130)
    firstBtn.toggle()    
    storyBtns["first"] = firstBtn
    
    #secondBtn = Button("Story 2", 110, 250, 70, 115, 270)
    secondBtn = Button("Story 2", 230, 110, 70, 235, 130)
    storyBtns["second"] = secondBtn
    
    thirdBtn = Button("Story 3", 350, 110, 70, 355, 130)
    storyBtns["third"] = thirdBtn
    
    fourthBtn = Button("Story 4", 160, 200, 70, 165, 220)
    storyBtns["fourth"] = fourthBtn
    
    fifthBtn = Button("Story 5", 310, 200, 70, 315, 220)
    storyBtns["fifth"] = fifthBtn
    
    
    doneBtn = Button("Done", 240, 290, 70, 250, 310)
    storyBtns["done"] = doneBtn
    
    list = firstList
    currentStory = Story(list[0], list[1], list[2], 0, "", True)
    
    
    
def draw():
    global currentPosition, list, currentStory
    background(255,255,255)
    x = 5
    y = 10
    currX = mouse.x
    currY = mouse.y
    
    #tools button
    storyButton.draw()
    
    if currentIndex == 1 :
        list = firstList
    elif currentIndex == 2 :
        list = secondList
        
    elif currentIndex == 3 :
        list = thirdList
    elif currentIndex == 4 :
        list = fourthList
    elif currentIndex == 5 :
        list = fifthList
    
    if not storyButton.selected: 
        
        currentStory = Story(list[0], list[1], list[2], 0, "", True)
        currentStory.draw()
        
        if (currentPosition <= len(currentStory.list_hint)) :
            for x in range(0, len(currentStory.list_hint)) :
                fill(0,0,0)
                text(list[2][x], 250, 30 * (x + 1))
            
    
        if (currentPosition == len(currentStory.list_hint)):
            currentStory.composite()
            
            text("The paragraph is : ", 10, 150)
            text(currentStory.word, 20, 180)
            
            
    
    if storyButton.selected:
        drawStories()
        currentPosition = 0
        currentStory.clear()
        
    
def mousePressed():
    global currentIndex
    currX = mouse.x
    currY = mouse.y
    if mouse.button == 37:
        if currY >= 10 and currY <= 35 and currX >= 480 and currX <= 550:
            storyButton.toggle()
        else:
            mouseBtn = 37
            if storyBtns["first"].checkSelected(currX, currY):
                    currentIndex = 1 
                    toggle()
                    storyBtns["first"].toggle()
                    
            elif storyBtns["second"].checkSelected(currX, currY):
                    currentIndex = 2
                    toggle()
                    storyBtns["second"].toggle()
                    
            elif storyBtns["third"].checkSelected(currX, currY):
                    currentIndex = 3
                    toggle()
                    storyBtns["third"].toggle()
            elif storyBtns["fourth"].checkSelected(currX, currY):
                    currentIndex = 4
                    toggle()
                    storyBtns["fourth"].toggle()
                    
            elif storyBtns["fifth"].checkSelected(currX, currY):
                    currentIndex = 5
                    toggle()
                    storyBtns["fifth"].toggle()
                    
            if storyBtns["done"].checkSelected(currX, currY):
                    storyButton.toggle()
                      
    
def drawStories():
    fill(0, 204, 255)
    rect(100, 100, 350, 250)
    
    for button in storyBtns:
        storyBtns[button].draw()
        
def keyPressed():
    
    global currentPosition
    if keyboard.key >= 'a' and keyboard.key <= 'z':
        list[2][currentPosition] += keyboard.key
        
    elif keyboard.keyCode == BACKSPACE :
        list[2][currentPosition] = list[2][currentPosition][:-1];
    elif keyboard.keyCode == ENTER :
        currentPosition = currentPosition + 1;
def toggle() :
    for button in storyBtns :
        if storyBtns[button].selected :
            storyBtns[button].toggle()
        
run()