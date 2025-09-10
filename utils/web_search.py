import requests
from config.config import TAVILY_API_KEY

def tavily_search(query, num_results=2):
    if not TAVILY_API_KEY:
        return []
    url = "https://api.tavily.com/search"
    try:
        resp = requests.post(url, json={"query": query, "num_results": num_results}, headers={"Authorization": f"Bearer {TAVILY_API_KEY}"})
        data = resp.json()
        return data.get("results", [])
    except Exception as e:
        return [{"title": "Error", "url": "", "content": str(e)}]

def format_results(results):
    return "\n\n".join([f"[W{i+1}] {r['title']}\n{r.get('content', '')}" for i, r in enumerate(results)])
