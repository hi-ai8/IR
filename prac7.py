import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser
from collections import deque
from datetime import datetime

def mini_crawler(start_url, max_depth=1, output_file=None):
    """Minimalist web crawler that respects robots.txt and outputs results to a file"""
    # Setup output file
    if not output_file:
        output_file = f"crawl_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Setup robots parser
    rp = RobotFileParser()
    rp.set_url(urljoin(start_url, '/robots.txt'))
    try:
        rp.read()
        can_check_robots = True
    except:
        can_check_robots = False
    
    # BFS crawling
    visited = set([start_url])
    to_visit = deque([(start_url, 1)])  # (url, depth)
    results = []
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"CRAWLER RESULTS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Starting URL: {start_url}, Max Depth: {max_depth}\n")
        f.write("-" * 60 + "\n\n")
        
        while to_visit:
            url, depth = to_visit.popleft()
            
            # Check depth and robots.txt
            if depth > max_depth:
                f.write(f"[SKIP] {url} - exceeded max depth\n")
                continue
            if can_check_robots and not rp.can_fetch('*', url):
                f.write(f"[BLOCKED] {url} - robots.txt restriction\n")
                continue
                
            print(f"Crawling: {url} (depth {depth}/{max_depth})")
            f.write(f"[CRAWL] {url}\n")
            
            try:
                # Fetch and parse
                headers = {'User-Agent': 'Python Educational Crawler'}
                response = requests.get(url, headers=headers, timeout=3)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.text.strip() if soup.title else "No title"
                
                # Record results
                f.write(f"  Title: {title}\n")
                f.write(f"  Size: {len(response.text)} bytes\n")
                results.append(url)
                
                # Find ALL links on the page
                all_links = []
                for link in soup.find_all('a', href=True):
                    next_url = urljoin(url, link['href'])
                    all_links.append(next_url)
                
                f.write(f"  Links Found: {len(all_links)}\n")
                
                # Write all links to the file
                f.write("  All URLs found on this page:\n")
                for i, link_url in enumerate(all_links, 1):
                    f.write(f"    {i}. {link_url}\n")
                
                # Find links for next level - only add unvisited links to the queue
                if depth < max_depth:
                    to_crawl_next = []
                    for next_url in all_links:
                        if next_url not in visited:
                            visited.add(next_url)
                            to_visit.append((next_url, depth + 1))
                            to_crawl_next.append(next_url)
                    
                    f.write(f"  New URLs added to crawl queue: {len(to_crawl_next)}\n")
                
                f.write("\n")
                time.sleep(1)  # Be nice to servers
                
            except Exception as e:
                f.write(f"[ERROR] {url} - {str(e)[:100]}\n\n")
        
        # Write summary
        f.write("\nALL URLS DISCOVERED\n")
        f.write("-" * 60 + "\n")
        for i, url in enumerate(visited, 1):
            f.write(f"{i}. {url}\n")
        
        f.write("\nSUMMARY\n")
        f.write("-" * 60 + "\n")
        f.write(f"Total URLs discovered: {len(visited)}\n")
        f.write(f"Successfully crawled: {len(results)}\n")
    
    print(f"\nCrawling complete! Results saved to {output_file}")
    return visited

# Run crawler
if __name__ == "__main__":
    mini_crawler("https://wikipedia.org")


# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# def simple_crawler(start_url, max_pages=5):
#     """Very simple web crawler that visits a limited number of pages"""
#     visited = set()
#     to_visit = [start_url]
    
#     print(f"Starting crawl at: {start_url}")
    
#     while to_visit and len(visited) < max_pages:
#         # Get next URL to visit
#         current_url = to_visit.pop(0)
#         if current_url in visited:
#             continue
            
#         # Mark as visited
#         visited.add(current_url)
#         print(f"Crawling: {current_url}")
        
#         try:
#             # Get page content
#             response = requests.get(current_url, timeout=3)
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # Extract title
#             title = soup.title.text.strip() if soup.title else "No title"
#             print(f"  Title: {title}")
            
#             # Find links and add to queue
#             for link in soup.find_all('a', href=True):
#                 next_url = urljoin(current_url, link['href'])
#                 if next_url not in visited:
#                     to_visit.append(next_url)
            
#         except Exception as e:
#             print(f"  Error: {str(e)[:100]}")
    
#     print(f"\nCrawl complete! Visited {len(visited)} pages")
#     return visited

# # Run crawler
# if __name__ == "__main__":
#     simple_crawler("https://example.com")