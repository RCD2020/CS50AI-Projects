import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    # damping probabilities
    weight = (1 - damping_factor) / len(corpus)
    model = { name : weight for name in corpus.keys() }

    # page probabilities
    pages = corpus[page]
    weight = damping_factor / len(pages)
    for x in pages:
        model[x] += weight

    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    # somewhere to store counts
    count = { name : 0 for name in corpus.keys() }

    # first sample
    page = list(corpus.keys())[random.randint(0, len(corpus)-1)]
    count[page] += 1
    
    # run n times
    for _ in range(n-1):
        model = transition_model(corpus, page, damping_factor)
        items = []
        weights = []
        for item, weight in model.items():
            items.append(item)
            weights.append(weight)

        nextItem = random.choices(items, weights)[0]
        count[nextItem] += 1
        
    # calculate weights and return
    return { name : amount / n for name, amount in count.items() }


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    # initialize ranks
    weight = 1 / len(corpus)
    ranks = { name : weight for name in corpus.keys() }

    # calculate ranks until change is no longer greater than 0.001
    change = 1
    dampingScore = (1 - damping_factor) / len(corpus)
    while change > 0.001:
        change = 0
        newRanks = {}
        for page in corpus.keys():
            # (1 - d) / N
            newScore = dampingScore
            
            # i
            linked = [
                name for name in corpus.keys() if page in corpus[name]
            ]

            if len(linked) == 0:
                linked = list(corpus.keys())

            # Σ_i
            sigma = 0
            for i in linked:
                # PR(i)
                pr = ranks[i]

                # NumLinks(i)
                numlinks = len(corpus[i])

                # PR(i) / NumLinks(i)
                sigma += pr / numlinks
            
            # d * Σ_i
            newScore += damping_factor * sigma
            newRanks[page] = newScore

            # calculate change
            newChange = abs(ranks[page] - newScore)
            if newChange > change:
                change = newChange
        
        ranks = newRanks

    return ranks


if __name__ == "__main__":
    main()
