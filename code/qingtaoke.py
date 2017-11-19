#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"
}

session = requests.session()
session.get("http://m.qingtaoke.com/", headers=headers)


def getJson():
    headers.update(
        dict(Referer="http://m.qingtaoke.com/", Host="m.qingtaoke.com"))

    getData = {
        "r": "default/webData",
        "scroll_id": "cXVlcnlUaGVuRmV0Y2g7NDsxNTAyMDY4NjM4Om1QU3JuZTI1UkFHSDItaUxGWTZoZlE7MTQ5ODA0MTAwMTotOWFOa29YNlRiT0txZDkyX0lvTUV3OzE0ODQ3NDQwMjI6VGVNR2NCZ3pTOHFnUzVQMVhKeDZ2dzsxNDgwNjgzMzQzOjAtREhSS3FYUzFtYTZFN2ZoZVZOQ1E7MDs="
    }

    preUrl = "http://m.qingtaoke.com/"
    # 抓取网页
    contentInfo = session.get(url=preUrl, params=getData, headers=headers)

    print(contentInfo.content.decode("utf-8", "ignore"))


def main():
    aa = "cXVlcnlUaGVuRmV0Y2g7NDsxNTAyMDY4NjM4Om1QU3JuZTI1UkFHSDItaUxGWTZoZlE7MTQ5ODA0MTAwMTotOWFOa29YNlRiT0txZDkyX0lvTUV3OzE0ODQ3NDQwMjI6VGVNR2NCZ3pTOHFnUzVQMVhKeDZ2dzsxNDgwNjgzMzQzOjAtREhSS3FYUzFtYTZFN2ZoZVZOQ1E7MDs="
    bb = "cXVlcnlUaGVuRmV0Y2g7NDsxNTAyMDY4NjM4Om1QU3JuZTI1UkFHSDItaUxGWTZoZlE7MTQ5ODA0MTAwMTotOWFOa29YNlRiT0txZDkyX0lvTUV3OzE0ODQ3NDQwMjI6VGVNR2NCZ3pTOHFnUzVQMVhKeDZ2dzsxNDgwNjgzMzQzOjAtREhSS3FYUzFtYTZFN2ZoZVZOQ1E7MDs="

    if aa == bb:
        print(22222222222222)
    # getJson()


if __name__ == "__main__":
    main()
