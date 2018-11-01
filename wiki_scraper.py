from bs4 import BeautifulSoup
import requests

def getAnchorTagLinks(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    tags = soup.findAll('a')
    links = []
    
    for i in range(len(tags)):
        try:
            links.append(tags[i]['href'])
        except KeyError:
            pass
    return links

def filterWikiTags(elems):
    filteredTags = []
    for elem in elems:
        if elem.startswith('/wiki/'):
            filteredTags.append(elem)
    return filteredTags

def main():
    wikiUri = 'https://en.wikipedia.org/'
    tags = []

    tags = getAnchorTagLinks(wikiUri + '/wiki/Github')
    tags = filterWikiTags(tags)

    # Prints all /wiki/ hrefs in the given URL 
    for tag in tags:
        print(tag)


if __name__ == '__main__':
    main()