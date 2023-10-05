CREATE TABLE public.series(
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    title character varying NOT NULL,
    serie_director character varying NOT NULL,
    actors character varying NOT NULL,
    kind_of_series character  varying NOT NULL,
    qualification interger NOT NULL,
    release_year interger NOT NULL,
    seasons interger NOT NULL,
    episodies interger NOT NULL
);

ALTER TABLE ONLY public.series
ADD CONSTRAINT series_pkey PRIMARY KEY (id_series)