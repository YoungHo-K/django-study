from django.urls import path

from posts.views import feeds, comment_add, comment_delete, post_add, post_detail, tags, post_like

app_name = "posts"

urlpatterns = [
    path("feeds/", feeds, name="feeds"),
    path("comment_add/", comment_add, name="comment_add"),
    path(f"comment_delete/<int:comment_id>/", comment_delete, name="comment_delete"),
    path("post_add/", post_add, name="post_add"),
    path("<int:post_id>/", post_detail, name="post_detail"),
    path("tags/<str:tag_name>/", tags, name="tags"),
    path("<int:post_id>/like/", post_like, name="post_like"),
]
