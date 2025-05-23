import json
import os
from typing import Dict
from dotenv import load_dotenv
from app.core.scraper import fetch_articles_from_urls
from app.core.chunker import split_and_save_articles
from app.core.embedder import embed_and_store

load_dotenv()

# URLs to fetch articles from
URLS=[
    "https://techcrunch.com/2025/03/31/temporal-lands-146-million-at-a-flat-valuation-eyes-agentic-ai-expansion/",
    "https://techcrunch.com/2025/03/31/signal-sees-its-downloads-double-after-scandal/",
    "https://techcrunch.com/2025/03/31/openai-disables-video-gen-for-certain-sora-users-as-capacity-challenges-continue/",
    "https://techcrunch.com/2025/03/28/mozilla-patches-firefox-bug-exploited-in-the-wild-similar-to-bug-attacking-chrome/",
    "https://techcrunch.com/2025/03/28/whatsapp-users-can-now-add-songs-to-their-status-updates/",
    "https://techcrunch.com/2025/03/28/google-rolls-out-user-choice-billing-on-google-play-in-the-uk/",
    "https://techcrunch.com/2025/03/28/openai-peels-back-chatgpts-safeguards-around-image-creation/",
    "https://techcrunch.com/2025/03/28/tesla-takedown-protesters-are-planning-a-global-day-of-action-on-march-29-and-things-might-get-ugly/",
    "https://techcrunch.com/2025/03/28/fintech-vc-powerhouse-frank-rotman-stepping-down-from-qed-investors-to-found-his-own-startups/",
    "https://techcrunch.com/2025/03/28/elon-musk-says-xai-acquired-x/",
    "https://techcrunch.com/2025/03/26/google-fixes-chrome-zero-day-security-flaw-used-in-hacking-campaign-targeting-journalists/",
    "https://techcrunch.com/2025/03/26/fintech-mercury-lands-300m-in-sequoia-led-series-c-doubles-valuation-to-3-5b/",
    "https://techcrunch.com/2025/03/26/bradley-tusk-says-he-makes-more-money-with-equity-for-services-than-he-did-as-a-traditional-vc/",
    "https://techcrunch.com/2025/03/27/open-source-devs-are-fighting-ai-crawlers-with-cleverness-and-vengeance/",
    "https://techcrunch.com/2025/03/27/trumps-auto-tariffs-are-a-gift-to-tesla/",
    "https://techcrunch.com/2025/03/27/facebook-debuts-a-revamped-friends-tab-as-part-of-its-return-to-og-facebook/",
    "https://techcrunch.com/2025/03/27/with-the-switch-2-coming-nintendo-is-working-on-virtual-game-cards-for-cross-device-portability/",
    "https://techcrunch.com/2025/03/27/twins-first-ai-agent-is-an-invoice-retrieval-agent-for-qonto-customers/",
    "https://techcrunch.com/2025/03/27/ebay-backs-wundergraph-to-build-an-open-source-graphql-federation/",
    "https://techcrunch.com/2025/03/27/google-rolls-out-new-vacation-planning-features-to-search-maps-and-gemini/",
    "https://techcrunch.com/2025/03/27/krafton-acquires-controlling-stake-in-indian-gaming-studio-nautilus-mobile-for-14m/",
    "https://techcrunch.com/2025/03/27/certification-platform-certiverse-nabs-11m-series-a-led-by-cherryrock/",
    "https://techcrunch.com/2025/03/27/why-honeybooks-140m-in-arr-may-finally-justify-its-2-4b-zirp-era-valuation/",
    "https://techcrunch.com/2025/04/01/roblox-partners-with-google-on-ads/",
    "https://techcrunch.com/2025/04/01/nanowrimo-shut-down-after-ai-content-moderation-scandals/",
  "https://techcrunch.com/2025/04/01/an-accounting-startup-has-turned-tax-preparations-into-a-pokemon-showdown-game/",
    "https://techcrunch.com/2025/04/01/researchers-suggest-openai-trained-ai-models-on-paywalled-oreilly-books/",
    "https://www.bigtechdigest.com/week-15-2025/",
    "https://www.bigtechdigest.com/week-10-2025/",
    "https://newsnclues.neocities.org/2025-03-26/2025-03-26_technology_articles",
    "https://techcrunch.com/2025/03/31/temporal-lands-146-million-at-a-flat-valuation-eyes-agentic-ai-expansion/",
    "https://techcrunch.com/2025/03/31/signal-sees-its-downloads-double-after-scandal/",
    "https://techcrunch.com/2025/03/31/openai-disables-video-gen-for-certain-sora-users-as-capacity-challenges-continue/",
    "https://techcrunch.com/2025/03/28/mozilla-patches-firefox-bug-exploited-in-the-wild-similar-to-bug-attacking-chrome/",
    "https://techcrunch.com/2025/03/28/whatsapp-users-can-now-add-songs-to-their-status-updates/",
    "https://techcrunch.com/2025/03/28/google-rolls-out-user-choice-billing-on-google-play-in-the-uk/",
    "https://techcrunch.com/2025/03/28/openai-peels-back-chatgpts-safeguards-around-image-creation/",
    "https://techcrunch.com/2025/03/28/tesla-takedown-protesters-are-planning-a-global-day-of-action-on-march-29-and-things-might-get-ugly/",
    "https://techcrunch.com/2025/03/28/fintech-vc-powerhouse-frank-rotman-stepping-down-from-qed-investors-to-found-his-own-startups/",
    "https://techcrunch.com/2025/03/28/elon-musk-says-xai-acquired-x/",
    "https://techcrunch.com/2025/03/26/google-fixes-chrome-zero-day-security-flaw-used-in-hacking-campaign-targeting-journalists/",
    "https://techcrunch.com/2025/03/26/fintech-mercury-lands-300m-in-sequoia-led-series-c-doubles-valuation-to-3-5b/",
    "https://techcrunch.com/2025/03/26/bradley-tusk-says-he-makes-more-money-with-equity-for-services-than-he-did-as-a-traditional-vc/",
    "https://techcrunch.com/2025/03/26/19-founders-and-vcs-working-with-elon-musks-doge/",
    "https://techcrunch.com/2025/03/26/a-new-social-app-is-fighting-rage-bait/",
    "https://techcrunch.com/2025/03/27/open-source-devs-are-fighting-ai-crawlers-with-cleverness-and-vengeance/",
    "https://techcrunch.com/2025/03/27/trumps-auto-tariffs-are-a-gift-to-tesla/",
    "https://techcrunch.com/2025/03/27/facebook-debuts-a-revamped-friends-tab-as-part-of-its-return-to-og-facebook/",
    "https://techcrunch.com/2025/03/27/with-the-switch-2-coming-nintendo-is-working-on-virtual-game-cards-for-cross-device-portability/",
    "https://techcrunch.com/2025/03/27/certification-platform-certiverse-nabs-11m-series-a-led-by-cherryrock/"
]



def save_article_as_json(article: Dict):
    """
    Save article as JSON file
    
    Args:
        article: Article dictionary
    """
    directory = "articles"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filename = os.path.join(directory, f"article_{article['article_id']}.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(article, f, indent=4, ensure_ascii=False)

def main():
    """
    Process news articles:
    1. Fetch articles
    2. Clean and save articles
    3. Split into chunks
    4. Store in Chroma DB
    """
    
    # Fetch articles
    articles = fetch_articles_from_urls(URLS)
    print(f"\nReceivied {len(articles)} articles")
    
    # Process and save cleaned articles
    chunks = split_and_save_articles(articles)
    if chunks:
        embed_and_store(chunks)
    else:
        print("No chunks to store")

if __name__ == "__main__":
    main()
