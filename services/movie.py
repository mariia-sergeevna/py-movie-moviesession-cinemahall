from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> QuerySet[Movie]:
    if not (genres_ids or actors_ids):
        return Movie.objects.all()

    if genres_ids and actors_ids:
        return Movie.objects.filter(
            actors__in=actors_ids,
            genres__in=genres_ids
        )

    if not actors_ids:
        return Movie.objects.filter(genres__in=genres_ids)

    return Movie.objects.filter(actors__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie