from app.settings.env import EnvSettings

class OllamaText:
    def __init__(self):
        self.env = EnvSettings()
        self.base_url = self.env.OLLAMA_URL
        self.base_context = ""
        
    