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
```
data = helper.get_data_with_skip_n_grams(n, k)
``` 
get_data_with_skip_n_grams(n, k) will savev the merged dataset as a dataframe but already preprocessed using skip-k n-grams. ```n``` and ```k``` are mandatory parameters.
