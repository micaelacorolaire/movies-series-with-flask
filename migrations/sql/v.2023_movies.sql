CREATE TABLE public.movies(
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    title character varying NOT NULL,
    movies_director character varying NOT NULL,
    actors character varying NOT NULL,
    kind_of_movies character  varying NOT NULL,
    qualification interger NOT NULL,
    release_year interger NOT NULL
);

ALTER TABLE ONLY public.movies
ADD CONSTRAINT movies_pkey PRIMARY KEY (id_movies) 