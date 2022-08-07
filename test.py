class Post:
    def __init__(self,title,description):
        self.title=title
        self.description=description

    def print(self):
        print("Title "+self.title)
        print("Desc "+self.description)


post=Post("Safrin","Critical Recource")

post.print()