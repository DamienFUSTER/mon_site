# This is the main file of the flask application

# --- PACKAGE IMPORTATION ---
from flask import Flask, render_template
import os
import markdown
import frontmatter
# --- Creation of the app object
app = Flask(__name__)


def load_articles():
    articles = []
    for filename in os.listdir("articles"):
        if filename.endswith(".md"):
            path = os.path.join("articles", filename)
            with open(path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                articles.append({
                    "title": post["id"],
                    "date": post["date"],
                    "content": markdown.markdown(post.content)
                })
    # Tri par date décroissante
    articles.sort(key=lambda x: x["date"], reverse=True)
    return articles



# --- Creation of the differents routes ---
@app.route("/")
def about():
    return render_template("about_me.html")

@app.route("/blog")
def blog():
    articles = load_articles()
    return render_template("blog.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
