# Blog Recommendation System



https://github.com/user-attachments/assets/22d8b27a-6bce-40ba-9fdd-5b4cbdb38567



### Setting up Couchbase

1. Install Couchbase (local) server using [official guide](https://docs.couchbase.com/server/current/getting-started/do-a-quick-install.html)

2. Set up buckets and scopes

```
cluster
    |- bucket
        |- scope
            |- collection1
            |- collection2
```

My database structure is as follows:

```
cluster
    |- personalized-blogs
        |- inventory
            |- user
            |- blog
```

3. Design data model

```user
{
  "id": "1",
  "name": "human",
  "preferences": ["technology", "sports"],
  "history": ["article1", "article2"]
}
```

```blog
{
  "id": "1",
  "title": "Latest Tech Trends",
  "category": "technology",
  "tags": ["AI", "ML", "innovation"]
}
```

4. Create indices (important!)

Go to Couchbase server query and excute following:

```user collection
CREATE PRIMARY INDEX `def_primary_user` ON `blog-recommender`.`inventory`.`user`;
CREATE INDEX `def_user_id` ON `blog-recommender`.`inventory`.`user`(`id`);
```
```blog collection
CREATE PRIMARY INDEX `def_primary_blog` ON `blog-recommender`.`inventory`.`blog`;
CREATE INDEX `def_blog_id` ON `blog-recommender`.`inventory`.`blog`(`id`);
CREATE INDEX `def_blog_topic` ON `blog-recommender`.`inventory`.`blog`(`topic`);
```

### Running application

0. (Optional, but highly recommended) Create virtual Python environment

```python3 -m venv env```

1. Install packages by running `pip install -r requirements.txt`

2. Run your Couchbase server

3. In project directory, run `fastapi dev main.py`

4. Open another terminal tab and run `streamlit run interface.py`

5. Try out the app!
