import requests
import dotenv
import os
import json
from Repository.Story import delete_story_repository, save_story_repository, get_stories_repository, update_story_repository

from models.Story import Story



def create_stories(story: Story):
    dotenv.load_dotenv()

    API_KEY = os.getenv("API_KEY")


    headers = { "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json" }

    link = "https://api.openai.com/v1/chat/completions"

    id_modelo = "gpt-3.5-turbo"
    body_mensagem = {
    "model" : id_modelo,
    "messages" : [{"role" : "user", "content" : f"Em um mundo onde a demanda por narrativas originais e envolventes é alta, surge uma tecnologia inovadora: uma API capaz de gerar histórias interativas e personalizadas. Esta API oferece oportunidades ilimitadas para explorar novos cenários, personagens e enredos. Pode ser usada por websites, aplicativos, equipes de escritores, desenvolvedores de jogos e até mesmo por educadores para ensinar elementos de enredo, estrutura de história e desenvolvimento de personagem de forma interativa. Essa ferramenta não apenas oferece diversidade e interatividade, mas também se adapta às necessidades dos usuários: Inspiração para criações individuais. Testes de diferentes abordagens para histórias. Narrativas personalizadas que se adaptam às escolhas dos leitores.Com base neste contexto, por favor, continue a história a partir deste ponto... {story.description}"}],
}

    response = requests.post(link, headers=headers, data=json.dumps(body_mensagem))

    save_story_repository(story, response.json()["choices"][0]["message"]["content"])
    
    return response.json()["choices"][0]["message"]["content"]


def get_stories():
    return get_stories_repository()

def update_story(id: int, story: Story):
    return update_story_repository(id, story)

def delete_story(id: int):
    return delete_story_repository(id)