import wikipedia
from duckduckgo_search import DDGS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ResearchAgent:
    def __init__(self):
        self.name = "Research Agent"
        self.sources = ["wikipedia", "web_search"]

    def search_wikipedia(self, topic: str) -> str:
        """Fetches summary from Wikipedia."""
        try:
            # Set language to English
            wikipedia.set_lang("en")
            # Search for the topic to get the most relevant page
            search_results = wikipedia.search(topic, results=1)
            if not search_results:
                return ""
            
            page_title = search_results[0]
            page = wikipedia.page(page_title, auto_suggest=False)
            
            # Get a substantial amount of content
            content = page.content[:2000] # Limit initial fetch to avoid overwhelming the summarizer initially
            return f"Wikipedia Source ({page_title}):\n{content}"
        except wikipedia.exceptions.DisambiguationError as e:
            logger.warning(f"Disambiguation error for {topic}: {e.options}")
            return ""
        except wikipedia.exceptions.PageError:
            logger.warning(f"Page not found on Wikipedia for topic: {topic}")
            return ""
        except Exception as e:
            logger.error(f"Error searching Wikipedia: {e}")
            return ""

    def search_web(self, topic: str) -> str:
        """Fetches snippets from DuckDuckGo to simulate web search."""
        try:
            results_text = []
            with DDGS() as ddgs:
                # Get 3 results
                results = list(ddgs.text(topic, max_results=3))
                for result in results:
                    results_text.append(f"Title: {result['title']}\nBody: {result['body']}\n")
            
            if not results_text:
                return ""
            return f"Web Search Sources:\n" + "\n".join(results_text)
        except Exception as e:
            logger.error(f"Error performing web search: {e}")
            return ""

    def run(self, topic: str) -> str:
        """Orchestrates research from multiple sources."""
        logger.info(f"Starting research for topic: {topic}")
        
        combined_data = []
        
        # 1. Wikipedia Source
        wiki_data = self.search_wikipedia(topic)
        if wiki_data:
            combined_data.append(wiki_data)
        
        # 2. Web Search Source (DuckDuckGo)
        web_data = self.search_web(topic)
        if web_data:
            combined_data.append(web_data)
            
        if not combined_data:
            raise ValueError(f"No data found for topic: {topic}")

        logger.info("Research completed successfully.")
        return "\n\n---SOURCE_SEPARATOR---\n\n".join(combined_data)