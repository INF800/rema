# usage:
#   - run with default:
# 
#       ```
#       python tests/hydra/test_config_simple/run_app.py \
#       > +main=default \
#       > +read_data=dsv-default
#       ```
#       
#       ``` 
#       {'seed': 111, 'read_data': {'run': False, 'path': 'default/path/goes/here', 'unique_identifier': 'uuid'}}
#       skipping read data process ...
#       ```
#
#   - run with custom path (override) `python tests/hydra/test_config_simple/run_app.py`
#
#       ```
#       python tests/hydra/test_config_simple/run_app.py \
#       > +main=default \
#       > +read_data=dsv-default \
#       > read_data.run=true read_data.path=new/path/goes/here
#       ```
#
#       ``` output
#       {'seed': 111, 'read_data': {'run': True, 'path': 'new/path/goes/here', 'unique_identifier': 'uuid'}}
#       reading data from: new/path/goes/here
#       ```


import hydra


@hydra.main(config_path='./conf')
def read_data(cfg):
    print(cfg)
    
    if not cfg.read_data.run:
        print('skipping read data process ...')
        return
    
    print('reading data from:', cfg.read_data.path)


if __name__=='__main__':
    read_data()