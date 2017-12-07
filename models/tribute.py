class Tribute:
    def __init__(self, name, content, date_added):
        self.name = name
        self.content = content
        self.date_added = date_added

    @property
    def json_format(self):
        return {
            "name": self.name,
            "content": self.content,
            "date_added": self.date_added
        }
