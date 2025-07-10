from langchain_core.tools import tool
from langchain_google_community import GoogleSearchAPIWrapper

@tool
def web_search_google(search_phrase: str):
    """Search Google for recent results."""
    search = GoogleSearchAPIWrapper()
    results = search.run(search_phrase) 
    return results


tool_choices = {
    "web_search_google": web_search_google
}
