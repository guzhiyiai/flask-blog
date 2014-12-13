# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for, session

from app.service.post import PostService
from app.service.comment import CommentService
from app.utils.auth import login_required

from app.utils.serialization import jsonify_with_data
from app.utils.serialization import jsonify_with_error

from . import bp
from . import APIError


@bp.route('/posts', methods=['GET'])
def get_posts():
    offset = request.args.get('offset', 0, int)
    limit  = request.args.get('limit', 10, int)

    posts = PostService.get_posts()

    return jsonify_with_data(APIError.OK, posts=posts)


@bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = PostService.get_one(post_id)
    if post is None:
        return jsonify_with_error(APIError.NOT_FOUNT)
    return jsonify_with_data(APIError.OK, post=post)


@bp.route('/posts', methods=['POST'])
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')

    post = PostService.add_post(title, content)

    return jsonify_with_data(APIError.OK, post=post)


@bp.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    title = request.form.get('title')
    content = request.form.get('content')

    post = PostService.update_post(post_id, {
        'title': title,
        'content': content
    })

    return jsonify_with_data(APIError.OK)


@bp.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = PostService.get_one(post_id)
    if not post:
        return jsonify_with_error(APIError.NOT_FOUND)

    PostService.delete_post(post_id)

    return jsonify_with_data(APIError.OK)


@bp.route('/posts/<int:post_id>/comments_count', methods=['GET'])
def comments_count(post_id):
    comments_count = CommentService.get_comments_count(post_id)

    return jsonify_with_data(APIError.OK, comments_count=comments_count)


