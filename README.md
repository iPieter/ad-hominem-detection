# Fallacy detection

## Datasets

### general

Sourced from [UKPLab/argotario](https://github.com/UKPLab/argotario).

### Ad Hominem

Sourced from [UKPLab/naacl2018-before-name-calling-habernal-et-al](https://github.com/UKPLab/naacl2018-before-name-calling-habernal-et-al).

## Running the backend server
This project uses [Pipenv](https://pipenv.readthedocs.io/en/latest/). So start with to create a virtual folder on your machine.

```bash
pipenv install
```

Afterwards, use:

```bash
pipenv shell
```

And if you want to exit the env, use:

```bash
exit
```

## Running the frontend

```bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

For detailed explanation on how things work, consult the [docs for vue-loader](http://vuejs.github.io/vue-loader).
