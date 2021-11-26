#!/bin/sh

curl -s 'https://api.hh.ru/vacancies?text=data+scientist&page=0&per_page=20' \
    -H 'User-Agent: Ecole42' 'Accept: application/json' \
    --fail | \
jq '. | {page, found, clusters, arguments, per_page, pages, items}' \
> hh.json
