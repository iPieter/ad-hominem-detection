# Models

## Helper

helper.py includes useful methods to be used by other scripts.

### Import it!
```
import helper
```

### Get data
```
data = helper.get_data()
``` 
get_data() will save the whole merged dataset with ad_hominems and non-fallacies as a dataframe into the variable data. 


### Get skip n-grams data

Example of skip n-grams: 
```
sent = "Insurgents killed in ongoing fighting".split()
list(skipgrams(sent, 2, 2))
[('Insurgents', 'killed'), ('Insurgents', 'in'), ('Insurgents', 'ongoing'), ('killed', 'in'), ('killed', 'ongoing'), ('killed', 'fighting'), ('in', 'ongoing'), ('in', 'fighting'), ('ongoing', 'fighting')]
 list(skipgrams(sent, 3, 2))
        [('Insurgents', 'killed', 'in'), ('Insurgents', 'killed', 'ongoing'), ('Insurgents', 'killed', 'fighting'), ('Insurgents', 'in', 'ongoing'), ('Insurgents', 'in', 'fighting'), ('Insurgents', 'ongoing', 'fighting'), ('killed', 'in', 'ongoing'), ('killed', 'in', 'fighting'), ('killed', 'ongoing', 'fighting'), ('in', 'ongoing', 'fighting')]
```

In our case:

```
data = helper.get_data_with_skip_n_grams(n, k)
``` 
get_data_with_skip_n_grams(n, k) will save the merged dataset as a dataframe but already preprocessed using skip-k n-grams. ```n``` and ```k``` are mandatory parameters.
