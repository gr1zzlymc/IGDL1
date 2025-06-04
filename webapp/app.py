from flask import Flask, render_template, request
import instaloader

app = Flask(__name__)
loader = instaloader.Instaloader()

@app.route('/', methods=['GET', 'POST'])
def index():
    images = []
    error = None
    url = ''
    if request.method == 'POST':
        url = request.form.get('url', '')
        try:
            shortcode = url.rstrip('/').split('/')[-1]
            if '?' in shortcode:
                shortcode = shortcode.split('?')[0]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            if post.typename == 'GraphSidecar':
                for node in post.get_sidecar_nodes():
                    images.append(node.display_url)
            else:
                images.append(post.url)
        except Exception as e:
            error = str(e)
    return render_template('index.html', images=images, url=url, error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
