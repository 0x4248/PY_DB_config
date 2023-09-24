# PY DB config

Use database files as a configuration file

![demo](demo.gif)

## Usage

```python
import py_db_config

config = py_db_config.Config('config.db')

config.set('key', 'value')

config.get('key') # 'value'
config.exists('key') # True
config.delete('key')
config.close()
```

### .Config

This class is the main class of the module. It is used to create a new config file or open an existing one.

### .set

This method is used to set a value in the config file.

### .get

This method is used to get a value from the config file.

### .exists

This method is used to check if a key exists in the config file.

### .delete

This method is used to delete a key from the config file.

### .close

This method is used to close the config file.


## Licence

This project is licensed under the GNU General Public License v3.0 - see the [LICENCE](LICENCE) file for details