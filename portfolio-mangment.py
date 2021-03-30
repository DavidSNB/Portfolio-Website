import json

fileName = "portfolio"


def json_read(filename):
    with open(".\\" + filename + ".json") as file:
        return json.load(file)


def json_write(filename, data):
    with open(".\\" + filename + ".json", 'w') as file:
        json.dump(data, file)


portfolio = []

portfolio = json_read(fileName)
"""
project = {
    'Title': "Website Development",
    'Desc': "This is how I made my Website",
    'Type': "Digital",
    'Rank': 1,
    'Photo': "web-dev.jpg",
    'Status': True
}
"""


def start():
    print("What do you want to do?")
    print("1. Add a new portfolio item?")
    print("2. Update a portfolio item?")
    print("3. Rank portfolio items?")
    print("4. Update the website?")
    task = input("")

    if task == "1":
        new()
    elif task == "2":
        update()
    elif task == "3":
        rank()
    elif task == "4":
        upload()
    else:
        start()


def new():
    project = {}

    def titleInput():
        project['Title'] = input("Project Title: ")

    def descInput():
        project['Desc'] = input("Project Description: ")

    def typeInput():
        print("Project Type: ")
        print("1. Physical")
        print("2. Digital")
        print("3. Photography")
        type = input("Project Type: ")
        if type == "1":
            project['Type'] = "Physical"
        elif type == "2":
            project['Type'] = "Digital"
        elif type == "3":
            project['Type'] = "Photography"
        else:
            typeInput()

    def photoInput():
        project['Photo'] = input("Project Photo Name: ")

    def statusInput():
        print("Project Status: ")
        print("1. Active")
        print("2. Archive")
        status = input("Project Type: ")
        if status == "1":
            project['Status'] = True
        elif status == "2":
            project['Status'] = False
        else:
            statusInput()

    def changes():
        print("Result: ")
        print(project)

        print("What would you like to change: ")
        print("1. Title")
        print("2. Description")
        print("3. Project Type")
        print("4. Project Photo")
        print("5. Project Status")
        print("6. Nothing")
        change = input("")

        if change == "1":
            titleInput()
            changes()
        elif change == "2":
            descInput()
            changes()
        elif change == "3":
            typeInput()
            changes()
        elif change == "4":
            photoInput()
            changes()
        elif change == "5":
            statusInput()
            changes()
        elif change == "6":
            saving()
        else:
            changes()

    def saving():
        print("Do you want to save ")
        print("1. Yes")
        print("2. No, make changes")
        print("3. No, cancel")

        save = input("")
        if save == "1":
            ranks = []
            for proj in portfolio:
                ranks.append(proj['Rank'])

            project['Rank'] = max(ranks) + 1
            portfolio.append(project)
            json_write(fileName, portfolio)
        elif save == "2":
            changes()
        elif save == "3":
            start()
        else:
            save()

    titleInput()
    descInput()
    typeInput()
    photoInput()
    statusInput()

    changes()


def update():
    selectedProject = {}

    def projectSelect():
        print("Which project?")

        for i in range(len(portfolio)):
            print(str(i + 1) + ". " + portfolio[i]['Title'])

        print(str(len(portfolio)) + ". Nothing")

        projectID = input("")

        try:
            if 0 <= int(projectID) <= len(portfolio):
                selectedProject = portfolio[int(projectID) - 1]
            elif int(projectID) == len(portfolio) + 1:
                start()
            else:
                projectSelect()
        except ValueError:
            projectSelect()

    projectSelect()

    if selectedProject != {}:
        """
        def changes():
        print("Project Details: ")
        print(selectedProject)

        print("What would you like to change: ")
        print("1. Title")
        print("2. Description")
        print("3. Project Type")
        print("4. Project Photo")
        print("5. Project Status")
        print("6. Nothing")
        change = input("")

        if change == "1":
            titleInput()
            changes()
        elif change == "2":
            descInput()
            changes()
        elif change == "3":
            typeInput()
            changes()
        elif change == "4":
            photoInput()
            changes()
        elif change == "5":
            statusInput()
            changes()
        elif change == "6":
            saving()
        else:
            changes()
        """


def rank():
    pass


def upload():
    pass


start()
