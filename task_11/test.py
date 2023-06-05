from app import Post

posts = Post.query.all()

for post in posts:
    print(post.title)
    print(post.tags)
    print('---')

from app import Post

posts = Post.query.all()

for post in posts:
    print('TITLE: ', post.title)
    print('-')
    print('TAGS:')
    for tag in post.tags:
        print('> ', tag.name)
    print('-'*30)

from app import Tag

writing_tag = Tag.query.filter_by(name='writing').first()

for post in writing_tag.posts:
    print(post.title)
    print('-'*6)
    print(post.content)
    print('-')
    print([tag.name for tag in post.tags])
    print('-'*20)


#** migrate
from app import db, Post, Tag

life_death_post = Post(title='A post on life and death', content='life and death')
joy_post = Post(title='A post on joy', content='joy')

life_tag = Tag(name='life')
death_tag = Tag(name='death')
joy_tag = Tag(name='joy')

life_death_post.tags.append(life_tag)
life_death_post.tags.append(death_tag)
joy_post.tags.append(joy_tag)

db.session.add_all([life_death_post, joy_post, life_tag, death_tag, joy_tag])

db.session.commit()