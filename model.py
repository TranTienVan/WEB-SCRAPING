class Example:
    def __init__(self, origin: str, meaning: str):
        self.origin = origin
        self.meaning = meaning
    def init(self, obj):
        self.origin = obj["origin"]
        self.meaning = obj["meaning"]
    def __str__(self):
        string = f"""       -> {self.origin}\n       {self.meaning}\n"""
        return string
    def toObj(self):
        return {"origin": self.origin, "meaning": self.meaning}
class Meaning:

    def __init__(self, meaning: str):   
        self.meaning = meaning      
        self.examples = []
    def init(self, obj: dict):
        self.meaning = obj["meaning"]
        self.examples = list([Example(e) for e in obj["examples"]])
    
    def addExample(self, example):
        self.examples.append(example)
    def __str__(self):
        string = f"""    + {self.meaning}\n"""
        for ex in self.examples:
            string += ex.__str__()
        
        return string
    def toObj(self):
        return {
            "meaning": self.meaning,
            "examples": list([e.toObj() for e in self.examples])
        }
        
class Block:
    
    def __init__(self, type: str):
        self.type = type
        self.meanings = []
    def init(self, obj: dict):
        self.type = obj["type"]
        self.meanings = list([Meaning(m) for m in obj["meanings"]])
    def addMeaning(self, meaning: Meaning):
        self.meanings.append(meaning)
    
    def __str__(self):
        string = f"""- {self.type}\n"""
        for mean in self.meanings:
            string += mean.__str__()
        
        return string
    def toObj(self):
        return {
            "type": self.type,
            "meanings": list([m.toObj() for m in self.meanings])
        }
class Vocabulary:
    def __init__(self, word: str, image_api: str, image: str, audio_api: str, audio: str, spelling: str):
        self.word = word
        self.image_api = image_api
        self.image = image
        self.audio_api = audio_api
        self.audio = audio
        self.spelling = spelling
        self.translation = []
    
    def addTranslation(self, translation: Block):
        self.translation.append(translation)
        
    def __str__(self):
        string = f"""- {self.word}\n- {self.image_api}\n- {self.image}\n- {self.audio_api}\n- {self.audio}\n- {self.spelling}\n"""
        
        for trans in self.translation:
            string += trans.__str__()
        
        
        return string
    def toObj(self):
        obj = {}
        obj["word"] = self.word
        obj["image_api"] = self.image_api
        obj["image"] = self.image
        obj["audio_api"] = self.audio_api
        obj["audio"] = self.audio
        obj["spelling"] = self.spelling
        
        for i, trans in enumerate(self.translation):
            obj[f"translation{i + 1}"] = trans.toObj()
        
        return obj