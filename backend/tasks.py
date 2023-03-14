import time

from celery import shared_task

from movie_review.models import Review


@shared_task
def add_review(movie: int, grade: int):
    print('Processing movie review...')
    time.sleep(10)
    review = Review.objects.create(movie_id=movie, grade=grade)
    print(f'Created review for movie {review.movie} with grade {review.grade}.')
