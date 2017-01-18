#!/usr/bin/env python3
"""Retrieve and print word from a URL.
Usage:

    python3 url_words_fetcher.py<URL>

"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        url:the URL of a utf-8 text document

    Returns:
        A list of strings containing the words from
        the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_items(items):
    """print items one per line

    Args:
    An iteration of the words to be printed


    :param items:
    :return:
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a utf-8 text document
    """
    #url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) #this is request of the URL argument from the CLI

