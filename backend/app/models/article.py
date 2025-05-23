from pydantic import BaseModel

class Article(BaseModel):
    article_id: int
    title: str
    description: str
    url: str
    maintext: str
    date_publish: str
    source_domain: str
    article_length: int
