#!/usr/bin/python3
"""
This is the "task_02_requests.py" module.
"""
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)


def fetch_and_print_posts():
    """
    Fetches all post from JSONPlaceholder
    and print out the titles of all the posts
    """
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches all post from JSONPlaceholder,
    structure the data into a list of dictionaries,
    write this data into a CSV file
    """
    if response.status_code == 200:
        data = response.json()
        posts_data = []
        for post in data:
            new_post = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            posts_data.append(new_post)

        # write to csv file
        with open("posts.csv", "w", encoding="utf-8") as f:
            headers = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(posts_data)
